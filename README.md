# Project HIPL - N8N Enterprise Automation Solution
## Hemraj Group - Manufacturing & Logistics Automation Platform

---

## 📋 Project Overview

**Project HIPL** is an enterprise-grade automation solution designed for Hemraj Group's manufacturing operations across multiple locations (India, Vietnam, Nigeria). The platform integrates N8N workflow automation, FastAPI backend, modern React frontend, and comprehensive database management to automate 12+ critical business departments.

### Core Objective
Enable seamless automation across Accounting, Procurement, Production, Inventory, Logistics, HR, Quality Control, Sales, Compliance, and Management Reporting with role-based access and real-time monitoring.

---

## 🏢 Company Profile

**Hemraj Group** - Eastern India's largest rice processor with:
- 65+ years legacy
- USD 200M turnover (FY 2021-22)
- Global operations in India, Vietnam, Nigeria
- ISO 9001:2015, ISO 22000:2005, ISO 45001:2018 certified
- Highest exporter of de-oiled rice-bran extraction for 7 consecutive years

---

## 🏗️ Project Architecture

```
project-HIPL/
├── backend/                          # FastAPI Backend
│   ├── app/
│   │   ├── main.py
│   │   ├── config.py
│   │   ├── dependencies.py
│   │   ├── models/
│   │   ├── schemas/
│   │   ├── crud/
│   │   ├── api/
│   │   ├── services/
│   │   └── middleware/
│   ├── database/
│   │   ├── database.py
│   │   ├── schemas/
│   │   └── migrations/
│   ├── requirements.txt
│   └── .env.example
│
├── frontend/                         # React Frontend
│   ├── public/
│   ├── src/
│   │   ├── components/
│   │   ├── pages/
│   │   ├── services/
│   │   ├── utils/
│   │   ├── styles/
│   │   └── App.jsx
│   ├── package.json
│   └── .env.example
│
├── n8n-workflows/                    # N8N Automation Workflows
│   ├── 01_accounting_automation.json
│   ├── 02_procurement_automation.json
│   ├── 03_production_automation.json
│   ├── 04_inventory_automation.json
│   ├── 05_logistics_automation.json
│   ├── 06_hr_automation.json
│   ├── 07_quality_control_automation.json
│   ├── 08_sales_automation.json
│   └── workflows_documentation.md
│
├── database/                         # Database Configuration
│   ├── schema.sql
│   ├── seed_data.sql
│   ├── migrations/
│   └── backup/
│
├── documentation/                    # Comprehensive Documentation
│   ├── ARCHITECTURE.md
│   ├── WORKFLOW_DOCUMENTATION.md
│   ├── API_REFERENCE.md
│   ├── DEPLOYMENT_GUIDE.md
│   └── USER_GUIDE.md
│
├── docker-compose.yml                # Docker Configuration
├── .env.example                      # Environment Variables Template
├── LICENSE
└── README.md                         # This file
```

---

## 👥 User Roles & Access Control

### 1. **System Administrator**
- **Email:** admin@hemrajgroup.com
- **Password:** Admin@HIPL2026
- **Permissions:** Full system access, user management, audit logs

### 2. **Finance Manager**
- **Email:** finance@hemrajgroup.com
- **Password:** Finance@HIPL2026
- **Departments:** Accounting & Finance
- **Responsibilities:**
  - Invoice processing & approval
  - Payment workflows
  - Bank reconciliation
  - GST/TDS compliance
  - Financial MIS & reporting

### 3. **Procurement Manager**
- **Email:** procurement@hemrajgroup.com
- **Password:** Procurement@HIPL2026
- **Departments:** Procurement & Vendor Management
- **Responsibilities:**
  - Purchase requisitions
  - Vendor onboarding
  - RFQ management
  - Purchase order tracking
  - Vendor communication

### 4. **Production Manager**
- **Email:** production@hemrajgroup.com
- **Password:** Production@HIPL2026
- **Departments:** Production & Operations
- **Responsibilities:**
  - Production reporting
  - Machine monitoring
  - Downtime alerts
  - Production planning
  - Efficiency tracking

### 5. **Inventory Manager**
- **Email:** inventory@hemrajgroup.com
- **Password:** Inventory@HIPL2026
- **Departments:** Inventory & Warehouse Management
- **Responsibilities:**
  - Stock tracking
  - GRN automation
  - Stock reconciliation
  - Batch tracking
  - Expiry monitoring

### 6. **Logistics Manager**
- **Email:** logistics@hemrajgroup.com
- **Password:** Logistics@HIPL2026
- **Departments:** Logistics & Supply Chain
- **Responsibilities:**
  - Dispatch planning
  - Shipment tracking
  - Delivery confirmations
  - Transporter coordination
  - Documentation management

