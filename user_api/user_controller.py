from flask import request, jsonify
from user_service import create_user


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
