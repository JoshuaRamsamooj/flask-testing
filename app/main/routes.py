from flask import jsonify, make_response, request
from . import main


@main.route('/')
def home():
    return make_response(jsonify({
        'status': True
    }))


@main.route('/greet/<name>')
def greet(name):
    return make_response(jsonify({
        'status': True,
        'greeting': f'Hello {name}'
    }))


@main.route('/login', methods=['POST'])
def login():
    """fake login function for testing post request"""
    login_data = request.json
    return make_response(jsonify({
        **{'status': True},
        **login_data
    }))
