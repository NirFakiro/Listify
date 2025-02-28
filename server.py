from flask import Flask, jsonify
from db_connector import get_db_connection

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'we just start!'


@app.route('/users', methods=['GET'])
def get_users():
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    cursor.close()
    connection.close()

    return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)
