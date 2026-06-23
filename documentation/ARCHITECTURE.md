# Project HIPL - Architecture & Design Documentation

## System Architecture Overview

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                    CLIENT LAYER                              │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           React Frontend (Port 5173)                 │  │
│  │  - Role-Based Dashboards                             │  │
│  │  - Real-time Data Visualization                      │  │
│  │  - Excel Import/Export                               │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                          ↓ (HTTP/REST API)
┌─────────────────────────────────────────────────────────────┐
│                   API GATEWAY LAYER                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │      Nginx Reverse Proxy (Port 80/443)              │  │
│  │  - Load Balancing                                    │  │
│  │  - SSL/TLS Termination                               │  │
│  │  - Request Rate Limiting                             │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────────┐
│                  APPLICATION LAYER                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │    FastAPI Backend (Port 8000)                       │  │
│  │  - Authentication & Authorization                    │  │
│  │  - Business Logic                                    │  │
│  │  - Data Validation                                   │  │
│  │  - Audit Logging                                     │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
      ↓ (DB Queries)    ↓ (Webhooks)    ↓ (API Calls)
┌─────────────────────────────────────────────────────────────┐
│                   SERVICE LAYER                              │
│  ┌──────────────────┐  ┌──────────────────┐               │
│  │  N8N Workflows   │  │  External APIs   │               │
│  │  (Port 5678)     │  │  - IoT Gateway   │               │
│  │  - 8 Workflows   │  │  - Logistics     │               │
│  │  - Real-time     │  │  - ERP Systems   │               │
│  └──────────────────┘  └──────────────────┘               │
└─────────────────────────────────────────────────────────────┘
      ↓ (SQL Queries)    ↓ (Caching)
┌─────────────────────────────────────────────────────────────┐
│                  DATA LAYER                                  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  MySQL Database 8.0 (Port 3306)                     │  │
│  │  - 25+ Tables                                        │  │
│  │  - Audit Logs                                        │  │
│  │  - Relationships & Constraints                       │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Redis Cache (Port 6379)                            │  │
│  │  - Session Management                               │  │
│  │  - Real-time Data Caching                           │  │
│  └──────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

---

## Technology Stack

### Backend
- **Framework:** FastAPI 0.104+
- **Language:** Python 3.11+
- **Database ORM:** SQLAlchemy 2.0+
- **Authentication:** JWT Tokens (PyJWT)
- **Password Hashing:** bcrypt
- **API Documentation:** Swagger/OpenAPI

### Frontend
- **Framework:** React 18+
- **State Management:** Redux/Context API
- **Styling:** Tailwind CSS
- **Charts:** Recharts, Chart.js
- **Build Tool:** Vite
- **Package Manager:** npm

### Automation & Workflows
- **Workflow Engine:** N8N (Community/Self-hosted)
- **Integrations:** MySQL, REST APIs, Webhooks
- **Scheduling:** Cron-based triggers
- **Error Handling:** Email/SMS alerts

### Database
- **DBMS:** MySQL 8.0
- **Connection Pool:** SQLAlchemy QueuePool
- **Caching:** Redis 7+
- **Backup:** Automated daily backups

### DevOps
- **Containerization:** Docker
- **Orchestration:** Docker Compose
- **Reverse Proxy:** Nginx
- **Monitoring:** Prometheus & Grafana (Optional)

---

## Database Design

### Core Tables

#### Authentication & Authorization
- `users` - User accounts and profiles
- `roles` - Role definitions
- `permissions` - Permission matrix
- `user_role` - User-role mapping
- `role_permission` - Role-permission mapping

#### Organization
- `departments` - Department master
- `employees` - Employee records

#### Workflows
- `workflows` - Workflow definitions
- `workflow_executions` - Execution logs
- `audit_logs` - System audit trail

#### Business Domains
- **Accounting:** `invoices`, `payments`
- **Procurement:** `vendors`, `purchase_orders`, `grn`
- **Production:** `production_logs`
- **Inventory:** `products`, `inventory`, `batch_tracking`
- **Logistics:** `orders`, `shipments`
- **HR:** `employees`, `attendance`, `leaves`
- **Quality:** `quality_checks`, `non_conformance`
- **Sales:** `customers`
- **Compliance:** `compliance_filings`, `contracts`

---

## API Architecture

### Endpoint Structure
```
/api/v1/
├── /auth
│   ├── POST /login
│   ├── POST /logout
│   ├── GET /me
│   └── POST /refresh-token
├── /accounting
│   ├── GET /invoices
│   ├── POST /invoices
│   ├── GET /payments
│   └── POST /reconciliation
├── /procurement
│   ├── GET /purchase-orders
│   ├── POST /purchase-orders
│   ├── GET /vendors
│   └── POST /rfq
├── /production
│   ├── GET /status
│   ├── GET /reports
│   └── POST /logs
├── /inventory
│   ├── GET /stock
│   ├── POST /grn
│   └── GET /batches
├── /logistics
│   ├── GET /shipments
│   ├── POST /dispatch
│   └── GET /tracking
├── /hr
│   ├── GET /employees
│   ├── POST /onboarding
│   ├── GET /attendance
│   └── POST /leave-request
├── /quality
│   ├── GET /checks
│   ├── POST /non-conformance
│   ├── GET /audits
│   └── POST /capa
├── /sales
│   ├── GET /orders
│   ├── POST /orders
│   ├── GET /customers
│   └── POST /credit-approval
└── /compliance
    ├── GET /filings
    ├── GET /contracts
    └── GET /audit-trails
```

