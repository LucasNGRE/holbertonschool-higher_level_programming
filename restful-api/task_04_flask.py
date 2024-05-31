#!/usr/bin/env python3
from flask import Flask
from flask import jsonify
from flask import request
import json


users = {}

app = Flask(__name__)


@app.route("/")
def home():
    message = "Welcome to the Flask API!"
    return (message)


@app.route("/data")
def data():
    usernames = list(users.keys())
    return jsonify(usernames)


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_users(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    if not request.json or "username" not in request.json:
        return jsonify({"error": "Username is required"}), 400
    user_data = request.json
    username = user_data["username"]
    if username in users:
        return jsonify({"error": "User already exists"}), 400
    users[username] = {
        "username": user_data.get("username"),
        "name": user_data.get("name"),
        "age": user_data.get("age"),
        "city": user_data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
