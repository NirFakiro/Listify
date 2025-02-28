from flask import Flask, jsonify
from user_routers import user_router


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'we just start!'

app.register_blueprint(user_router, url_prefix='/api')
# @app.route('/users', methods=['GET'])
# def get_users():
#     connection = get_db_connection()
#     cursor = connection.cursor()
#
#     cursor.execute('SELECT * FROM users')
#     users = cursor.fetchall()
#     cursor.close()
#     connection.close()
#
#     return jsonify(users)


if __name__ == '__main__':
    app.run(debug=True)
