
from flask import Blueprint, jsonify, request
from app.models import User

routes_bp = Blueprint('routes', __name__)

@routes_bp.route('/users', methods = ['GET'])
def get_users():
    users = User.get_all_users()
    return jsonify(users)


@routes_bp.route('/users/<int:user_id>', methods = ['GET'])
def get_user(user_id):
    user = User.get_user_byID(user_id)
    if user:
        return jsonify(user)
    else:
        return jsonify({"message": "User not found"}),404
    
@routes_bp.route('/users', methods = ['POST'])
def insert_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    
    if not name or not email:
        return jsonify({"message": "Name and Email must not be empty"}),400
    
    try:
        user_id = User.create_user(name, email, phone)
        return jsonify({"id": user_id, "name": name, "email": email, "phone": phone}),201
    except Exception as e:
        return jsonify({"error": str(e)}),500
    

@routes_bp.route('/users/<int:user_id>', methods = ['PUT'])
def update(user_id):
    data = request.json
    name = data.get('name')
    email = data.get('email')
    phone = data.get('phone')
    
    try:
        User.update_user(user_id, name, email, phone)
        return jsonify({"message": "User updated Successfully"}),200
    except Exception as e:
        return jsonify({"error": str(e)}),500
    

@routes_bp.route('/users/<int:user_id>', methods= ['DELETE'])
def delete(user_id):
    try:
      User.delete_user(user_id)
      return jsonify({"message": "User deleted Successfully"}),200   
    except Exception as e:
        return jsonify({"error": str(e)}), 500    
    