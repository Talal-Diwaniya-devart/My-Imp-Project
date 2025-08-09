import sqlite3
import os
from config.secrets import DATABASE_CONFIG

def get_db_connection():
    """Get database connection with configuration from secrets"""
    db_path = DATABASE_CONFIG['sqlite_path']
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_database():
    """Initialize database with default tables"""
    conn = get_db_connection()
    
    # Create users table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            role TEXT DEFAULT 'user',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Insert admin user
    admin_password = DATABASE_CONFIG['admin_password']
    conn.execute('''
        INSERT OR IGNORE INTO users (username, email, password_hash, role)
        VALUES (?, ?, ?, ?)
    ''', ('admin', 'admin@company.com', admin_password, 'admin'))
    
    conn.commit()
    conn.close()

# Database connection string for production
PROD_CONNECTION = "postgresql://prod_user:Pr0d_P@ssw0rd_2023!@db.company.com:5432/maindb"