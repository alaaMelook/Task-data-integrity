from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from db import get_db_connection

product = Blueprint('product', __name__)

@product.route('/products', methods=['POST'])
@jwt_required()
def add_product():
    data = request.json
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, description, price, quantity) VALUES (%s, %s, %s, %s)",
                   (data['name'], data['description'], data['price'], data['quantity']))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({"message": "Product added successfully"})
