-- Project HIPL Database Schema
-- MySQL 8.0+
-- Created: 2026-06-23

-- ============================================
-- USERS & AUTHENTICATION
-- ============================================

CREATE TABLE IF NOT EXISTS `users` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `full_name` VARCHAR(255) NOT NULL,
  `hashed_password` VARCHAR(255) NOT NULL,
  `is_active` BOOLEAN DEFAULT TRUE,
  `is_superuser` BOOLEAN DEFAULT FALSE,
  `department_id` INT,
  `last_login` DATETIME,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX `idx_email` (`email`),
  INDEX `idx_department` (`department_id`),
  INDEX `idx_created_at` (`created_at`)
);

CREATE TABLE IF NOT EXISTS `roles` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100) UNIQUE NOT NULL,
  `description` VARCHAR(500),
  `is_active` BOOLEAN DEFAULT TRUE,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_name` (`name`)
);

CREATE TABLE IF NOT EXISTS `permissions` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100) UNIQUE NOT NULL,
  `description` VARCHAR(500),
  `module` VARCHAR(100) NOT NULL,
  `action` VARCHAR(100) NOT NULL,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_module_action` (`module`, `action`)
);

CREATE TABLE IF NOT EXISTS `user_role` (
  `user_id` INT NOT NULL,
  `role_id` INT NOT NULL,
  PRIMARY KEY (`user_id`, `role_id`),
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`role_id`) REFERENCES `roles`(`id`) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS `role_permission` (
  `role_id` INT NOT NULL,
  `permission_id` INT NOT NULL,
  PRIMARY KEY (`role_id`, `permission_id`),
  FOREIGN KEY (`role_id`) REFERENCES `roles`(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`permission_id`) REFERENCES `permissions`(`id`) ON DELETE CASCADE
);

-- ============================================
-- DEPARTMENTS & ORGANIZATION
-- ============================================

CREATE TABLE IF NOT EXISTS `departments` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(100) UNIQUE NOT NULL,
  `code` VARCHAR(50) UNIQUE NOT NULL,
  `description` TEXT,
  `manager_id` INT,
  `is_active` BOOLEAN DEFAULT TRUE,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX `idx_code` (`code`),
  INDEX `idx_manager` (`manager_id`)
);

ALTER TABLE `users` ADD FOREIGN KEY (`department_id`) REFERENCES `departments`(`id`) ON DELETE SET NULL;

-- ============================================
-- WORKFLOWS & AUTOMATION
-- ============================================

CREATE TABLE IF NOT EXISTS `workflows` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `n8n_id` VARCHAR(100) UNIQUE NOT NULL,
  `department` VARCHAR(100) NOT NULL,
  `status` VARCHAR(50) DEFAULT 'active',
  `version` INT DEFAULT 1,
  `config` JSON,
  `error_handling` VARCHAR(50) DEFAULT 'email',
  `is_monitoring` BOOLEAN DEFAULT TRUE,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX `idx_department` (`department`),
  INDEX `idx_status` (`status`)
);

CREATE TABLE IF NOT EXISTS `workflow_executions` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `workflow_id` INT NOT NULL,
  `execution_id` VARCHAR(100) UNIQUE NOT NULL,
  `status` VARCHAR(50) NOT NULL,
  `input_data` JSON,
  `output_data` JSON,
  `error_message` TEXT,
  `execution_time` INT,
  `started_at` DATETIME NOT NULL,
  `completed_at` DATETIME,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`workflow_id`) REFERENCES `workflows`(`id`) ON DELETE CASCADE,
  INDEX `idx_workflow` (`workflow_id`),
  INDEX `idx_status` (`status`),
  INDEX `idx_started_at` (`started_at`)
);

-- ============================================
-- AUDIT & LOGGING
-- ============================================

CREATE TABLE IF NOT EXISTS `audit_logs` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `user_id` INT,
  `action` VARCHAR(100) NOT NULL,
  `module` VARCHAR(100) NOT NULL,
  `resource_type` VARCHAR(100) NOT NULL,
  `resource_id` VARCHAR(100) NOT NULL,
  `changes` JSON,
  `ip_address` VARCHAR(50),
  `user_agent` TEXT,
  `timestamp` DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`user_id`) REFERENCES `users`(`id`) ON DELETE SET NULL,
  INDEX `idx_user_action` (`user_id`, `action`),
  INDEX `idx_module_resource` (`module`, `resource_type`, `resource_id`),
  INDEX `idx_timestamp` (`timestamp`)
);

-- ============================================
-- ACCOUNTING & FINANCE
-- ============================================

