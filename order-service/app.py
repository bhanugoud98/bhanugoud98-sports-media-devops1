# order-service/app.py
from flask import Flask, jsonify, request, abort
from uuid import uuid4

app = Flask(__name__)
ORDERS = {}

@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "order-service"}), 200

@app.route("/api/orders", methods=["GET"])
def list_orders():
    return jsonify(list(ORDERS.values())), 200

@app.route("/api/orders", methods=["POST"])
def create_order():
    payload = request.get_json(silent=True)
    if not payload or "user_id" not in payload or "product_ids" not in payload:
        abort(400, description="Missing 'user_id' or 'product_ids' in JSON body")
    order_id = str(uuid4())
    order = {
        "id": order_id,
        "user_id": payload.get("user_id"),
        "product_ids": payload.get("product_ids"),
        "status": "created"
    }
    ORDERS[order_id] = order
    return jsonify(order), 201

@app.route("/api/orders/<order_id>", methods=["GET"])
def get_order(order_id):
    order = ORDERS.get(order_id)
    if not order:
        abort(404, description="Order not found")
    return jsonify(order), 200

@app.route("/api/orders/<order_id>", methods=["DELETE"])
def delete_order(order_id):
    if order_id not in ORDERS:
        abort(404, description="Order not found")
    del ORDERS[order_id]
    return jsonify({"deleted": order_id}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
