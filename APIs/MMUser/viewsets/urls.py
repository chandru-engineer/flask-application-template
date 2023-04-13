from APIs.MMUser import auth_main
from flask import jsonify, request
from APIs.MMUser.model.user_model import User
from APIs import db, app
import jwt
import datetime
from jwt.exceptions import ExpiredSignatureError, InvalidSignatureError
from APIs.authentication import required_auth
from APIs.authorization import authorize

@auth_main.route('/', methods=['POST'])
def hello_auth():
    if request.method == 'POST':
        data = request.get_json()
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return jsonify({'data': "data added successfully!!!"})
    return jsonify({'data': "authendication example"}) 

@auth_main.route('/login', methods=['POST'])
def login():
    try:
        request_data = request.get_json()
        user_data = User.query.filter_by(name=request_data['username']).first()
        if user_data and user_data.password == request_data['password']:
            payload_access = {
                'id': user_data.id,
                "username": user_data.name,
                "email": user_data.email, 
                'Role': "Admin",
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }
            payload_refresh = {
                "username": user_data.name,
                "exp": datetime.datetime.utcnow() + datetime.timedelta(days=30)
            }
            access_token = jwt.encode(payload_access, app.config['SECRET_KEY'], algorithm='HS256')
            refresh_token = jwt.encode(payload_refresh, app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({'access_token': access_token, 'refresh_token': refresh_token})
        else:
            return jsonify({'error': 'Invalid username or password'})
    except Exception as e:
        return jsonify({'error':"Server Not Responding"})

# Step 5: Refresh access token with refresh token
@auth_main.route('/refresh')
def refresh():
    refresh_token = request.headers.get('refresh_token')
    if not refresh_token:
        return {'error': 'Refresh token required'}, 401
    try:
        data = jwt.decode(refresh_token, app.config['SECRET_KEY'], algorithms=['HS256'])
        username = data['username']
        user_data = User.query.filter_by(name=username).first()
        if user_data:
            payload_access = {
                'id': user_data.id,
                "username": user_data.name,
                "email": user_data.email, 
                'Role': "Admin",
                "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
            }
            access_token = jwt.encode(payload_access, app.config['SECRET_KEY'], algorithm='HS256')
            return {'access_token': access_token}
    except ExpiredSignatureError:
        return jsonify({'error': 'Login Required'}), 401
    except InvalidSignatureError:
        return jsonify({'error': 'Invalid refresh token'}), 401
    except:
        return jsonify({'error': 'Server Not responding'}), 500

# Step 4: Protect routes with access token
@auth_main.route('/protected')
@required_auth
@authorize([])
def protected(data):
    return jsonify({'data': data})




    



