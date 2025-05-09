
from flask import jsonify
from .models import User
from functools import wraps
from flask_jwt_extended import get_jwt_identity

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_user_id = get_jwt_identity()
        user = User.query.get(current_user_id)
        if not user or user.role != 'admin':
            return jsonify({"message": "Admin Access Required"}), 403
        return f(*args, **kwargs)
    return decorated_function

