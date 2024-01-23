from flask import jsonify, request

from data import product_records


def read_products_by_id(id):
    for product in product_records:
        if product['product_id'] == int(id):
            return jsonify({"message": "product found", "results": product}), 200
    return jsonify({"message": f"product with id {id} not found."}), 404


def get_all_products():
    return jsonify({'message': 'products found', "result": product_records}), 200


def read_products_by_active(active):
    for product in product_records:
        if product['active'] == bool(active):
            return jsonify({"message": "product is active", "results": product}), 200


def add_product():
    data = request.form if request.form else request.json
    product = {}

    highest_id = max([p.get('product_id', 0) for p in product_records])

    product['product_id'] = highest_id + 1

    product['product_name'] = data['name']
    product['price'] = data['price']
    product['description'] = data['description']
    product['active'] = data['active']

    product_records.append(product)

    return jsonify({"message": "Here are your results"}), 200


def update_product(product_id):
    data = request.form if request.form else request.json
    product = {}

    for record in product_records:
        if record['product_id'] == int(product_id):
            product = record

    product['product_name'] = data.get('product_name', product['name'])
    product['description'] = data.get('description', product['description'])
    product['price'] = data.get('price', product['price'])
    product['active'] = data.get('active', product['active'])

    return jsonify({'message': 'product updated', 'result': data}), 200


def delete_product(product_id):
    for product in product_records:
        if product['product_id'] == product_id:
            product_records.remove(product)
            return jsonify({"message": "Product deleted successfully"}), 200
