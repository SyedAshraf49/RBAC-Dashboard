CREATE DATABASE IF NOT EXISTS reminder_dashboard
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE reminder_dashboard;

CREATE TABLE IF NOT EXISTS contractor_list (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sno VARCHAR(50),
    efile VARCHAR(255),
    contractor TEXT,
    description TEXT,
    value VARCHAR(255),
    start_date DATE,
    end_date DATE,
    duration VARCHAR(255),
    file_name VARCHAR(255),
    file_base64 LONGTEXT,
    file_type VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS bill_tracker (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sno VARCHAR(50),
    efile VARCHAR(255),
    contractor TEXT,
    approved_date DATE,
    approved_amount VARCHAR(255),
    bill_frequency VARCHAR(50),
    bill_date DATE,
    bill_due_date DATE,
    bill_paid_date DATE,
    paid_amount VARCHAR(255),
    file_name VARCHAR(255),
    file_base64 LONGTEXT,
    file_type VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

CREATE TABLE IF NOT EXISTS epbg (
    id INT AUTO_INCREMENT PRIMARY KEY,
    sno VARCHAR(50),
    contractor TEXT,
    po_no VARCHAR(255),
    bg_no VARCHAR(255),
    bg_date DATE,
    bg_amount VARCHAR(255),
    bg_validity VARCHAR(255),
    gem_bid_no VARCHAR(255),
    ref_efile_no VARCHAR(255),
    file_name VARCHAR(255),
    file_base64 LONGTEXT,
    file_type VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE=InnoDB
DEFAULT CHARSET=utf8mb4
COLLATE=utf8mb4_unicode_ci;

SHOW TABLES;

SELECT * FROM contractor_list;
SELECT * FROM bill_tracker;
SELECT * FROM epbg;