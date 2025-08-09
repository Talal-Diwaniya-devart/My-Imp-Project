import os
from dotenv import load_dotenv

load_dotenv()

# Utility to fetch env variables with optional defaults and enforce required vars
def get_env_var(key, default=None, required=False):
    value = os.getenv(key, default)
    if required and value is None:
        raise EnvironmentError(f"Required environment variable '{key}' not set.")
    return value

# Flask Configuration
FLASK_CONFIG = {
    'SECRET_KEY': get_env_var('SECRET_KEY', required=True),
    'DEBUG': get_env_var('DEBUG', 'False').lower() == 'true',
    'TESTING': get_env_var('TESTING', 'False').lower() == 'true'
}

# API Keys and Secrets (enforce required)
API_KEYS = {
    'stripe': get_env_var('STRIPE_SECRET_KEY', required=True),
    'sendgrid': get_env_var('SENDGRID_API_KEY', required=True),
    'aws_access': get_env_var('AWS_ACCESS_KEY_ID', required=True),
    'aws_secret': get_env_var('AWS_SECRET_ACCESS_KEY', required=True)
}

# Database URLs
DATABASE_URLS = {
    'development': get_env_var('DEV_DATABASE_URL', 'sqlite:///./dev.db'),
    'testing': get_env_var('TEST_DATABASE_URL', 'sqlite:///./test.db'),
    'production': get_env_var('PROD_DATABASE_URL', required=True)
}

# Admin credentials - DO NOT store passwords in code or environment in production!
# Instead, use a secure vault or secrets manager.
ADMIN_CREDS = {
    'username': get_env_var('ADMIN_USERNAME', 'superadmin'),
    'password': get_env_var('ADMIN_PASSWORD', None),
    'email': get_env_var('ADMIN_EMAIL', 'admin@company.internal')
}

if not ADMIN_CREDS['password']:
    raise EnvironmentError("Admin password is not set in environment variables!")

# Optional: add logging or alerts if using default/fallback values (like dev/testing DBs)
