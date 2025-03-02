from flask import Flask
from user_routers import user_router

app = Flask(__name__)

app.register_blueprint(user_router, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
