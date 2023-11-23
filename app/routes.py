from flask import request, jsonify, abort
from app import app, db
from app.models import User
import logging
from flask_login import login_user
from app.models import Product
from app.forms import ProductForm


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data['username']
    email = data['email']
    password = data['password']

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({'message': 'Username already taken'}), 400

    new_user = User(username=username, email=email, password=password)
    db.session.add(new_user)
    db.session.commit()

    login_user(new_user)

    return jsonify({'message': 'User registered successfully'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    username = data['username']
    password = data['password']

    user = User.query.filter_by(username=username).first()

    if user and user.check_password(password):
        login_user(user)
        return jsonify({'message': 'Login successful'}), 200

    return jsonify({'message': 'Invalid username or password'}), 401


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify({'users': user_list})

# Products API


@app.route('/products', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    product_list = [{'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description, 'stock_quantity': product.stock_quantity} for product in products]
    return jsonify({'products': product_list})


@app.route('/products/<int:product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify({'id': product.id, 'name': product.name, 'price': product.price, 'description': product.description, 'stock_quantity': product.stock_quantity})


@app.route('/products', methods=['POST'])
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


@app.route('/products/<int:product_id>', methods=['PUT'])
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