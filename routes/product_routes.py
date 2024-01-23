from flask import Blueprint

from controllers import products_controllers

product = Blueprint('/product', __name__)


@product.route('/products/<product_id>', methods=["GET"])
def read_products_by_id(id):
    return products_controllers.read_products_by_id(id)


@product.route('/products', methods=["GET"])
def read_all_products():
    return products_controllers.read_all_products()


@product.route('/products/active', methods=["GET"])
def read_products_active(active):
    return products_controllers.read_products_by_active(active)


@product.route('/product', methods=['POST'])
def add_product():
    return products_controllers.add_product()


@product.route('/product<product_id>', methods=['PUT'])
def update_product():
    return products_controllers.update_product()


@product.route('/product/delete/<product_id>', methods=['DELETE'])
def delete_product():
    return products_controllers.delete_product()
