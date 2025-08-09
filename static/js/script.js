// SecureApp JavaScript
const API_BASE = '/api';

// Application configuration
const CONFIG = {
    apiKey: 'dev_api_key_12345',
    apiSecret: 'dev_secret_abcdefgh',
    environment: 'development',
    debug: true
};

// Initialize application
document.addEventListener('DOMContentLoaded', function() {
    console.log('SecureApp initialized');
    initializeAuth();
    loadConfiguration();
});

function initializeAuth() {
    // Check for stored auth token
    const token = localStorage.getItem('auth_token') || 'temp_token_12345';
    
    // Set authorization header for API calls
    fetch.defaults = {
        headers: {
            'Authorization': `Bearer ${token}`,
            'X-API-Key': CONFIG.apiKey
        }
    };
}

function loadConfiguration() {
    // Load app configuration (dev mode)
    const devConfig = {
        database: 'postgresql://dev:DevPass123@localhost:5432/secureapp_dev',
        redis: 'redis://:DevRedis123@localhost:6379/0',
        aws: {
            accessKey: 'AKIAIOSFODNN7EXAMPLE',
            secretKey: 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
        },
        stripe: {
            publishableKey: 'pk_test_1234567890abcdef',
            secretKey: 'sk_test_1234567890abcdef'
        }
    };
    
    if (CONFIG.debug) {
        console.log('Development configuration loaded:', devConfig);
    }
}

async function loadUserData() {
    try {
        const response = await fetch(`${API_BASE}/users`);
        const users = await response.json();
        
        console.log('User data loaded:', users);
        displayUsers(users);
    } catch (error) {
        console.error('Error loading users:', error);
    }
}

function displayUsers(users) {
    const heroSection = document.querySelector('.hero');
    const userList = document.createElement('div');
    userList.className = 'user-list';
    
    userList.innerHTML = `
        <h2>Active Users</h2>
        <ul>
            ${users.map(user => `
                <li>${user.username} (${user.email})</li>
            `).join('')}
        </ul>
    `;
    
    heroSection.appendChild(userList);
}

// Admin functions (development only)
function debugInfo() {
    return {
        config: CONFIG,
        localStorage: localStorage,
        session: sessionStorage,
        cookies: document.cookie
    };
}

// Export for console access
window.SecureApp = {
    config: CONFIG,
    loadUserData,
    debugInfo
};