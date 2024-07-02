from flask import Flask, request, jsonify
from models.auth import AuthSystem

app = Flask(__name__)
user = AuthSystem()

@app.route('/signup', methods=['POST'])
def signup():
    """this is the sign up endpoint"""
    data = request.get_json()
    email = data.get('email')
    username = data.get('username')
    password = data.get('password')
    confirm_pass = data.get('confirmPassword')

    if password != confirm_pass:
        return jsonify({'error': 'Passwords do no match'}), 400
    
    result = user.signup(email, username, password, confirm_pass)

    if result == 'Email already taken' or result== 'Passwords don\'t match':
        return jsonify({'error': result}), 400
    
    return jsonify({'message': result}), 200
