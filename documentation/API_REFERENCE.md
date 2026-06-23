# API Reference - Project HIPL

## Base URL
```
http://localhost:8000/api/v1
```

## Authentication

All endpoints (except login) require a JWT token in the Authorization header:

```
Authorization: Bearer <your_jwt_token>
```

---

## Authentication Endpoints

### Login
**POST** `/auth/login`

Authenticate user and receive JWT token.

**Request Body:**
```json
{
  "email": "finance@hemrajgroup.com",
  "password": "Finance@HIPL2026"
}
```

**Response (200):**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer",
  "user": {
    "id": 1,
    "email": "finance@hemrajgroup.com",
    "full_name": "Finance Manager",
    "is_active": true,
    "roles": ["Finance Manager"]
  }
}
```

**Error (401):**
```json
{
  "detail": "Invalid email or password"
}
```

---

### Get Current User
**GET** `/auth/me`

Get currently authenticated user information.

**Response (200):**
```json
{
  "id": 1,
  "email": "finance@hemrajgroup.com",
  "full_name": "Finance Manager",
  "is_active": true,
  "last_login": "2026-06-23T10:30:00",
  "roles": ["Finance Manager"],
  "department": "Finance"
}
```

---

### Logout
**POST** `/auth/logout`

Logout current user (invalidate token client-side).

**Response (200):**
```json
{
  "message": "Successfully logged out"
}
```

---

## Accounting Endpoints

### Get Invoices
**GET** `/accounting/invoices`

Retrieve all invoices (Finance Manager only).

**Query Parameters:**
- `status` (optional): pending, processed, paid
- `vendor_id` (optional): Filter by vendor
- `start_date` (optional): YYYY-MM-DD
- `end_date` (optional): YYYY-MM-DD

**Response (200):**
```json
{
  "invoices": [
    {
      "id": 1,
      "invoice_number": "INV-2026-001",
      "vendor_id": 1,
      "amount": 50000,
      "gst_amount": 9000,
      "status": "pending",
      "created_at": "2026-06-20T10:00:00"
    }
  ],
  "total": 1,
  "page": 1
}
```

---

### Create Invoice
**POST** `/accounting/invoices`

Create new invoice.

**Request Body:**
```json
{
  "invoice_number": "INV-2026-002",
  "vendor_id": 1,
  "invoice_date": "2026-06-22",
  "due_date": "2026-07-22",
  "amount": 75000,
  "gst_amount": 13500,
  "notes": "Payment terms: Net 30"
}
```

**Response (201):**
```json
{
  "id": 2,
  "invoice_number": "INV-2026-002",
  "status": "pending",
  "message": "Invoice created successfully"
}
```

---

### Get Payments
**GET** `/accounting/payments`

Retrieve payment records.

**Response (200):**
```json
{
  "payments": [
    {
      "id": 1,
      "invoice_id": 1,
      "payment_date": "2026-06-23",
      "amount": 50000,
      "status": "completed",
      "approved_by": "admin@hemrajgroup.com"
    }
  ]
}
```

---

## Procurement Endpoints

### Get Purchase Orders
**GET** `/procurement/purchase-orders`

Retrieve all purchase orders.

**Query Parameters:**
- `status` (optional): draft, submitted, approved, received
- `vendor_id` (optional): Filter by vendor

**Response (200):**
```json
{
  "purchase_orders": [
    {
      "id": 1,
      "po_number": "PO-2026-001",
      "vendor_id": 1,
      "total_amount": 100000,
      "status": "approved",
      "po_date": "2026-06-20"
    }
  ]
}
```

---

### Create Purchase Order
**POST** `/procurement/purchase-orders`

Create new purchase order.

**Request Body:**
```json
{
  "vendor_id": 1,
  "po_date": "2026-06-23",
  "expected_delivery_date": "2026-07-05",
  "items": [
    {
      "product_id": 1,
      "quantity": 500,
      "unit_price": 100
    }
  ]
}
```

**Response (201):**
```json
{
  "id": 2,
  "po_number": "PO-2026-002",
  "total_amount": 50000,
  "status": "draft"
}
```

---

### Get Vendors
**GET** `/procurement/vendors`

Retrieve vendor information.

**Response (200):**
```json
{
  "vendors": [
    {
      "id": 1,
      "name": "Local Rice Supplier",
      "code": "VEN-001",
      "email": "supplier@local.com",
      "status": "active"
    }
  ]
}
```

---

## Production Endpoints

### Get Production Status
**GET** `/production/status`

Get real-time production status.

**Response (200):**
```json
{
  "machines": [
    {
      "id": 1,
      "name": "Machine A",
      "status": "running",
      "efficiency": 95.5,
      "downtime_minutes": 0,
      "units_produced": 1500
    }
  ],
  "total_efficiency": 94.2,
  "total_downtime": 45
}
```

---

### Get Production Reports
**GET** `/production/reports`

Get production reports by shift/date.

**Query Parameters:**
- `report_date` (optional): YYYY-MM-DD
- `shift` (optional): morning, afternoon, night

**Response (200):**
```json
{
  "reports": [
    {
      "date": "2026-06-23",
      "shift": "morning",
      "units_produced": 5000,
      "efficiency": 96.2,
      "downtime_minutes": 15
    }
  ]
}
```

---

## Inventory Endpoints

### Get Stock Levels
**GET** `/inventory/stock`

Retrieve current stock levels.

**Query Parameters:**
- `product_id` (optional)
- `low_stock` (optional): true/false (show only low stock items)

**Response (200):**
```json
{
  "inventory": [
    {
      "product_id": 1,
      "product_name": "Parboiled Rice",
      "quantity": 2500,
      "reorder_level": 1000,
      "available": 2300,
      "reserved": 200
    }
  ]
}
```

---

### Create GRN
**POST** `/inventory/grn`

Create Goods Receipt Note.

**Request Body:**
```json
{
  "po_id": 1,
  "received_quantity": 500,
  "product_id": 1,
  "batch_number": "BATCH-2026-001",
  "expiry_date": "2027-06-23"
}
```

**Response (201):**
```json
{
  "grn_id": 1,
  "grn_number": "GRN-2026-001",
  "status": "pending_verification"
}
```

---

## Logistics Endpoints

### Get Shipments
**GET** `/logistics/shipments`

Retrieve shipment information.

**Query Parameters:**
- `status` (optional): pending, in_transit, delivered

**Response (200):**
```json
{
  "shipments": [
    {
      "id": 1,
      "tracking_number": "HIPL20260623000001",
      "order_id": 1,
      "status": "in_transit",
      "dispatch_date": "2026-06-23",
      "expected_delivery": "2026-06-27"
    }
  ]
}
```

---

### Create Dispatch
**POST** `/logistics/dispatch`

Create new dispatch/shipment.

**Request Body:**
```json
{
  "order_id": 1,
  "carrier": "Delhivery",
  "expected_delivery": "2026-06-27"
}
```

**Response (201):**
```json
{
  "shipment_id": 1,
  "tracking_number": "HIPL20260623000001",
  "status": "dispatched"
}
```

---

### Get Tracking
**GET** `/logistics/tracking/{tracking_number}`

Get real-time tracking information.

**Response (200):**
```json
{
  "tracking_number": "HIPL20260623000001",
  "status": "in_transit",
  "current_location": "Delhi Distribution Center",
  "events": [
    {
      "timestamp": "2026-06-24T10:30:00",
      "status": "dispatched",
      "location": "Kolkata"
    }
  ]
}
```

---

## HR Endpoints

### Get Employees
**GET** `/hr/employees`

Retrieve employee information.

**Query Parameters:**
- `department_id` (optional)
- `status` (optional): active, inactive, on_leave

**Response (200):**
```json
{
  "employees": [
    {
      "id": 1,
      "employee_code": "EMP-001",
      "first_name": "Rajesh",
      "last_name": "Kumar",
      "email": "rajesh@hemrajgroup.com",
      "department": "Finance",
      "position": "Finance Manager",
      "status": "active"
    }
  ]
}
```

---

### Create Onboarding
**POST** `/hr/onboarding`

Create employee onboarding workflow.

**Request Body:**
```json
{
  "first_name": "Neha",
  "last_name": "Sharma",
  "email": "neha@hemrajgroup.com",
  "department_id": 1,
  "position": "Accountant"
}
```

**Response (201):**
```json
{
  "employee_id": 11,
  "employee_code": "EMP-011",
  "status": "onboarding_initiated"
}
```

---

## Quality Endpoints

### Get Quality Checks
**GET** `/quality/checks`

Retrieve quality control checks.

**Response (200):**
```json
{
  "checks": [
    {
      "id": 1,
      "batch_id": 1,
      "check_type": "Moisture Content",
      "result_value": 12.5,
      "specification_min": 10,
      "specification_max": 15,
      "status": "passed",
      "checked_at": "2026-06-23T10:00:00"
    }
  ]
}
```

---

### Create Non-Conformance
**POST** `/quality/non-conformance`

Report quality issue.

**Request Body:**
```json
{
  "batch_id": 1,
  "issue_description": "Excess moisture detected",
  "severity": "high"
}
```

**Response (201):**
```json
{
  "id": 1,
  "status": "open",
  "message": "Non-conformance report created"
}
```

---

## Sales Endpoints

### Get Orders
**GET** `/sales/orders`

Retrieve sales orders.

**Query Parameters:**
- `status` (optional): pending, confirmed, shipped, delivered
- `customer_id` (optional)

**Response (200):**
```json
{
  "orders": [
    {
      "id": 1,
      "order_number": "ORD-2026-001",
      "customer_id": 1,
      "order_date": "2026-06-20",
      "total_amount": 100000,
      "status": "confirmed"
    }
  ]
}
```

---

### Create Order
**POST** `/sales/orders`

Create new sales order.

**Request Body:**
```json
{
  "customer_id": 1,
  "order_date": "2026-06-23",
  "delivery_date": "2026-06-30",
  "items": [
    {
      "product_id": 1,
      "quantity": 100,
      "unit_price": 500
    }
  ]
}
```

**Response (201):**
```json
{
  "id": 2,
  "order_number": "ORD-2026-002",
  "status": "confirmed",
  "total_amount": 50000
}
```

---

## Error Responses

All error responses follow this format:

**400 Bad Request:**
```json
{
  "detail": "Validation error message"
}
```

**401 Unauthorized:**
```json
{
  "detail": "Invalid authentication token"
}
```

**403 Forbidden:**
```json
{
  "detail": "Insufficient permissions for this operation"
}
```

**404 Not Found:**
```json
{
  "detail": "Resource not found"
}
```

**500 Internal Server Error:**
```json
{
  "detail": "Internal server error",
  "path": "/api/v1/endpoint"
}
```

---

## Status Codes

- `200 OK` - Successful GET request
- `201 Created` - Successful POST request
- `204 No Content` - Successful DELETE request
- `400 Bad Request` - Invalid input
- `401 Unauthorized` - Missing/invalid token
- `403 Forbidden` - Insufficient permissions
- `404 Not Found` - Resource not found
- `429 Too Many Requests` - Rate limit exceeded
- `500 Internal Server Error` - Server error

---

## Rate Limiting

- **Limit:** 1000 requests per minute per user
- **Response Header:** `X-RateLimit-Remaining`
- **Exceeding limit:** Returns `429 Too Many Requests`

---

## Pagination

All list endpoints support pagination:

**Query Parameters:**
- `page` (optional, default: 1)
- `per_page` (optional, default: 30, max: 100)

**Response:**
```json
{
  "data": [...],
  "total": 100,
  "page": 1,
  "per_page": 30,
  "total_pages": 4
}
```

---

## Testing with cURL

### Login
```bash
curl -X POST http://localhost:8000/api/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"finance@hemrajgroup.com","password":"Finance@HIPL2026"}'
```

### Get Invoices
```bash
curl -X GET http://localhost:8000/api/v1/accounting/invoices \
  -H "Authorization: Bearer <token>"
```

### Create Invoice
```bash
curl -X POST http://localhost:8000/api/v1/accounting/invoices \
  -H "Authorization: Bearer <token>" \
  -H "Content-Type: application/json" \
  -d '{"invoice_number":"INV-2026-002","vendor_id":1,"amount":75000}'
```

---

**API Version:** 1.0.0
**Last Updated:** June 23, 2026
