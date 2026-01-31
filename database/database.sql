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
                    gst VARCHAR(20),
                    start_date DATE,
                    end_date DATE,
                    duration VARCHAR(255),
                    file_name VARCHAR(255),
                    file_base64 LONGTEXT,
                    file_type VARCHAR(100),
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

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
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

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
                    bg_no_attachment_name VARCHAR(255) AFTER file_type;
                    bg_no_attachment_base64 LONGTEXT AFTER bg_no_attachment_name;
                    bg_no_attachment_type VARCHAR(100) AFTER bg_no_attachment_base64;
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

-- Users table for authentication
                CREATE TABLE IF NOT EXISTS users (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(50) UNIQUE NOT NULL,
                    email VARCHAR(100) UNIQUE NOT NULL,
                    password VARCHAR(255) NOT NULL,
                    name VARCHAR(100) NOT NULL,
                    role ENUM('admin', 'user', 'staff') NOT NULL DEFAULT 'user',
                    theme_preference VARCHAR(10) DEFAULT 'light',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci

-- Insert default users with email support
INSERT INTO users (username, email, password, name, role) VALUES
('admin1', 'admin1@company.com', 'Admin@123', 'Admin One', 'admin'),
('admin2', 'admin2@company.com', 'Admin@456', 'Admin Two', 'admin'),
('user1', 'user1@company.com', 'User@123', 'User One', 'user'),
('user2', 'user2@company.com', 'User@456', 'User Two', 'user'),
('user3', 'user3@company.com', 'User@789', 'User Three', 'user'),
('user4', 'user4@company.com', 'User@012', 'User Four', 'user'),
('staff1', 'staff1@company.com', 'Staff@123', 'Staff One', 'staff'),
('staff2', 'staff2@company.com', 'Staff@456', 'Staff Two', 'staff')
ON DUPLICATE KEY UPDATE email=VALUES(email);

--Create password_resets table

                CREATE TABLE IF NOT EXISTS password_resets (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    email VARCHAR(100) NOT NULL,
                    otp_hash VARCHAR(255) NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    expires_at TIMESTAMP NOT NULL,
                    used BOOLEAN DEFAULT FALSE,
                    INDEX (email),
                    INDEX (otp_hash)
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci



SHOW TABLES;

SELECT * FROM contractor_list;
SELECT * FROM bill_tracker;
SELECT * FROM epbg;
