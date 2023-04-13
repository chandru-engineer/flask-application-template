from flask import request, jsonify
import jwt
from jwt import ExpiredSignatureError, InvalidSignatureError
from APIs import app
from functools import wraps


# This method will validate the Authentication.
def required_auth(req_data):
    @wraps(req_data)
    def decorated(*args, **kwargs):
        token = None
        access_token = request.headers.get('access_token')
        if not access_token:
            return jsonify({'error': 'Access token required'}), 401
        try:
            data = jwt.decode(access_token, app.config['SECRET_KEY'],verify=True, algorithms=['HS256'])
        except ExpiredSignatureError:
            return jsonify({'error': 'access token expried'}), 401
        except InvalidSignatureError:
            return jsonify({'error': 'Invalid refresh token'}), 401
        except:
            return jsonify({'error': 'Server Not responding'}), 500
        return req_data(data, *args, **kwargs)
    return decorated


