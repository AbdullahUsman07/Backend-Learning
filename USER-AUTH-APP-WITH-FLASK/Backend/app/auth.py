
from flask import jsonify, Blueprint, request
from .models import User
from .import db
from flask_jwt_extended import get_jwt_identity,create_access_token,jwt_required
from werkzeug.security import generate_password_hash, check_password_hash
from .auth_helpers import role_required

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods= ['POST'])
def register_user():
    data= request.json
    
    if User.query.filter_by(username= data['username']).first():
        return jsonify({"msg":"Username already exists"}), 400
    
    role = data.get('role', 'user')
    if role != 'user':
        return jsonify({"msg": "Can't assign admin role"}), 403
    
    hashed_password = generate_password_hash(data['password'], method='pbkdf2:sha256')
    new_user = User(
        username = data['username'],
        password = hashed_password,
        age = data['age'],
        role = data['role']
    )
    db.session.add(new_user)
    db.session.commit()
    
    access_token = create_access_token(identity= str(new_user.id))
    return jsonify({"msg":"User registered successfully","access_token":access_token}), 201


@auth_bp.route('/login',methods = ['POST'])
def login_user():
    data = request.json
    user = User.query.filter_by(username = data['username']).first()
    if not user:
        return jsonify({"msg":"User not found"}), 404
    if check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity = str(user.id))
        return jsonify(access_token = access_token, msg= "Login successful"), 200
    return jsonify({"msg": "Invalid credentials"}), 401


@auth_bp.route('/profile', methods = ['GET'])
@jwt_required()
def get_profile():
    current_user_id = get_jwt_identity()
    user = User.query.get(current_user_id)
    return jsonify({
        "username": user.username,
        "age": user.age,
        "role": user.role
        }),200

@auth_bp.route('/admin-dashboard', methods= ['GET'])
@jwt_required()
@role_required(['admin'])
def admin_dashboard():
    return jsonify({"msg":"Welcome to the admin dashboard"}), 200


@auth_bp.route('/user-dashboard', methods= ['GET'])
@jwt_required()
@role_required(['user','admin'])
def user_dashboard():
    return jsonify({"msg":"Welcome to the user dashboard"}), 200


    