### 7. **HR Manager**
- **Email:** hr@hemrajgroup.com
- **Password:** HR@HIPL2026
- **Departments:** HR & Administration
- **Responsibilities:**
  - Employee onboarding/exit
  - Attendance & leave
  - Payroll processing
  - Compliance tracking
  - Internal communications

### 8. **Quality Manager**
- **Email:** quality@hemrajgroup.com
- **Password:** Quality@HIPL2026
- **Departments:** Quality Control & Assurance
- **Responsibilities:**
  - QC data capture
  - Non-conformance reporting
  - Audit workflows
  - CAPA management

### 9. **Sales Manager**
- **Email:** sales@hemrajgroup.com
- **Password:** Sales@HIPL2026
- **Departments:** Sales & Customer Management
- **Responsibilities:**
  - Order processing
  - CRM management
  - Customer communication
  - Sales reporting
  - Credit approvals

### 10. **Compliance Officer**
- **Email:** compliance@hemrajgroup.com
- **Password:** Compliance@HIPL2026
- **Departments:** Compliance & Legal
- **Responsibilities:**
  - Regulatory filing
  - Contract management
  - Audit trails
  - Policy monitoring

---

## 🔐 Login Credentials Summary

| Role | Email | Password | Dashboard Focus |
|------|-------|----------|------------------|
| Admin | admin@hemrajgroup.com | Admin@HIPL2026 | System Control |
| Finance | finance@hemrajgroup.com | Finance@HIPL2026 | Financial Dashboard |
| Procurement | procurement@hemrajgroup.com | Procurement@HIPL2026 | Procurement Dashboard |
| Production | production@hemrajgroup.com | Production@HIPL2026 | Production Dashboard |
| Inventory | inventory@hemrajgroup.com | Inventory@HIPL2026 | Inventory Dashboard |
| Logistics | logistics@hemrajgroup.com | Logistics@HIPL2026 | Logistics Dashboard |
| HR | hr@hemrajgroup.com | HR@HIPL2026 | HR Dashboard |
| Quality | quality@hemrajgroup.com | Quality@HIPL2026 | Quality Dashboard |
| Sales | sales@hemrajgroup.com | Sales@HIPL2026 | Sales Dashboard |
| Compliance | compliance@hemrajgroup.com | Compliance@HIPL2026 | Compliance Dashboard |

---

## 🚀 Quick Start Guide

### Prerequisites
- Docker & Docker Compose
- Node.js 18+
- Python 3.9+
- MySQL 8.0+
- N8N (Community or Self-hosted)

### Installation Steps

```bash
# 1. Clone the repository
git clone https://github.com/ravinashaanand/project-HIPL.git
cd project-HIPL

# 2. Setup environment variables
cp .env.example .env
# Edit .env with your configuration

# 3. Start Docker services
docker-compose up -d

# 4. Install backend dependencies
cd backend
pip install -r requirements.txt

# 5. Initialize database
python -m alembic upgrade head

# 6. Start backend server
uvicorn app.main:app --reload --port 8000

# 7. Install frontend dependencies
cd ../frontend
npm install

# 8. Start frontend development server
npm run dev

# 9. Access the application
# Frontend: http://localhost:5173
# Backend API: http://localhost:8000
# API Docs: http://localhost:8000/docs
# N8N: http://localhost:5678
```

---

## 📊 Dashboard Features by Role

### Finance Manager Dashboard
- Real-time invoice tracking
- Payment approval workflows
- Bank reconciliation status
- GST/TDS compliance reporting
- Financial MIS & P&L statements
- Expense management
- Vendor payment schedules

### Procurement Manager Dashboard
- Active purchase requisitions
- Vendor performance metrics
- RFQ status tracking
- Purchase order management
- Auto-reorder triggers
- Contract pricing management
- Vendor communication logs

### Production Manager Dashboard
- Real-time production status
- Machine performance metrics
- Downtime alerts & escalation
- Production planning calendar
- Efficiency KPIs
- Shift-wise reporting
- IoT device monitoring

### Inventory Manager Dashboard
- Stock levels & movements
- Low stock alerts
- GRN processing
- Batch tracking
- Expiry monitoring
- Warehouse utilization
- Stock reconciliation reports

### Logistics Manager Dashboard
- Dispatch schedules
- Shipment tracking (real-time)
- Delivery confirmations
- Transporter performance
- E-way bill automation
- Route optimization
- Transit alerts

### HR Manager Dashboard
- Onboarding/Exit workflows
- Attendance & leave tracking
- Payroll status
- Compliance document tracking
- Employee communications
- Org structure overview

### Quality Manager Dashboard
- QC data capture forms
- Non-conformance tracking
- Audit schedules
- CAPA workflows
- Quality metrics
- Compliance status