---

## Security Architecture

### Authentication Flow
```
┌──────────────────────────────────────────────────────┐
│ User Credentials (Email + Password)                  │
└─────────────────────┬──────────────────────────────┘
                      ↓
┌──────────────────────────────────────────────────────┐
│ Validate Email & Verify Password (bcrypt)            │
└─────────────────────┬──────────────────────────────┘
                      ↓
┌──────────────────────────────────────────────────────┐
│ Generate JWT Token (HS256 Algorithm)                 │
│ - Payload: user_id, email, exp time                 │
│ - Signed with SECRET_KEY                             │
└─────────────────────┬──────────────────────────────┘
                      ↓
┌──────────────────────────────────────────────────────┐
│ Return Token to Client                               │
│ - Store in localStorage/sessionStorage               │
│ - Include in Authorization header                    │
└──────────────────────────────────────────────────────┘
```

### Authorization Flow
```
API Request → JWT Token Validation → User Lookup → 
Role Check → Permission Check → Execute Action → 
Audit Log → Return Response
```

### Security Features
- ✅ JWT-based stateless authentication
- ✅ Bcrypt password hashing (12 rounds)
- ✅ Role-Based Access Control (RBAC)
- ✅ Permission-level authorization
- ✅ SQL injection prevention (SQLAlchemy ORM)
- ✅ XSS protection (FastAPI headers)
- ✅ CORS configuration
- ✅ Rate limiting (1000 requests/min per user)
- ✅ Audit logging for all actions
- ✅ HTTPS/TLS support

---

## Workflow Integration Architecture

### Workflow Execution Flow
```
Trigger (Webhook/Schedule)
       ↓
Validate Input Data
       ↓
Connect to Database
       ↓
Fetch Required Data
       ↓
Process Business Logic
       ↓
Update Database
       ↓
Send Notifications
       ↓
Log Execution
       ↓
Return Response
```

### Error Handling Strategy
```
Error Occurs
       ↓
Catch Exception
       ↓
Check Error Type
       ↓
Retry? (Exponential Backoff)
       ↓
Failed After Retries?
       ↓
Log Error → Send Alert → Manual Queue → Notify Manager
```

---

## Scalability & Performance

### Database Optimization
- Connection pooling (20 connections, max 40 overflow)
- Strategic indexing on foreign keys and frequently queried columns
- Partitioning strategy for large tables (optional)
- Query optimization and prepared statements

### Caching Strategy
- Redis for session management
- API response caching (TTL: 5-30 minutes)
- Database query result caching
- Real-time cache invalidation on updates

### API Rate Limiting
- Global: 1000 requests/minute per user
- Endpoint-specific limits configurable
- Sliding window algorithm
- HTTP 429 (Too Many Requests) responses

### Load Distribution
- Nginx round-robin load balancing
- Multiple FastAPI workers (via Gunicorn)
- N8N distributed execution
- Database read replicas (future)

---

## Deployment Architecture

### Development Environment
```
Local Machine
├── Docker Desktop
│   ├── MySQL Container
│   ├── Redis Container
│   ├── N8N Container
│   ├── FastAPI Container
│   └── Nginx Container
└── Frontend Dev Server (npm run dev)
```

### Production Environment
```
Cloud/Server
├── Load Balancer (Nginx)
├── API Tier (FastAPI instances × N)
├── Application Tier (N8N workflows)
├── Data Tier
│   ├── MySQL Master (Primary)
│   ├── MySQL Slave (Read replicas)
│   └── Redis Cluster
├── Storage (Backup & Logs)
└── Monitoring (Prometheus/Grafana)
```

---

## Data Flow Diagrams

### Invoice Processing Flow
```
Invoice Receipt
    ↓
Data Extraction (N8N Workflow 01)
    ↓
Validation & Matching with PO
    ↓
Approval Workflow (Manager Review)
    ↓
Payment Processing
    ↓
Bank Reconciliation
    ↓
Compliance Reporting (GST/TDS)
    ↓
Audit Log Entry
```

### Order to Delivery Flow
```
Sales Order Created
    ↓
Credit Validation (N8N Workflow 08)
    ↓
Order Confirmation
    ↓
Production/Inventory Check
    ↓
Dispatch Planning (N8N Workflow 05)
    ↓
Shipment Creation
    ↓
Tracking Updates
    ↓
Delivery Confirmation
    ↓
Invoice Generation
```

---

## Monitoring & Observability

### Metrics Tracked
- API response times (p50, p95, p99)
- Database query performance
- Workflow execution times
- Error rates by endpoint
- User activity logs
- System resource usage (CPU, Memory, Disk)

### Alerting
- High error rate (> 5%)
- Slow API response (> 2s)
- Database connection pool exhaustion
- Workflow execution failures
- Disk space low (< 10%)
- Memory usage high (> 80%)

---

## Future Enhancements

1. **Microservices Architecture** - Split into domain-based microservices
2. **Message Queue** - RabbitMQ/Kafka for async processing
3. **GraphQL API** - Alternative to REST API
4. **Machine Learning** - Predictive analytics
5. **Mobile App** - Native iOS/Android applications
6. **Advanced Analytics** - BI dashboards with drill-down capabilities
7. **API Gateway** - Kong/AWS API Gateway
8. **Service Mesh** - Istio for advanced networking

---

**Document Version:** 1.0.0
**Last Updated:** June 23, 2026
**Author:** N8N Automation Team
