#!/usr/bin/python3
"""Flask API with Basic Authentication"""

from flask import Flask
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "user1": generate_password_hash("password")
}


@auth.verify_password
def verify_password(username, password):
    """Verify username and password"""
    if username in users and check_password_hash(users[username], password):
        return username
    return None


@app.route("/")
def home():
    """Home route"""
    return "Welcome to the Flask API!"


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Protected route"""
    return "Basic Auth: Access Granted"


if __name__ == "__main__":
    app.run()
