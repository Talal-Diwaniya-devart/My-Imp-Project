# SENSITIVE: This file contains production secrets
# DO NOT COMMIT TO VERSION CONTROL

import os

# Production Database Configuration
DATABASE_CONFIG = {
    'host': 'prod-mysql.company.com',
    'port': 3306,
    'database': 'production_app',
    'username': 'prod_app_user',
    'password': 'MySQLProd2023!SecureDB',
    'sqlite_path': './database/app.db',
    'admin_password': 'hashedAdminPass123!'
}

# API Keys for Production Services
PRODUCTION_KEYS = {
    'jwt_secret': 'jwt_super_secret_key_production_2023',
    'encryption_key': 'AES256_ENCRYPTION_KEY_32_BYTES_LONG',
    'api_master_key': 'master_api_key_full_access_2023',
    'webhook_secret': 'webhook_validation_secret_key',
    'oauth_client_secret': 'oauth_client_secret_google_auth'
}

# Third Party Service Credentials
EXTERNAL_SERVICES = {
    'paypal': {
        'client_id': 'paypal_client_id_production',
        'client_secret': 'paypal_secret_key_prod_2023'
    },
    'github': {
        'webhook_secret': 'github_webhook_secret_2023'
    },
    'slack': {
        'signing_secret': 'slack_signing_secret_key_2023'
    }
}

# Infrastructure Secrets
INFRASTRUCTURE = {
    'docker_registry': {
        'username': 'deploy_user',
        'password': 'DockerRegistry2023!Deploy'
    },
    'kubernetes': {
        'token': 'k8s_service_account_token_production',
        'cluster_cert': '/path/to/cluster-ca-certificate.pem'
    },
    'monitoring': {
        'grafana_admin': 'GrafanaAdmin2023!Monitor',
        'prometheus_token': 'prometheus_bearer_token_2023'
    }
}

# Security Configuration
SECURITY_CONFIG = {
    'password_salt': 'unique_salt_for_password_hashing_2023',
    'session_secret': 'flask_session_secret_key_2023',
    'csrf_secret': 'csrf_protection_secret_key_2023',
    'rate_limit_key': 'rate_limiting_redis_key_2023'
}

# Flag for CTF Challenge
CTF_FLAG = "CTF{g1t_s3cr3ts_1n_c0mm1t_h1st0ry_f0und}"