from flask import Flask
from flask_cors import CORS
from user_routers import user_router

app = Flask(__name__)
CORS(app)

app.register_blueprint(user_router, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
