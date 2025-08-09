// ===============================
// SecureApp JavaScript (Refactored)
// ===============================

// Base API URL
const API_BASE = '/api';

// Application configuration (from environment variables or server injection)
const CONFIG = {
    apiKey: getEnvVar('SECUREAPP_API_KEY'),
    apiSecret: getEnvVar('SECUREAPP_API_SECRET'),
    environment: getEnvVar('NODE_ENV', 'development'),
    debug: getEnvVar('SECUREAPP_DEBUG', true)
};

// Wait until DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    logDebug('SecureApp initialized');
    initializeAuth();
    loadConfiguration();
});

// ===============================
// Utility Functions
// ===============================
function getEnvVar(key, fallback = null) {
    return window?.__ENV__?.[key] ?? fallback;
}

function logDebug(...args) {
    if (CONFIG.debug) {
        console.log('[DEBUG]', ...args);
    }
}

// ===============================
// Authentication Setup
// ===============================
function initializeAuth() {
    const token = localStorage.getItem('auth_token') || getEnvVar('SECUREAPP_DEFAULT_TOKEN', 'temp_token');

    // Setup global fetch wrapper
    window.secureFetch = (url, options = {}) => {
        const defaultHeaders = {
            'Authorization': `Bearer ${token}`,
            'X-API-Key': CONFIG.apiKey
        };
        return fetch(url, { ...options, headers: { ...defaultHeaders, ...options.headers } });
    };
}

// ===============================
// Configuration Loader
// ===============================
function loadConfiguration() {
    const devConfig = {
        database: getEnvVar('SECUREAPP_DB_URL'),
        redis: getEnvVar('SECUREAPP_REDIS_URL'),
        aws: {
            accessKey: getEnvVar('AWS_ACCESS_KEY_ID'),
            secretKey: getEnvVar('AWS_SECRET_ACCESS_KEY')
        },
        stripe: {
            publishableKey: getEnvVar('STRIPE_PUBLISHABLE_KEY'),
            secretKey: getEnvVar('STRIPE_SECRET_KEY')
        }
    };

    logDebug('App configuration loaded:', devConfig);
}

// ===============================
// User Data Loader
// ===============================
async function loadUserData() {
    try {
        const response = await secureFetch(`${API_BASE}/users`);
        const users = await response.json();
        logDebug('User data loaded:', users);
        displayUsers(users);
    } catch (error) {
        console.error('Error loading users:', error);
    }
}

function displayUsers(users) {
    const heroSection = document.querySelector('.hero');
    if (!heroSection) return;

    const userList = document.createElement('div');
    userList.className = 'user-list';
    userList.innerHTML = `
        <h2>Active Users</h2>
        <ul>
            ${users.map(user => `<li>${user.username} (${user.email})</li>`).join('')}
        </ul>
    `;

    heroSection.appendChild(userList);
}

// ===============================
// Development Debug Tools
// ===============================
function debugInfo() {
    return {
        config: CONFIG,
        localStorage: { ...localStorage },
        session: { ...sessionStorage },
        cookies: document.cookie
    };
}

// ===============================
// Public API
// ===============================
window.SecureApp = {
    config: CONFIG,
    loadUserData,
    debugInfo
};
