# product-service/app.py
# Simple Flask microservice for products

from flask import Flask, jsonify, request, abort
from uuid import uuid4

app = Flask(__name__)

# In-memory store for demo (no DB here)
PRODUCTS = {}

# Health check
@app.route("/api/health", methods=["GET"])
def health():
    return jsonify({"status": "ok", "service": "product-service"}), 200

# List products
@app.route("/api/products", methods=["GET"])
def list_products():
    # return list of products
    return jsonify(list(PRODUCTS.values())), 200

# Create product
@app.route("/api/products", methods=["POST"])
def create_product():
    payload = request.get_json(silent=True)
    if not payload or "name" not in payload:
        abort(400, description="Missing 'name' in JSON body")
    product_id = str(uuid4())
    product = {
        "id": product_id,
        "name": payload.get("name"),
        "price": payload.get("price", 0),
        "metadata": payload.get("metadata", {}),
    }
    PRODUCTS[product_id] = product
    return jsonify(product), 201

# Get product by id
@app.route("/api/products/<product_id>", methods=["GET"])
def get_product(product_id):
    product = PRODUCTS.get(product_id)
    if not product:
        abort(404, description="Product not found")
    return jsonify(product), 200

# Simple delete
@app.route("/api/products/<product_id>", methods=["DELETE"])
def delete_product(product_id):
    if product_id not in PRODUCTS:
        abort(404, description="Product not found")
    del PRODUCTS[product_id]
    return jsonify({"deleted": product_id}), 200

if __name__ == "__main__":
    # Default host/port for container
    app.run(host="0.0.0.0", port=5000)
