from models.user import User
from db.database import db
from flask import jsonify
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token

def register_user(data):
    username = data.get('username')
    if User.query.filter_by(username=username).first():
        return jsonify({"message": "User already exists"}), 400

    new_user = User(
        fullname=data.get('fullname'),
        username=username,
        email=data.get('email'),
        password=generate_password_hash(data.get('password')),
        role=data.get('role', 'user')
    )

    db.session.add(new_user)
    db.session.commit()

    access_token = create_access_token(identity=username)
    return jsonify({"token": access_token}), 201
