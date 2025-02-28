from db_connector import get_db_connection
from mysql.connector import Error


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