CREATE TABLE IF NOT EXISTS `invoices` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `invoice_number` VARCHAR(100) UNIQUE NOT NULL,
  `vendor_id` INT NOT NULL,
  `invoice_date` DATE NOT NULL,
  `due_date` DATE NOT NULL,
  `amount` DECIMAL(12, 2) NOT NULL,
  `gst_amount` DECIMAL(10, 2),
  `tds_amount` DECIMAL(10, 2),
  `status` VARCHAR(50) DEFAULT 'pending',
  `notes` TEXT,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX `idx_status` (`status`),
  INDEX `idx_invoice_date` (`invoice_date`),
  INDEX `idx_vendor` (`vendor_id`)
);

CREATE TABLE IF NOT EXISTS `payments` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `invoice_id` INT NOT NULL,
  `payment_date` DATE NOT NULL,
  `amount` DECIMAL(12, 2) NOT NULL,
  `payment_method` VARCHAR(50),
  `reference_number` VARCHAR(100),
  `status` VARCHAR(50) DEFAULT 'pending',
  `approved_by` INT,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`invoice_id`) REFERENCES `invoices`(`id`) ON DELETE CASCADE,
  FOREIGN KEY (`approved_by`) REFERENCES `users`(`id`) ON DELETE SET NULL,
  INDEX `idx_status` (`status`),
  INDEX `idx_payment_date` (`payment_date`)
);

-- ============================================
-- PROCUREMENT & VENDORS
-- ============================================

CREATE TABLE IF NOT EXISTS `vendors` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `name` VARCHAR(255) NOT NULL,
  `code` VARCHAR(100) UNIQUE NOT NULL,
  `email` VARCHAR(255),
  `phone` VARCHAR(20),
  `address` TEXT,
  `city` VARCHAR(100),
  `state` VARCHAR(100),
  `country` VARCHAR(100),
  `pin_code` VARCHAR(10),
  `gst_number` VARCHAR(50),
  `kyc_verified` BOOLEAN DEFAULT FALSE,
  `status` VARCHAR(50) DEFAULT 'active',
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX `idx_status` (`status`),
  INDEX `idx_code` (`code`)
);

CREATE TABLE IF NOT EXISTS `purchase_orders` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `po_number` VARCHAR(100) UNIQUE NOT NULL,
  `vendor_id` INT NOT NULL,
  `po_date` DATE NOT NULL,
  `expected_delivery_date` DATE NOT NULL,
  `total_amount` DECIMAL(12, 2) NOT NULL,
  `status` VARCHAR(50) DEFAULT 'draft',
  `notes` TEXT,
  `created_by` INT,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (`vendor_id`) REFERENCES `vendors`(`id`),
  FOREIGN KEY (`created_by`) REFERENCES `users`(`id`),
  INDEX `idx_status` (`status`),
  INDEX `idx_vendor` (`vendor_id`),
  INDEX `idx_po_date` (`po_date`)
);

-- ============================================
-- PRODUCTION & OPERATIONS
-- ============================================

CREATE TABLE IF NOT EXISTS `production_logs` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `machine_id` INT NOT NULL,
  `shift` VARCHAR(20),
  `start_time` DATETIME,
  `end_time` DATETIME,
  `units_produced` INT,
  `efficiency_percentage` DECIMAL(5, 2),
  `downtime_minutes` INT DEFAULT 0,
  `downtime_reason` VARCHAR(255),
  `status` VARCHAR(50) DEFAULT 'active',
  `timestamp` DATETIME DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_machine` (`machine_id`),
  INDEX `idx_timestamp` (`timestamp`),
  INDEX `idx_status` (`status`)
);

-- ============================================
-- INVENTORY & WAREHOUSE
-- ============================================

CREATE TABLE IF NOT EXISTS `products` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `code` VARCHAR(100) UNIQUE NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `description` TEXT,
  `category` VARCHAR(100),
  `unit_of_measure` VARCHAR(20),
  `reorder_level` INT DEFAULT 100,
  `reorder_quantity` INT DEFAULT 500,
  `status` VARCHAR(50) DEFAULT 'active',
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_code` (`code`),
  INDEX `idx_category` (`category`)
);

CREATE TABLE IF NOT EXISTS `inventory` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `warehouse_location` VARCHAR(100),
  `quantity` INT DEFAULT 0,
  `reserved_quantity` INT DEFAULT 0,
  `available_quantity` INT GENERATED ALWAYS AS (quantity - reserved_quantity) STORED,
  `last_updated` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (`product_id`) REFERENCES `products`(`id`),
  INDEX `idx_product` (`product_id`),
  INDEX `idx_available` (`available_quantity`)
);

