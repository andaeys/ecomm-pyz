from flask import request, jsonify, Blueprint
from app import db
from app.models import Product
from app.forms import ProductForm


product_routes = Blueprint('product_routes', __name__)


# Products API
@product_routes.route('/all', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    product_list = [{'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description, 'stock_quantity': product.stock_quantity} for product in products]
    return jsonify({'products': product_list})


@product_routes.route('/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description, 'stock_quantity': product.stock_quantity})


@product_routes.route('/new', methods=['POST'])
def create_product():
    form = ProductForm(request.json)
    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            price=form.price.data,
            description=form.description.data,
            stock_quantity=form.stock_quantity.data
        )
        db.session.add(product)
        db.session.commit()
        return jsonify({'message': 'Product created successfully'}), 201
    else:
        return jsonify({'error': 'Invalid data'}), 400


@product_routes.route('update/<int:product_id>', methods=['PUT'])
def edit_product(product_id):
    product = Product.query.get_or_404(product_id)
    form = ProductForm(request.json)
    if form.validate_on_submit():
        product.name = form.name.data
        product.price = form.price.data
        product.description = form.description.data
        product.stock_quantity = form.stock_quantity.data
        db.session.commit()
        return jsonify({'message': 'Product updated successfully'}), 200
    else:
        return jsonify({'error': 'Invalid data'}), 400