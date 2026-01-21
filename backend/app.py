from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from mysql.connector import Error
import json
import os
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Database configuration
DB_CONFIG = {
    'host': os.getenv('DB_HOST', 'localhost'),
    'database': os.getenv('DB_NAME', 'reminder_dashboard'),
    'user': os.getenv('DB_USER', 'root'),
    'password': os.getenv('DB_PASSWORD', '7849'),
    'charset': 'utf8mb4',
    'collation': 'utf8mb4_unicode_ci'
}

def get_db_connection():
    """Create and return a database connection"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def init_database():
    """Initialize database and create tables if they don't exist"""
    try:
        connection = get_db_connection()
        if connection:
            cursor = connection.cursor()
            
            # Create contractor_list table
            cursor.execute("""
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
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            """)
            
            # Create bill_tracker table
            cursor.execute("""
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
            """)
            
            # Create epbg table
            cursor.execute("""
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
                ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci
            """)
            
            connection.commit()
            cursor.close()
            connection.close()
            print("Database tables initialized successfully")
            return True
    except Error as e:
        print(f"Error initializing database: {e}")
        return False

# Initialize database on startup
init_database()

# ============= CONTRACTOR LIST ENDPOINTS =============

@app.route('/api/contractor-list', methods=['GET'])
def get_contractor_list():
    """Get all contractor list records"""
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM contractor_list ORDER BY id")
        records = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        # Convert datetime objects to strings
        for record in records:
            if record.get('created_at'):
                record['created_at'] = record['created_at'].isoformat()
            if record.get('updated_at'):
                record['updated_at'] = record['updated_at'].isoformat()
            if record.get('start_date'):
                record['start_date'] = str(record['start_date'])
            if record.get('end_date'):
                record['end_date'] = str(record['end_date'])
        
        return jsonify(records), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/contractor-list', methods=['POST'])
def save_contractor_list():
    """Save contractor list data"""
    try:
        data = request.get_json()
        if not data or 'records' not in data:
            return jsonify({'error': 'Invalid data format'}), 400
        
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = connection.cursor()
        
        # Delete all existing records (or you can implement update logic)
        cursor.execute("DELETE FROM contractor_list")
        
        # Insert new records
        insert_query = """
            INSERT INTO contractor_list 
            (sno, efile, contractor, description, value, start_date, end_date, duration, 
             file_name, file_base64, file_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        records_to_insert = []
        for record in data['records']:
            records_to_insert.append((
                record.get('sno', ''),
                record.get('efile', ''),
                record.get('contractor', ''),
                record.get('description', ''),
                record.get('value', ''),
                record.get('startDate') or None,
                record.get('endDate') or None,
                record.get('duration', ''),
                record.get('fileName', ''),
                record.get('fileBase64', ''),
                record.get('fileType', '')
            ))
        
        cursor.executemany(insert_query, records_to_insert)
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return jsonify({'message': 'Contractor list saved successfully', 'count': len(records_to_insert)}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

# ============= BILL TRACKER ENDPOINTS =============

@app.route('/api/bill-tracker', methods=['GET'])
def get_bill_tracker():
    """Get all bill tracker records"""
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM bill_tracker ORDER BY id")
        records = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        # Convert datetime objects to strings
        for record in records:
            if record.get('created_at'):
                record['created_at'] = record['created_at'].isoformat()
            if record.get('updated_at'):
                record['updated_at'] = record['updated_at'].isoformat()
            date_fields = ['approved_date', 'bill_date', 'bill_due_date', 'bill_paid_date']
            for field in date_fields:
                if record.get(field):
                    record[field] = str(record[field])
        
        return jsonify(records), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/bill-tracker', methods=['POST'])
def save_bill_tracker():
    """Save bill tracker data"""
    try:
        data = request.get_json()
        if not data or 'records' not in data:
            return jsonify({'error': 'Invalid data format'}), 400
        
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = connection.cursor()
        
        # Delete all existing records
        cursor.execute("DELETE FROM bill_tracker")
        
        # Insert new records
        insert_query = """
            INSERT INTO bill_tracker 
            (sno, efile, contractor, approved_date, approved_amount, bill_frequency, 
             bill_date, bill_due_date, bill_paid_date, paid_amount, 
             file_name, file_base64, file_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        records_to_insert = []
        for record in data['records']:
            records_to_insert.append((
                record.get('sno', ''),
                record.get('efile', ''),
                record.get('contractor', ''),
                record.get('approvedDate') or None,
                record.get('approvedAmount', ''),
                record.get('billFrequency', ''),
                record.get('billDate') or None,
                record.get('billDueDate') or None,
                record.get('billPaidDate') or None,
                record.get('paidAmount', ''),
                record.get('fileName', ''),
                record.get('fileBase64', ''),
                record.get('fileType', '')
            ))
        
        cursor.executemany(insert_query, records_to_insert)
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return jsonify({'message': 'Bill tracker saved successfully', 'count': len(records_to_insert)}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

# ============= EPBG ENDPOINTS =============

@app.route('/api/epbg', methods=['GET'])
def get_epbg():
    """Get all EPBG records"""
    try:
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM epbg ORDER BY id")
        records = cursor.fetchall()
        
        cursor.close()
        connection.close()
        
        # Convert datetime objects to strings
        for record in records:
            if record.get('created_at'):
                record['created_at'] = record['created_at'].isoformat()
            if record.get('updated_at'):
                record['updated_at'] = record['updated_at'].isoformat()
            if record.get('bg_date'):
                record['bg_date'] = str(record['bg_date'])
        
        return jsonify(records), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/epbg', methods=['POST'])
def save_epbg():
    """Save EPBG data"""
    try:
        data = request.get_json()
        if not data or 'records' not in data:
            return jsonify({'error': 'Invalid data format'}), 400
        
        connection = get_db_connection()
        if not connection:
            return jsonify({'error': 'Database connection failed'}), 500
        
        cursor = connection.cursor()
        
        # Delete all existing records
        cursor.execute("DELETE FROM epbg")
        
        # Insert new records
        insert_query = """
            INSERT INTO epbg 
            (sno, contractor, po_no, bg_no, bg_date, bg_amount, bg_validity, 
             gem_bid_no, ref_efile_no, file_name, file_base64, file_type)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        records_to_insert = []
        for record in data['records']:
            records_to_insert.append((
                record.get('sno', ''),
                record.get('contractor', ''),
                record.get('poNo', ''),
                record.get('bgNo', ''),
                record.get('bgDate') or None,
                record.get('bgAmount', ''),
                record.get('bgValidity', ''),
                record.get('gemBid', ''),
                record.get('refEfile', ''),
                record.get('fileName', ''),
                record.get('fileBase64', ''),
                record.get('fileType', '')
            ))
        
        cursor.executemany(insert_query, records_to_insert)
        connection.commit()
        
        cursor.close()
        connection.close()
        
        return jsonify({'message': 'EPBG saved successfully', 'count': len(records_to_insert)}), 200
    except Error as e:
        return jsonify({'error': str(e)}), 500

# Health check endpoint
@app.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    try:
        connection = get_db_connection()
        if connection:
            connection.close()
            return jsonify({'status': 'healthy', 'database': 'connected'}), 200
        else:
            return jsonify({'status': 'unhealthy', 'database': 'disconnected'}), 500
    except Exception as e:
        return jsonify({'status': 'unhealthy', 'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
