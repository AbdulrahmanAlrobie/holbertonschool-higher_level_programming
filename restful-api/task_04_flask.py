#!/usr/bin/env python3
"""Simple RESTful API using Flask framework."""

from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# In-memory users store
users = {}

@app.route('/', methods=['GET'])
def home():
    """Root endpoint returns a welcome message."""
    return "Welcome to the Flask API!"

@app.route('/data', methods=['GET'])
def get_usernames():
    """Return a JSON list of all usernames."""
    return jsonify(list(users.keys()))

@app.route('/status', methods=['GET'])
def status():
    """Return API status."""
    return "OK"

@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Return full user object or error if not found."""
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user via JSON payload."""
    data = request.get_json(force=True)
    username = data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    # Build user object
    user = {
        "username": username,
        "name": data.get('name'),
        "age": data.get('age'),
        "city": data.get('city')
    }
    users[username] = user
    return jsonify({"message": "User added", "user": user}), 201

if __name__ == '__main__':
    app.run()
