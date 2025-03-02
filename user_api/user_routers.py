from flask import Blueprint
from user_controller import add_user, get_all_users, put, delete

user_router = Blueprint('user', __name__)

user_router.route('/users', methods=['POST'])(add_user)

user_router.route('/', methods=['GET'])(get_all_users)

user_router.route('/<int:user_id>', methods=['PUT'])(put)

user_router.route('/<int:user_id>', methods=['DELETE'])(delete)
