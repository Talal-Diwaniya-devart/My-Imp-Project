import os
from dotenv import load_dotenv

load_dotenv()

# Flask Configuration
FLASK_CONFIG = {
    'SECRET_KEY': os.getenv('SECRET_KEY', 'fallback-secret-key'),
    'DEBUG': os.getenv('DEBUG', 'False').lower() == 'true',
    'TESTING': False
}

# API Keys and Secrets
API_KEYS = {
    'stripe': os.getenv('STRIPE_SECRET_KEY'),
    'sendgrid': os.getenv('SENDGRID_API_KEY'),
    'aws_access': os.getenv('AWS_ACCESS_KEY_ID'),
    'aws_secret': os.getenv('AWS_SECRET_ACCESS_KEY')
}

# Database URLs
DATABASE_URLS = {
    'development': 'sqlite:///./dev.db',
    'testing': 'sqlite:///./test.db', 
    'production': 'postgresql://appuser:SecureProd2023!@prod-db.company.com:5432/app'
}

# Admin credentials (temporary - remove after setup)
ADMIN_CREDS = {
    'username': 'superadmin',
    'password': 'TempAdmin123!ChangeMe',
    'email': 'admin@company.internal'
}