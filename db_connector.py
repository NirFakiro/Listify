import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()
db_password = os.getenv("DB_PASSWORD")


def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password=db_password,
            database='users_db',
            port=3307

        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
