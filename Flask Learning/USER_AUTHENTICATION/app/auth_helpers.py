
from flask import jsonify
from .models import User
from functools import wraps
from flask_jwt_extended import get_jwt_identity


def role_required(*roles):
    def wrapper(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            curreny_user_id = get_jwt_identity()
            user = User.query.get(curreny_user_id)
            if not user or user.role not in roles:
                return jsonify({"message": "Access Denied: Not sufficient persmission"}),403
            return f(*args, **kwargs)
        return decorated_function
    return wrapper