CREATE TABLE IF NOT EXISTS `batch_tracking` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `product_id` INT NOT NULL,
  `batch_number` VARCHAR(100) NOT NULL,
  `expiry_date` DATE,
  `quantity` INT,
  `received_date` DATE,
  `status` VARCHAR(50) DEFAULT 'active',
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`product_id`) REFERENCES `products`(`id`),
  INDEX `idx_batch` (`batch_number`),
  INDEX `idx_expiry_date` (`expiry_date`),
  UNIQUE (`batch_number`, `product_id`)
);

CREATE TABLE IF NOT EXISTS `grn` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `grn_number` VARCHAR(100) UNIQUE NOT NULL,
  `po_id` INT NOT NULL,
  `received_quantity` INT NOT NULL,
  `received_date` DATE NOT NULL,
  `status` VARCHAR(50) DEFAULT 'pending_verification',
  `verified_by` INT,
  `notes` TEXT,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`po_id`) REFERENCES `purchase_orders`(`id`),
  FOREIGN KEY (`verified_by`) REFERENCES `users`(`id`),
  INDEX `idx_status` (`status`),
  INDEX `idx_received_date` (`received_date`)
);

-- ============================================
-- LOGISTICS & SUPPLY CHAIN
-- ============================================

CREATE TABLE IF NOT EXISTS `orders` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `order_number` VARCHAR(100) UNIQUE NOT NULL,
  `customer_id` INT NOT NULL,
  `order_date` DATE NOT NULL,
  `delivery_date` DATE,
  `total_amount` DECIMAL(12, 2) NOT NULL,
  `status` VARCHAR(50) DEFAULT 'pending',
  `notes` TEXT,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX `idx_status` (`status`),
  INDEX `idx_order_date` (`order_date`),
  INDEX `idx_customer` (`customer_id`)
);

CREATE TABLE IF NOT EXISTS `shipments` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `order_id` INT NOT NULL,
  `tracking_number` VARCHAR(100) UNIQUE NOT NULL,
  `carrier` VARCHAR(100),
  `dispatch_date` DATE,
  `expected_delivery` DATE,
  `actual_delivery` DATE,
  `status` VARCHAR(50) DEFAULT 'pending',
  `location` VARCHAR(255),
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  FOREIGN KEY (`order_id`) REFERENCES `orders`(`id`),
  INDEX `idx_status` (`status`),
  INDEX `idx_tracking` (`tracking_number`),
  INDEX `idx_dispatch_date` (`dispatch_date`)
);

-- ============================================
-- HR & ADMINISTRATION
-- ============================================

CREATE TABLE IF NOT EXISTS `employees` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `employee_code` VARCHAR(100) UNIQUE NOT NULL,
  `first_name` VARCHAR(100) NOT NULL,
  `last_name` VARCHAR(100) NOT NULL,
  `email` VARCHAR(255) UNIQUE NOT NULL,
  `phone` VARCHAR(20),
  `department_id` INT,
  `position` VARCHAR(100),
  `hire_date` DATE,
  `dob` DATE,
  `status` VARCHAR(50) DEFAULT 'active',
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`department_id`) REFERENCES `departments`(`id`),
  INDEX `idx_status` (`status`),
  INDEX `idx_employee_code` (`employee_code`)
);

CREATE TABLE IF NOT EXISTS `attendance` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `employee_id` INT NOT NULL,
  `attendance_date` DATE NOT NULL,
  `check_in_time` TIME,
  `check_out_time` TIME,
  `status` VARCHAR(50) DEFAULT 'present',
  `notes` VARCHAR(255),
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`employee_id`) REFERENCES `employees`(`id`),
  INDEX `idx_employee_date` (`employee_id`, `attendance_date`),
  UNIQUE (`employee_id`, `attendance_date`)
);

CREATE TABLE IF NOT EXISTS `leaves` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `employee_id` INT NOT NULL,
  `leave_type` VARCHAR(50),
  `start_date` DATE NOT NULL,
  `end_date` DATE NOT NULL,
  `status` VARCHAR(50) DEFAULT 'pending',
  `approved_by` INT,
  `reason` TEXT,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`employee_id`) REFERENCES `employees`(`id`),
  FOREIGN KEY (`approved_by`) REFERENCES `users`(`id`),
  INDEX `idx_status` (`status`),
  INDEX `idx_employee` (`employee_id`)
);

-- ============================================
-- QUALITY CONTROL
-- ============================================

