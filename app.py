from flask import Flask, render_template, request, jsonify
import os
import sqlite3
import hashlib
from config.database import get_db_connection
from config.settings import FLASK_CONFIG

app = Flask(__name__)
app.config.update(FLASK_CONFIG)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/users')
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT id, username, email FROM users').fetchall()
    conn.close()
    return jsonify([dict(user) for user in users])

@app.route('/health')
def health_check():
    return {'status': 'healthy', 'timestamp': str(datetime.now())}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)