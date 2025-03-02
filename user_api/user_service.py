from db_connector import get_db_connection
from mysql.connector import Error
from flask import jsonify


def get_users():
    connection = get_db_connection()
    if connection is None:
        return {"error": "Failed to connect to the database"}
    cursor = connection.cursor()
    try:
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        return jsonify(users)
    except Error as e:
        return {"error": f"An error occurred: {str(e)}"}
    finally:
        cursor.close()
        connection.close()


def update_user(user_id, name):
    connection = get_db_connection()
    if connection is None:
        return {"error": "Failed to connect to the database"}

    cursor = connection.cursor()
    try:
        query = 'UPDATE users SET user_name = %s WHERE user_id= %s'
        value = (name, user_id)
        cursor.execute(query, value)
        connection.commit()

        if cursor.rowcount > 0:
            return jsonify({"message": "User updated successfully!"}), 200
        else:
            return jsonify({"message": "User not found!"}), 404

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        cursor.close()
        connection.close()


def create_user(user_name):
    connection = get_db_connection()
    if connection is None:
        return {"error": "Failed to connect to the database"}
    cursor = connection.cursor()
    try:
        query = 'INSERT INTO users (user_name) VALUES (%s)'

        cursor.execute(query, (user_name,))
        connection.commit()
        return {"message": "User created successfully"}


    except Error as e:
        return {"error": f"An error occurred: {str(e)}"}

    finally:
        cursor.close()
        connection.close()