### Sales Manager Dashboard
- Order processing pipeline
- CRM customer tracking
- Sales performance metrics
- Customer communications
- Credit limit approvals
- Sales forecasting

### Compliance Officer Dashboard
- Regulatory filing calendar
- Contract lifecycle status
- Audit trails
- Policy compliance monitoring
- Document management
- Compliance alerts

---

## 🔄 N8N Workflows Included

1. **Accounting Automation** - Invoice processing, payment workflows, reconciliation
2. **Procurement Automation** - RFQ, PO creation, vendor management
3. **Production Automation** - Real-time monitoring, downtime alerts, planning
4. **Inventory Automation** - Stock tracking, GRN, batch management
5. **Logistics Automation** - Dispatch, shipment tracking, documentation
6. **HR Automation** - Onboarding, attendance, payroll input
7. **Quality Control Automation** - QC data capture, CAPA, audit tracking
8. **Sales Automation** - Order processing, CRM integration, customer notifications

---

## 🗄️ Database Overview

### Key Tables
- **users** - User authentication & role management
- **departments** - Department master
- **workflows** - N8N workflow tracking
- **invoices** - Financial transactions
- **purchase_orders** - Procurement data
- **production_logs** - Manufacturing data
- **inventory** - Stock management
- **shipments** - Logistics tracking
- **employees** - HR data
- **quality_checks** - QC records
- **orders** - Sales orders
- **audit_logs** - System audit trails

---

## 🔌 API Endpoints

### Authentication
```
POST /api/v1/auth/login
POST /api/v1/auth/logout
POST /api/v1/auth/refresh-token
GET /api/v1/auth/me
```

### Accounting
```
GET /api/v1/accounting/invoices
POST /api/v1/accounting/invoices
PUT /api/v1/accounting/invoices/{id}
GET /api/v1/accounting/payments
```

### Procurement
```
GET /api/v1/procurement/purchase-orders
POST /api/v1/procurement/purchase-orders
GET /api/v1/procurement/vendors
POST /api/v1/procurement/rfq
```

### Production
```
GET /api/v1/production/status
GET /api/v1/production/reports
POST /api/v1/production/logs
GET /api/v1/production/iot-devices
```

### Inventory
```
GET /api/v1/inventory/stock
PUT /api/v1/inventory/stock
POST /api/v1/inventory/grn
GET /api/v1/inventory/batches
```

### Logistics
```
GET /api/v1/logistics/shipments
POST /api/v1/logistics/dispatch
GET /api/v1/logistics/tracking
POST /api/v1/logistics/delivery-confirmation
```

### HR
```
GET /api/v1/hr/employees
POST /api/v1/hr/onboarding
GET /api/v1/hr/attendance
POST /api/v1/hr/leave-request
```

### Quality
```
GET /api/v1/quality/checks
POST /api/v1/quality/non-conformance
GET /api/v1/quality/audits
POST /api/v1/quality/capa
```

### Sales
```
GET /api/v1/sales/orders
POST /api/v1/sales/orders
GET /api/v1/sales/customers
POST /api/v1/sales/credit-approval
```

---

## 🛡️ Security Features

✅ Role-Based Access Control (RBAC)
✅ JWT Token Authentication
✅ Encrypted password storage (bcrypt)
✅ Audit logging for all transactions
✅ Rate limiting on API endpoints
✅ CORS security headers
✅ SQL injection prevention
✅ XSS protection
✅ CSRF tokens
✅ Compliance tracking

---

## 📈 Performance & Scalability

- **Load Balancing:** Nginx reverse proxy
- **Caching:** Redis for session & data caching
- **Database:** MySQL with optimized indexing
- **API Rate Limiting:** 1000 requests/minute per user
- **Workflow Scaling:** N8N distributed execution
- **Real-time Updates:** WebSocket integration
- **Monitoring:** Prometheus & Grafana

---

## 🔍 Real-time Monitoring

- **Workflow Status Dashboard:** Monitor all N8N workflows in real-time
- **System Health:** CPU, memory, disk usage metrics
- **Database Performance:** Query execution times, connection pool stats
- **API Response Times:** Endpoint latency tracking
- **User Activity Logs:** Track all user actions with timestamps
- **Alerts & Notifications:** Email/SMS alerts for critical issues

---

## 📞 Support & Contact

**Project Lead:** N8N Automation Specialist
**Company:** Hemraj Group
**Location:** Kolkata, Park Street
**Email:** support@hemrajgroup.com

---

## 📄 License

Proprietary - Hemraj Group
All rights reserved.

---

**Last Updated:** June 23, 2026
**Maintained By:** N8N Automation Team
**Status:** ✅ Active & Production Ready
