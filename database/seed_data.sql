-- Seed data for Project HIPL
-- This file populates initial data for testing and demonstration

-- Insert Roles
INSERT INTO roles (name, description) VALUES
('System Administrator', 'Full system access and configuration'),
('Finance Manager', 'Financial operations and reporting'),
('Procurement Manager', 'Procurement and vendor management'),
('Production Manager', 'Production planning and monitoring'),
('Inventory Manager', 'Inventory and warehouse management'),
('Logistics Manager', 'Logistics and shipment management'),
('HR Manager', 'Human resources and administration'),
('Quality Manager', 'Quality control and assurance'),
('Sales Manager', 'Sales and customer management'),
('Compliance Officer', 'Compliance and legal matters');

-- Insert Departments
INSERT INTO departments (name, code, description) VALUES
('Finance', 'FIN', 'Accounting & Finance Department'),
('Procurement', 'PROC', 'Procurement & Vendor Management'),
('Production', 'PROD', 'Production & Operations'),
('Inventory', 'INV', 'Inventory & Warehouse Management'),
('Logistics', 'LOG', 'Logistics & Supply Chain'),
('HR', 'HR', 'Human Resources & Administration'),
('Quality', 'QA', 'Quality Control & Assurance'),
('Sales', 'SAL', 'Sales & Customer Management'),
('Compliance', 'COMP', 'Compliance & Legal');

-- Insert Products (Sample)
INSERT INTO products (code, name, description, category, unit_of_measure, reorder_level, reorder_quantity) VALUES
('RICE-001', 'Parboiled Rice', 'Premium quality parboiled rice', 'Rice', 'kg', 1000, 5000),
('RICE-002', 'White Rice', 'Regular white rice', 'Rice', 'kg', 800, 4000),
('OIL-001', 'Rice Bran Oil', 'Refined rice bran oil', 'Oil', 'liter', 500, 2000),
('EXTRACT-001', 'De-oiled Rice Bran', 'High quality DORB', 'Extraction', 'kg', 2000, 10000);

-- Insert Vendors (Sample)
INSERT INTO vendors (name, code, email, phone, city, state, gst_number, kyc_verified, status) VALUES
('Local Rice Supplier', 'VEN-001', 'supplier1@local.com', '+91-9999999999', 'Kolkata', 'West Bengal', '19AABCT1234A1Z5', TRUE, 'active'),
('National Logistics', 'VEN-002', 'logistics@national.com', '+91-8888888888', 'Delhi', 'Delhi', '07AABCT5678B1Z9', TRUE, 'active'),
('Quality Materials Ltd', 'VEN-003', 'quality@materials.com', '+91-7777777777', 'Chennai', 'Tamil Nadu', '33AABCT9999C1Z2', TRUE, 'active');

-- Insert Customers (Sample)
INSERT INTO customers (customer_code, name, contact_person, email, city, state, credit_limit, status) VALUES
('CUST-001', 'ABC Retail Chain', 'John Doe', 'john@abcretail.com', 'Mumbai', 'Maharashtra', 500000, 'active'),
('CUST-002', 'XYZ Distributors', 'Jane Smith', 'jane@xyzdist.com', 'Bangalore', 'Karnataka', 750000, 'active'),
('CUST-003', 'Global Foods Export', 'Robert Brown', 'robert@globalfoods.com', 'Cochin', 'Kerala', 1000000, 'active');

-- Insert Employees (Sample)
INSERT INTO employees (employee_code, first_name, last_name, email, phone, department_id, position, hire_date, status) VALUES
('EMP-001', 'Rajesh', 'Kumar', 'rajesh@hemrajgroup.com', '+91-9000000001', 1, 'Finance Manager', '2020-01-15', 'active'),
('EMP-002', 'Priya', 'Singh', 'priya@hemrajgroup.com', '+91-9000000002', 2, 'Procurement Manager', '2019-06-20', 'active'),
('EMP-003', 'Amit', 'Verma', 'amit@hemrajgroup.com', '+91-9000000003', 3, 'Production Manager', '2021-03-10', 'active'),
('EMP-004', 'Deepak', 'Patel', 'deepak@hemrajgroup.com', '+91-9000000004', 4, 'Warehouse Manager', '2020-09-25', 'active');

-- Insert Workflows
INSERT INTO workflows (name, description, n8n_id, department, status, is_monitoring) VALUES
('Accounting Automation', 'Invoice processing and payment workflows', 'wf-001-accounting', 'Accounting & Finance', 'active', TRUE),
('Procurement Automation', 'Purchase order and vendor management', 'wf-002-procurement', 'Procurement & Vendor Management', 'active', TRUE),
('Production Automation', 'Real-time production monitoring', 'wf-003-production', 'Production & Operations', 'active', TRUE),
('Inventory Automation', 'Stock tracking and GRN processing', 'wf-004-inventory', 'Inventory & Warehouse Management', 'active', TRUE),
('Logistics Automation', 'Shipment tracking and dispatch', 'wf-005-logistics', 'Logistics & Supply Chain', 'active', TRUE),
('HR Automation', 'Employee onboarding and management', 'wf-006-hr', 'HR & Administration', 'active', TRUE),
('Quality Control Automation', 'QC data capture and reporting', 'wf-007-quality', 'Quality Control & Assurance', 'active', TRUE),
('Sales Automation', 'Order processing and CRM integration', 'wf-008-sales', 'Sales & Customer Management', 'active', TRUE);
