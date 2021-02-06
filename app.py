from flask import Flask, jsonify, request, make_response
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token, get_jwt_identity)
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
import datetime

# Config Connect database and Flask
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:123@localhost:5432/User"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = 'secret'

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)


# ORM class to databse table
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), index=True)
    password = db.Column(db.String(128))

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def verify_password(self, password):
        return check_password_hash(self.password, password)


# Expired access token
@jwt.expired_token_loader
def my_expired_token_callback(expired_token):
    token_type = expired_token['type']
    return jsonify({
        'status': 401,
        'message': 'The {} token has expired'.format(token_type)
    }), 401


# Login witch Json Body Username and password
@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username:
        return jsonify({"message": "Missing username"}), 400
    if not password:
        return jsonify({"message": "Missing password"}), 400

    user = User.query.filter_by(username=username).first()

    if user is None:
        return jsonify({"message": "Bad username or password"}), 401

    if user.verify_password(password):
        # Token have 15 minutes validity to access
        expires = datetime.timedelta(minutes=15)
        access_token = create_access_token(username, expires_delta=expires)
        return jsonify(token=access_token), 200

    return jsonify({"message": "Bad password"}), 401


# Register witch username and password
@app.route('/register', methods=['POST'])
def register():
    if not request.is_json:
        return jsonify({"message": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        return jsonify({"message": "Missing username"}), 400
    if not password:
        return jsonify({"message": "Missing password"}), 400
    if User.query.filter_by(username=username).first() is not None:
        return jsonify({"message": "User exist !!!"}), 400

    new_user = User(username, generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "Succes add user"}), 201


# Endpoint protected access token
@app.route('/protected', methods=['GET'])
@jwt_required
def protected():
    current_user = get_jwt_identity()
    return jsonify(user_name=current_user), 200


# Endpoint to check whether server is run
@app.route('/', methods=['GET'])
def hello():
    return jsonify("Hello World"), 200


if __name__ == '__main__':
    app.run()
