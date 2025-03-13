from flask import request, jsonify
from user_api.user_service  import create_user, get_users, update_user, delete_user


def get_all_users():
    try:
        users = get_users()
        if not users:
            return jsonify({"message": "No users found"}), 404
        return users
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def add_user():
    try:
        data = request.get_json()
        user_name = data.get('user_name')

        if not user_name:
            return jsonify({"error": "user_name is required"}), 400

        result = create_user(user_name)

        if 'error' in result:
            return jsonify(result), 500

        return jsonify(result), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def put(user_id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    user_name = data.get('user_name')
    if not user_name:
        return jsonify({"error": "User name is required"}), 400
    try:
        update = update_user(user_id,user_name)
        return update
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete(user_id):
    try:
        return delete_user(user_id)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


