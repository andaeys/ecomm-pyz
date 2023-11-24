from flask import Blueprint, jsonify
from app import db
from app.models import ShoppingCart, Product

cart_routes = Blueprint('cart_routes', __name__)


@cart_routes.route('/add/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    product = Product.query.get_or_404(product_id)

    # Check if the product is already in the user's cart
    existing_item = ShoppingCart.query.filter_by(product_id=product.id).first()

    if existing_item:
        existing_item.quantity += 1
    else:
        new_item = ShoppingCart(product_id=product.id, user_id=1, quantity=1)
        db.session.add(new_item)

    db.session.commit()

    return jsonify({'message': 'Product added to cart successfully'}), 200


@cart_routes.route('/get', methods=['GET'])
def get_cart():
    cart_items = ShoppingCart.query.all()

    cart_data = [{'product_id': item.product_id, 'quantity': item.quantity} for item in cart_items]
    return jsonify({'cart': cart_data})


@cart_routes.route('/checkout', methods=['POST'])
def checkout():
    # Get user's cart items
    cart_items = ShoppingCart.query.all()

    # Update product stock quantity and remove items from the cart
    for item in cart_items:
        product = Product.query.get_or_404(item.product_id)
        if product.stock_quantity >= item.quantity:
            product.stock_quantity -= item.quantity
            db.session.delete(item)
        else:
            return jsonify({'error': f'Not enough stock for product {product.id}'}), 400

    db.session.commit()

    return jsonify({'message': 'Checkout successful'}), 200
