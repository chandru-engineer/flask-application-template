from flask import jsonify, request
import jwt
from jwt import ExpiredSignatureError, InvalidSignatureError
from APIs import app
from functools import wraps


# This method will validate the Authorization.
def authorize(roles):
    def authorize_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            access_token = request.headers.get('access_token')
            if not access_token:
                return jsonify({'error': 'Access token required'}), 401
            try:
                data = jwt.decode(access_token, app.config['SECRET_KEY'], verify=True, algorithms=['HS256'])
                user_role = data['Role']
            except Exception as e:
                return jsonify({'error': str(e)}), 401
            if user_role == []:
                return wrapper
            if user_role not in roles:
                return jsonify({'error': 'Unauthorized access'}), 401
            return func(*args, **kwargs)
        return wrapper
    return authorize_decorator