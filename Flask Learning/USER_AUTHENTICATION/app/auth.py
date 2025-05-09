from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from . import db
from .models import User

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods = ['POST'])
def register_user():
    data = request.json
    
    if User.query.filter_by(username = data['username']).first():
        return jsonify ({"message": "Username Already Exist"}), 400
    
    hashed_password = generate_password_hash(data['password'], method= 'pbkdf2:sha256')
    new_user = User(username= data['username'], password = hashed_password)
    
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify ({"message":"User Added Successfully"})


@auth_bp.route('/login', methods = ['POST'])
def login():
    data = request.json
    user = User.query.filter_by( username = data['username']).first()
    
    if not user:
        return jsonify({"message": "no user"})
    
    if check_password_hash(user.password, data['password']):
        access_token = create_access_token(identity= str(user.id))
        return jsonify(access_token = access_token), 400
    
    return jsonify({"Message": "Invalid Credentials"}), 401


@auth_bp.route('/profile', methods = ['GET'])
@jwt_required()
def profile():
    current_user_identity = get_jwt_identity()
    user = User.query.get(current_user_identity)
    return jsonify (username = user.username),200