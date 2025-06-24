from flask import Blueprint, request
from controllers.auth_controller import register_user

auth_bp = Blueprint('auth_bp', __name__, url_prefix='/auth')

@auth_bp.route('/register', methods=['POST'])
def register():
    return register_user(request.json)
