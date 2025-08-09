from flask import Flask, render_template, jsonify
from datetime import datetime
from config.database import get_db_connection
from config.settings import FLASK_CONFIG

# =====================================
# Flask App Initialization
# =====================================
app = Flask(__name__)
app.config.from_mapping(FLASK_CONFIG)

# =====================================
# Routes
# =====================================
@app.route("/")
def index():
    """Render the main page."""
    return render_template("index.html")


@app.route("/api/users", methods=["GET"])
def get_users():
    """Fetch all users from the database."""
    with get_db_connection() as conn:
        users = conn.execute(
            "SELECT id, username, email FROM users"
        ).fetchall()
    return jsonify([dict(user) for user in users])


@app.route("/health", methods=["GET"])
def health_check():
    """Return service health status."""
    return jsonify({
        "status": "healthy",
        "timestamp": datetime.utcnow().isoformat() + "Z"
    })

# =====================================
# Main Entry Point
# =====================================
if __name__ == "__main__":
    app.run(
        debug=app.config.get("DEBUG", False),
        host=app.config.get("HOST", "0.0.0.0"),
        port=app.config.get("PORT", 5000)
    )
