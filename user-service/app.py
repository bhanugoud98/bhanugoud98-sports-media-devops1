# user-service/app.py
from flask import Flask, jsonify, request, abort
from uuid import uuid4

app = Flask(__name__)
USERS = {}

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "user-service"}), 200

@app.route("/api/users", methods=["GET"])
def list_users():
    return jsonify(list(USERS.values())), 200

@app.route("/api/users", methods=["POST"])
def create_user():
    payload = request.get_json(silent=True)
    if not payload or "email" not in payload:
        abort(400, description="Missing 'email' in JSON body")
    user_id = str(uuid4())
    user = {
        "id": user_id,
        "email": payload.get("email"),
        "name": payload.get("name", "")
    }
    USERS[user_id] = user
    return jsonify(user), 201

@app.route("/api/users/<user_id>", methods=["GET"])
def get_user(user_id):
    user = USERS.get(user_id)
    if not user:
        abort(404, description="User not found")
    return jsonify(user), 200

@app.route("/api/users/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    if user_id not in USERS:
        abort(404, description="User not found")
    del USERS[user_id]
    return jsonify({"deleted": user_id}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
