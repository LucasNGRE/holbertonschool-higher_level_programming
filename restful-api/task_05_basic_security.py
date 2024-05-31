#!/usr/bin/env python3
'''Module of API security'''
from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from flask_jwt_extended import verify_jwt_in_request

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("admin_password"),
        "role": "admin"
    }
}


app = Flask(__name__)
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@auth.error_handler
def unauthorized():
    return jsonify({"error": "Unauthorized access"}), 401


app.config["JWT_SECRET_KEY"] = "holberton"
jwt = JWTManager(app)


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if not username or not password:
        return jsonify({"message": "Missing username or password"}), 400
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"message": "Bad username or password"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    verify_jwt_in_request()
    return "JWT Auth: Access Granted"


# Protected route with role-based access control
@app.route("/admin-only")
@jwt_required()
def admin_only():
    verify_jwt_in_request()
    current_user = get_jwt_identity()
    if users[current_user]["role"] != "admin":
        return jsonify({"error": "Unauthorized access"}), 403
    return "Admin Access: Granted"


# Handle JWT unauthorized access
@jwt.unauthorized_loader
def unauthorized_loader_callback(callback):
    return jsonify({"error": "Missing JWT token"}), 401


# Handle expired JWT token
@jwt.expired_token_loader
def expired_token_callback(expired_token):
    return jsonify({"error": "Expired token"}), 401


if __name__ == '__main__':
    app.run()
