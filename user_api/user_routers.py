from  flask import Blueprint
from user_controller import add_user

user_router= Blueprint('user',__name__)

user_router.route('/users',methods=['POST']) (add_user)


