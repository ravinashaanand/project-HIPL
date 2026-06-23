# Deployment Guide - Project HIPL

## Prerequisites

- Docker & Docker Compose installed
- Git installed
- Python 3.11+ (for local development)
- Node.js 18+ (for frontend development)
- MySQL 8.0 client tools

## Development Deployment

### 1. Clone Repository

```bash
git clone https://github.com/ravinashaanand/project-HIPL.git
cd project-HIPL
```

### 2. Setup Environment Variables

```bash
cp .env.example .env
# Edit .env with your configuration
```

### 3. Start Docker Services

```bash
# Start all services
docker-compose up -d

# Verify services
docker-compose ps
```

### 4. Initialize Database

```bash
# Execute schema creation
docker exec hipl_mysql mysql -u hipl_user -pHIPL_SecurePass2026 hipl_db < database/schema.sql

# Seed initial data
docker exec hipl_mysql mysql -u hipl_user -pHIPL_SecurePass2026 hipl_db < database/seed_data.sql
```

### 5. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations (if using Alembic)
alembic upgrade head

# Start backend server
uvicorn app.main:app --reload --port 8000
```

### 6. Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### 7. Access Applications

- **Frontend:** http://localhost:5173
- **Backend API:** http://localhost:8000
- **API Docs:** http://localhost:8000/docs
- **N8N:** http://localhost:5678
- **MySQL:** localhost:3306
- **Redis:** localhost:6379

---

## Production Deployment

### 1. Server Setup

#### System Requirements
- OS: Ubuntu 20.04 LTS or higher
- CPU: 4+ cores
- RAM: 16GB minimum
- Storage: 100GB SSD
- Bandwidth: 10Mbps minimum

#### Install Dependencies

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Install Docker Compose
sudo apt install docker-compose -y

# Install Nginx
sudo apt install nginx -y

# Install SSL certificates (Let's Encrypt)
sudo apt install certbot python3-certbot-nginx -y
```

### 2. Clone Repository

```bash
cd /var/www
sudo git clone https://github.com/ravinashaanand/project-HIPL.git
cd project-HIPL
sudo chown -R $(whoami):$(whoami) .
```

### 3. Configure Environment

```bash
cp .env.example .env
# Edit .env with production values
vim .env
```

**Important Production Settings:**
```env
APP_ENV=production
APP_DEBUG=false
DATABASE_URL=mysql+pymysql://user:password@db-server:3306/hipl_db
REDIS_URL=redis://redis-server:6379/0
JWT_SECRET_KEY=<generate-strong-secret-key>
SECURE_COOKIES=true
HTTPS_ONLY=true
```

### 4. Generate Strong Secret Key

```bash
python3 -c "import secrets; print(secrets.token_urlsafe(32))"
```

### 5. Configure Nginx

Create `/etc/nginx/sites-available/hipl`:

```nginx
upstream backend {
    server localhost:8000;
}

upstream frontend {
    server localhost:5173;
}

server {
    listen 80;
    server_name hipl.hemrajgroup.com www.hipl.hemrajgroup.com;
    return 301 https://$server_name$request_uri;
}

server {
    listen 443 ssl http2;
    server_name hipl.hemrajgroup.com www.hipl.hemrajgroup.com;

    ssl_certificate /etc/letsencrypt/live/hipl.hemrajgroup.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/hipl.hemrajgroup.com/privkey.pem;

    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    client_max_body_size 50M;

    # API endpoints
    location /api/ {
        proxy_pass http://backend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_read_timeout 300s;
        proxy_connect_timeout 75s;
    }

    # Frontend
    location / {
        proxy_pass http://frontend;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
    }

    # Gzip compression
    gzip on;
    gzip_vary on;
    gzip_types text/plain text/css text/xml text/javascript
               application/javascript application/xml+rss
               application/json application/x-javascript;
}
```

Enable the site:

```bash
sudo ln -s /etc/nginx/sites-available/hipl /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### 6. Setup SSL Certificate

```bash
sudo certbot certonly --nginx -d hipl.hemrajgroup.com -d www.hipl.hemrajgroup.com
```

### 7. Start Docker Services

```bash
cd /var/www/project-HIPL

# Production compose file
docker-compose -f docker-compose.yml -f docker-compose.prod.yml up -d

# Verify services
docker-compose ps
```

### 8. Initialize Production Database

```bash
# Execute schema
docker exec hipl_mysql mysql -u hipl_user -p<password> hipl_db < database/schema.sql

