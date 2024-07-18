from flask import Flask, request, jsonify
from flask_cors import CORS
from models.auth import AuthSystem

app = Flask(__name__)
CORS(app)
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
        return jsonify({'error': result, 'res': "11"}), 400
    
    return jsonify({'message': result, 'res': "00"}), 200

@app.route('/login', methods=['POST'])
def login():
    """this is the sign up endpoint"""
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    result = user.login(email, password)
    if result == "Incorrect password or email" or result == "Email not registered, please sign up"
        return jsonify({'message': result, 'res':"11"}), 400
    
    return jsonify({'message': result, 'res':"00"}), 200

@app.route('/create_task', methods=['POST'])
def create_task():
    """create task endpoint"""
    data = request.get_json()
    email= data.get('email')
    task = data.get('task')
    id = data.get('id')
    status = data.get('status')

    result = user.add_task(email, task,id, status)
    return jsonify({'message': result, 'res':"00"}), 200

@app.route('/get_tasks', methods=['POST'])
def get_tasks():
    """get users tasks"""
    data = request.get_json()
    email = data.get('email')
    result = user.get_tasks(email)
    return jsonify({'message': result, 'res':"00"})

@app.route('/update_task', methods=['PUT'])
def update_task():
    """update task"""
    data = request.get_json()
    email = data.get('email')
    id = data.get('id')
    task = data.get('title')
    status = data.get('status')
    result = user.update_task(email, id, task, status)
    return jsonify({'message': result}), 200

@app.route('/delete', methods=['DELETE'])
def delete_task():
    """delete task"""
    data = request.get_json()
    email = data.get('email')
    id= data.get('id')
    result = user.remove_task(email, id)
    return jsonify({'message': result}), 200

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode
