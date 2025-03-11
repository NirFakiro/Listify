from flask import Flask
from flask_cors import CORS
from user_routers import user_router
import os
import signal



app = Flask(__name__)
CORS(app)

@app.route('/stop_server')
def stop_server():
 os.kill(os.getpid(), signal.CTRL_C_EVENT)
 return 'Server stopped'

app.register_blueprint(user_router, url_prefix='/api')

if __name__ == '__main__':
    app.run(debug=True)