# Seed data
docker exec hipl_mysql mysql -u hipl_user -p<password> hipl_db < database/seed_data.sql
```

### 9. Configure Monitoring

#### Setup Prometheus

Create `/var/www/project-HIPL/prometheus.yml`:

```yaml
global:
  scrape_interval: 15s

scrape_configs:
  - job_name: 'backend'
    static_configs:
      - targets: ['localhost:8000']

  - job_name: 'mysql'
    static_configs:
      - targets: ['localhost:3306']

  - job_name: 'redis'
    static_configs:
      - targets: ['localhost:6379']
```

#### Setup Grafana

Access http://localhost:3000 and configure data sources.

### 10. Backup Strategy

#### Automated Daily Backups

Create `/usr/local/bin/hipl-backup.sh`:

```bash
#!/bin/bash

BACKUP_DIR="/backup/hipl"
DATE=$(date +%Y%m%d_%H%M%S)

# Create backup directory
mkdir -p $BACKUP_DIR

# Backup MySQL database
docker exec hipl_mysql mysqldump -u hipl_user -pHIPL_SecurePass2026 hipl_db | \
  gzip > $BACKUP_DIR/hipl_db_$DATE.sql.gz

# Backup application files
tar -czf $BACKUP_DIR/app_files_$DATE.tar.gz /var/www/project-HIPL

# Keep only last 30 days of backups
find $BACKUP_DIR -type f -mtime +30 -delete

echo "Backup completed: $DATE"
```

Make executable and schedule with cron:

```bash
chmod +x /usr/local/bin/hipl-backup.sh

# Add to crontab (daily at 2 AM)
0 2 * * * /usr/local/bin/hipl-backup.sh >> /var/log/hipl-backup.log 2>&1
```

### 11. Health Checks

```bash
# Check all services
docker-compose ps

# Check backend health
curl http://localhost:8000/health

# Check MySQL
docker exec hipl_mysql mysqladmin -u hipl_user -pHIPL_SecurePass2026 ping

# Check Redis
docker exec hipl_redis redis-cli ping
```

### 12. Log Management

View logs:

```bash
# Backend logs
docker-compose logs -f backend

# N8N logs
docker-compose logs -f n8n

# MySQL logs
docker-compose logs -f mysql

# All logs
docker-compose logs -f
```

---

## Troubleshooting

### Database Connection Issues

```bash
# Check MySQL status
docker-compose ps mysql

# Check MySQL logs
docker-compose logs mysql

# Verify connection
mysql -h 127.0.0.1 -u hipl_user -pHIPL_SecurePass2026 -e "SELECT 1"
```

### API Not Responding

```bash
# Check backend health
curl -v http://localhost:8000/health

# Restart backend
docker-compose restart backend

# Check logs
docker-compose logs backend
```

### N8N Workflow Issues

```bash
# Access N8N logs
docker-compose logs n8n

# Restart N8N
docker-compose restart n8n
```

### Permission Denied Errors

```bash
# Fix Docker permissions
sudo usermod -aG docker $USER
newgrp docker

# Restart Docker
sudo systemctl restart docker
```

---

## Performance Tuning

### MySQL Optimization

```sql
-- Increase max connections
SET GLOBAL max_connections = 1000;

-- Optimize query cache
SET GLOBAL query_cache_size = 0;
SET GLOBAL query_cache_type = 0;

-- Increase buffer pool size
SET GLOBAL innodb_buffer_pool_size = 4GB;
```

### Redis Optimization

```bash
# Increase max memory
redis-cli CONFIG SET maxmemory 2gb

# Set eviction policy
redis-cli CONFIG SET maxmemory-policy allkeys-lru
```

### Nginx Optimization

```nginx
# Increase worker processes
worker_processes auto;

# Increase worker connections
events {
    worker_connections 4096;
}
```

---

## Security Checklist

- [ ] Change all default passwords
- [ ] Enable HTTPS/SSL
- [ ] Configure firewall rules
- [ ] Setup rate limiting
- [ ] Enable audit logging
- [ ] Configure backup strategy
- [ ] Setup monitoring/alerting
- [ ] Enable CORS properly
- [ ] Rotate JWT secret keys regularly
- [ ] Keep dependencies updated
- [ ] Setup log rotation
- [ ] Enable database encryption

---

## Support

For deployment issues, contact:
- **Email:** support@hemrajgroup.com
- **Documentation:** /documentation folder
- **N8N Support:** https://n8n.io/support

---

**Last Updated:** June 23, 2026
**Status:** Production Ready ✅