CREATE TABLE IF NOT EXISTS `quality_checks` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `batch_id` INT NOT NULL,
  `check_type` VARCHAR(100),
  `result_value` DECIMAL(10, 4),
  `specification_min` DECIMAL(10, 4),
  `specification_max` DECIMAL(10, 4),
  `status` VARCHAR(50) DEFAULT 'passed',
  `checked_by` INT,
  `checked_at` DATETIME,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_status` (`status`),
  INDEX `idx_batch` (`batch_id`),
  INDEX `idx_checked_at` (`checked_at`)
);

CREATE TABLE IF NOT EXISTS `non_conformance` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `batch_id` INT NOT NULL,
  `issue_description` TEXT NOT NULL,
  `severity` VARCHAR(50) DEFAULT 'medium',
  `status` VARCHAR(50) DEFAULT 'open',
  `reported_by` INT,
  `root_cause` TEXT,
  `corrective_action` TEXT,
  `closed_date` DATE,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`reported_by`) REFERENCES `users`(`id`),
  INDEX `idx_status` (`status`),
  INDEX `idx_severity` (`severity`)
);

-- ============================================
-- SALES & CUSTOMERS
-- ============================================

CREATE TABLE IF NOT EXISTS `customers` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `customer_code` VARCHAR(100) UNIQUE NOT NULL,
  `name` VARCHAR(255) NOT NULL,
  `contact_person` VARCHAR(255),
  `email` VARCHAR(255),
  `phone` VARCHAR(20),
  `address` TEXT,
  `city` VARCHAR(100),
  `state` VARCHAR(100),
  `credit_limit` DECIMAL(12, 2) DEFAULT 0,
  `credit_used` DECIMAL(12, 2) DEFAULT 0,
  `status` VARCHAR(50) DEFAULT 'active',
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_status` (`status`),
  INDEX `idx_code` (`customer_code`)
);

-- ============================================
-- COMPLIANCE & LEGAL
-- ============================================

CREATE TABLE IF NOT EXISTS `compliance_filings` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `filing_type` VARCHAR(100) NOT NULL,
  `due_date` DATE NOT NULL,
  `submitted_date` DATE,
  `status` VARCHAR(50) DEFAULT 'pending',
  `reference_number` VARCHAR(100),
  `notes` TEXT,
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_status` (`status`),
  INDEX `idx_due_date` (`due_date`)
);

CREATE TABLE IF NOT EXISTS `contracts` (
  `id` INT PRIMARY KEY AUTO_INCREMENT,
  `contract_number` VARCHAR(100) UNIQUE NOT NULL,
  `vendor_id` INT,
  `contract_date` DATE,
  `expiry_date` DATE,
  `value` DECIMAL(12, 2),
  `status` VARCHAR(50) DEFAULT 'active',
  `document_path` VARCHAR(255),
  `created_at` DATETIME DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (`vendor_id`) REFERENCES `vendors`(`id`),
  INDEX `idx_status` (`status`),
  INDEX `idx_expiry_date` (`expiry_date`)
);

-- ============================================
-- DASHBOARD & REPORTING VIEWS
-- ============================================

CREATE VIEW `vw_pending_invoices` AS
SELECT 
  i.id,
  i.invoice_number,
  v.name as vendor_name,
  i.amount,
  i.status,
  DATEDIFF(i.due_date, CURDATE()) as days_until_due
FROM invoices i
JOIN vendors v ON i.vendor_id = v.id
WHERE i.status IN ('pending', 'partially_paid')
ORDER BY i.due_date ASC;

CREATE VIEW `vw_low_stock_items` AS
SELECT 
  p.id,
  p.code,
  p.name,
  i.quantity,
  p.reorder_level,
  (p.reorder_level - i.quantity) as shortage_quantity
FROM inventory i
JOIN products p ON i.product_id = p.id
WHERE i.quantity <= p.reorder_level
AND p.status = 'active';

CREATE VIEW `vw_shipment_tracking` AS
SELECT 
  s.id,
  s.tracking_number,
  o.order_number,
  s.status,
  s.dispatch_date,
  s.expected_delivery,
  DATEDIFF(s.expected_delivery, CURDATE()) as days_remaining
FROM shipments s
JOIN orders o ON s.order_id = o.id
WHERE s.status IN ('pending', 'in_transit')
ORDER BY s.expected_delivery ASC;

-- ============================================
-- CREATE INDEXES FOR PERFORMANCE
-- ============================================

CREATE INDEX idx_invoice_vendor ON invoices(vendor_id);
CREATE INDEX idx_payment_invoice ON payments(invoice_id);
CREATE INDEX idx_po_vendor ON purchase_orders(vendor_id);
CREATE INDEX idx_grn_po ON grn(po_id);
CREATE INDEX idx_shipment_order ON shipments(order_id);
CREATE INDEX idx_order_customer ON orders(customer_id);
CREATE INDEX idx_attendance_employee ON attendance(employee_id);
CREATE INDEX idx_leave_employee ON leaves(employee_id);

-- ============================================
-- SET CHARACTER SET
-- ============================================

ALTER DATABASE hipl_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
