import json
import time

from flask import Flask, request, jsonify

app = Flask(__name__)

# Load seeded data from seed.json
try:
    with open('seed.json', 'r') as f:
        raw_users = json.load(f)
        # Convert keys to match internal structure
        users = [
            {
                "id": u["id"],
                "username": u["doggy"],
                "password": u["zebra42"],
                "email": u["kittycat"],
                "age": u["rocketShip"]
            } for u in raw_users
        ]
except FileNotFoundError:
    users = []


# GET: Return all users
# cRud snippet goes here
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200

# POST: Add a new user
# Crud snippet goes here
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json(silent=True) or {}
    required = ['username', 'password', 'email', 'age']
    if not all(k in data and data[k] not in (None, '') for k in required):
        return jsonify({"error": "Missing required fields", "required": required}), 400
    try:
        age_val = int(data['age'])
    except (ValueError, TypeError):
        return jsonify({"error": "age must be an integer"}), 400

    new_id = (max((u['id'] for u in users), default=0) + 1)
    new_user = {
        "id": new_id,
        "username": data['username'],
        "password": data['password'],
        "email": data['email'],
        "age": age_val
    }
    users.append(new_user)
    return jsonify(new_user), 201


# PUT: Update user by ID
# crUd snippet goes here
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json(silent=True) or {}
    for u in users:
        if u['id'] == user_id:
            if 'username' in data and data['username'] is not None:
                u['username'] = data['username']
            if 'password' in data and data['password'] is not None:
                u['password'] = data['password']
            if 'email' in data and data['email'] is not None:
                u['email'] = data['email']
            if 'age' in data and data['age'] is not None:
                try:
                    u['age'] = int(data['age'])
                except (ValueError, TypeError):
                    return jsonify({"error": "age must be an integer"}), 400
            return jsonify(u), 200
    return jsonify({"error": "User not found"}), 404


# DELETE: Remove user by ID
# cruD snippet goes here
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    global users
    if not any(u['id'] == user_id for u in users):
        return jsonify({"error": "User not found"}), 404
    users = [u for u in users if u['id'] != user_id]
    return jsonify({"message": f"User {user_id} deleted"}), 200


# starts the application, and binds to 127.0.0.1 NOT localhost!!!
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
