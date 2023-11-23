from flask import request, jsonify
from app import app
from app.models import User
import logging


# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


@app.route('/hello', methods=['GET'])
def sample_endpoint():
    data = {'message': 'This is a sample endpoint.'}
    return jsonify(data)


@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = [{'id': user.id, 'username': user.username, 'email': user.email} for user in users]
    return jsonify({'users': user_list})


