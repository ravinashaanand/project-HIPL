# User Guide - Project HIPL

## Table of Contents

1. [Getting Started](#getting-started)
2. [Login & Authentication](#login--authentication)
3. [Role-Based Access](#role-based-access)
4. [Department Dashboards](#department-dashboards)
5. [Common Tasks](#common-tasks)
6. [FAQ](#faq)

---

## Getting Started

### System Requirements

- **Browser:** Chrome, Firefox, Safari, or Edge (latest version)
- **Internet:** Stable connection (5+ Mbps)
- **Device:** Desktop, Tablet, or Mobile

### Accessing the Application

1. Open your browser
2. Navigate to: `http://hipl.hemrajgroup.com` (or configured domain)
3. You will see the Project HIPL login page

---

## Login & Authentication

### First-Time Login

1. **Enter Email:** Your corporate email address
   - Example: `finance@hemrajgroup.com`

2. **Enter Password:** Your assigned password
   - Passwords are case-sensitive
   - Minimum 8 characters

3. **Click Login**

4. You will be redirected to your departmental dashboard

### Password Reset

If you forget your password:

1. Click "Forgot Password" on login page
2. Enter your email address
3. Check your email for reset link
4. Follow instructions to set a new password

### Logout

1. Click your **Profile Icon** (top right)
2. Select **Logout**
3. Confirm logout

---

## Role-Based Access

### User Roles & Permissions

#### System Administrator
- **Access:** All modules
- **Responsibilities:**
  - User management
  - System configuration
  - Audit logs review
  - Backup & recovery

#### Finance Manager
- **Access:** Accounting, Compliance
- **Responsibilities:**
  - Invoice processing
  - Payment approvals
  - Financial reporting
  - Bank reconciliation

#### Procurement Manager
- **Access:** Procurement, Vendor Management
- **Responsibilities:**
  - Create purchase orders
  - Vendor evaluation
  - RFQ management
  - Contract negotiation

#### Production Manager
- **Access:** Production, Inventory (monitoring)
- **Responsibilities:**
  - Production planning
  - Machine monitoring
  - Shift reporting
  - Downtime management

#### Inventory Manager
- **Access:** Inventory, Warehouse
- **Responsibilities:**
  - Stock management
  - GRN processing
  - Batch tracking
  - Expiry monitoring

#### Logistics Manager
- **Access:** Logistics, Shipments
- **Responsibilities:**
  - Dispatch planning
  - Shipment tracking
  - Delivery confirmation
  - Transporter coordination

#### HR Manager
- **Access:** HR, Employees
- **Responsibilities:**
  - Employee onboarding
  - Attendance tracking
  - Leave approval
  - Payroll management

#### Quality Manager
- **Access:** Quality, Production (monitoring)
- **Responsibilities:**
  - QC inspections
  - Non-conformance reporting
  - Audit management
  - CAPA tracking

#### Sales Manager
- **Access:** Sales, Customers
- **Responsibilities:**
  - Order processing
  - Customer management
  - Sales reporting
  - Credit approvals

#### Compliance Officer
- **Access:** Compliance, Contracts
- **Responsibilities:**
  - Regulatory filing
  - Contract management
  - Policy compliance
  - Audit trails

---

## Department Dashboards

### Finance Manager Dashboard

**Key Sections:**
- **Pending Invoices** - Shows invoices awaiting payment
- **Payment Status** - Tracks payment processing
- **Financial Overview** - Monthly revenue & expenses
- **GST/TDS Tracking** - Compliance status
- **Bank Reconciliation** - Account balances

**Actions:**
1. View invoice details
2. Approve/reject payments
3. Export financial reports
4. Generate GST statements

### Procurement Manager Dashboard

**Key Sections:**
- **Purchase Orders** - Active and pending orders
- **Vendor List** - Approved vendors
- **RFQ Status** - Request for quotations
- **Order History** - Past orders
- **Vendor Performance** - Rating and metrics

**Actions:**
1. Create new purchase order
2. Manage vendor information
3. Generate RFQ
4. Track vendor performance

### Production Manager Dashboard

**Key Sections:**
- **Machine Status** - Real-time machine monitoring
- **Production Today** - Units produced
- **Downtime Alerts** - Active downtime events
- **Efficiency Metrics** - Performance KPIs
- **Shift Reports** - Daily shift summaries

**Actions:**
1. View machine details
2. Monitor production in real-time
3. Report downtime
4. Generate production reports

### Inventory Manager Dashboard

**Key Sections:**
- **Stock Levels** - Current inventory
- **Low Stock Alerts** - Items below reorder level
- **GRN Processing** - Pending goods receipts
- **Batch Tracking** - Batch details
- **Expiry Monitoring** - Items expiring soon

**Actions:**
1. Create GRN
2. Update stock levels
3. Process batch information
4. Set reorder levels

### Logistics Manager Dashboard

**Key Sections:**
- **Active Shipments** - In-transit shipments
- **Tracking Information** - Real-time GPS tracking
- **Delivery Status** - Delivery confirmations
- **Transporter Performance** - Rating metrics
- **Transit Alerts** - Delayed shipments

**Actions:**
1. Create dispatch
2. Track shipments
3. Confirm delivery
4. Manage transporters

### HR Manager Dashboard

**Key Sections:**
- **Employee Directory** - Active employees
- **Onboarding Pipeline** - New hires
- **Attendance Summary** - Daily attendance
- **Leave Requests** - Pending approvals
- **Payroll Status** - Salary processing

**Actions:**
1. Create new employee
2. Process onboarding
3. Approve leave requests
4. View attendance records

### Quality Manager Dashboard

**Key Sections:**
- **QC Results** - Quality check data
- **Non-Conformance** - Failed quality checks
- **Audits** - Audit schedules
- **CAPA Status** - Corrective actions
- **Quality Metrics** - Performance metrics

**Actions:**
1. Enter QC data
2. Create non-conformance reports
3. Assign CAPA tasks
4. Generate quality reports

### Sales Manager Dashboard

**Key Sections:**
- **Sales Orders** - Active orders
- **Customer Information** - Customer database
- **Order Status** - Order processing status
- **Sales Performance** - Monthly sales metrics
- **Credit Limits** - Customer credit status

**Actions:**
1. Create sales order
2. Manage customer information
3. Approve credit limits
4. Generate sales reports

---

## Common Tasks

### Create a Purchase Order

1. Navigate to **Procurement** → **Purchase Orders**
2. Click **+ New Purchase Order**
3. Select **Vendor** from dropdown
4. Enter **Delivery Date**
5. Add **Items**:
   - Select Product
   - Enter Quantity
   - Verify Unit Price
6. Review **Total Amount**
7. Click **Save as Draft** or **Submit**
8. System sends email notification

### Process an Invoice

1. Navigate to **Finance** → **Invoices**
2. Click on **Pending Invoice**
3. Review invoice details
4. Match with PO (if applicable)
5. Enter **Payment Terms**
6. Click **Approve**
7. System schedules payment
8. Generates payment notification

### Create a Shipment

1. Navigate to **Logistics** → **Shipments**
2. Click **+ New Shipment**
3. Select **Sales Order**
4. Choose **Carrier/Transporter**
5. Enter **Expected Delivery Date**
6. System generates **Tracking Number**
7. Click **Dispatch**
8. Customer receives tracking notification

### Report Quality Issue

1. Navigate to **Quality** → **Non-Conformance**
2. Click **+ New Report**
3. Select **Batch/Product**
4. Describe **Issue**
5. Select **Severity** (Low/Medium/High)
6. Click **Submit**
7. Triggers investigation workflow

### Onboard New Employee

1. Navigate to **HR** → **Employees**
2. Click **+ New Employee**
3. Fill in **Personal Information**
4. Select **Department & Position**
5. Set **Start Date**
6. Click **Create Onboarding Workflow**
7. System sends welcome email
8. Generates onboarding checklist

---

## FAQ

### Q: How do I reset my password?
**A:** Click "Forgot Password" on the login page and follow the email instructions.

### Q: Why am I getting "Insufficient Permissions" error?
**A:** Your role doesn't have access to this feature. Contact your System Administrator.

### Q: How do I export data to Excel?
**A:** Look for the **Export** button in list views. Click and select Excel format.

### Q: Can I access the system on mobile?
**A:** Yes, the system is fully responsive. Use any modern browser.

### Q: What if I notice a bug?
**A:** Report it to support@hemrajgroup.com with screenshot and steps to reproduce.

### Q: How do I change my profile information?
**A:** Click Profile Icon → Settings → Update your details.

### Q: Are there keyboard shortcuts?
**A:** Press `?` to view available shortcuts.

### Q: How often is data backed up?
**A:** Daily at 2 AM IST. Contact IT for recovery requests.

### Q: How do I check system status?
**A:** Visit the Status page (link in footer) or contact support.

### Q: Can I schedule reports?
**A:** Yes, use the **Schedule** option in report generation.

---

## Tips & Best Practices

### Do's ✅
- [ ] Change your password regularly
- [ ] Log out when leaving your desk
- [ ] Verify data before submitting
- [ ] Use meaningful descriptions
- [ ] Keep audit trail records
- [ ] Report issues immediately
- [ ] Attend training sessions
- [ ] Review error messages carefully

### Don'ts ❌
- [ ] Share your login credentials
- [ ] Save passwords in browser
- [ ] Use same password for other systems
- [ ] Delete important records
- [ ] Ignore system alerts
- [ ] Bypass approval workflows
- [ ] Access other users' data
- [ ] Take screenshots of sensitive data

---

## Support & Help

### Getting Help

- **Help Button:** Click `?` icon in top right
- **Email:** support@hemrajgroup.com
- **Phone:** +91-33-XXXX-XXXX (Ext: 5000)
- **Documentation:** /documentation folder
- **Video Tutorials:** Available on support portal

### Report Issues

Include in your report:
1. Date & time of issue
2. Steps to reproduce
3. Screenshot/video
4. Your role/department
5. Expected vs actual behavior

---

**Version:** 1.0.0
**Last Updated:** June 23, 2026
**Support Email:** support@hemrajgroup.com
