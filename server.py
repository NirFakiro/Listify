from flask import Flask, send_from_directory
from flask_cors import CORS
from user_api.user_routers import user_router
import os
import signal



app = Flask(__name__, static_folder='./public', static_url_path='/')
CORS(app)

@app.route('/')
def serve_react():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/stop_server')
def stop_server():
 os.kill(os.getpid(), signal.CTRL_C_EVENT)
 return 'Server stopped'

app.register_blueprint(user_router, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
