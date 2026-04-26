#!/usr/bin/python3
"""Flask authentication example."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "super-secret-key-change-this"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "admin": {
        "password": generate_password_hash("adminpass"),
        "role": "admin"
    },
    "john": {
        "password": generate_password_hash("johnpass"),
        "role": "user"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password for Basic Auth."""
    if username in users and check_password_hash(
        users[username]["password"], password
    ):
        return username
    return None


@app.route("/")
def home():
    """Public route."""
    return jsonify({"message": "Welcome"})


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Protected route using Basic Auth."""
    return jsonify({
        "message": "Basic Auth: Access granted",
        "user": auth.current_user()
    })


@app.route("/login", methods=["POST"])
def login():
    """Login route that returns JWT token."""
    data = request.get_json(silent=True)

    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Invalid credentials"}), 401

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)

    return jsonify({"access_token": access_token}), 200


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Protected route using JWT."""
    current_user = get_jwt_identity()

    return jsonify({
        "message": "JWT: Access granted",
        "user": current_user
    })


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Route only accessible to admin users."""
    current_user = get_jwt_identity()

    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return jsonify({
        "message": "Admin access granted",
        "user": current_user
    })


if __name__ == "__main__":
    app.run()
