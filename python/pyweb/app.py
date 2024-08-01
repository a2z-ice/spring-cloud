import logging
import os

from flask import Flask
from waitress import serve

import home
from error.http_error_handler import handle_exception
from home.home_controller import home_blueprint

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

app.errorhandler(Exception)(handle_exception)
app.register_blueprint(home_blueprint)

if __name__ == '__main__':
    env = os.environ.get('ENVIRONMENT', 'dev')
    if env == 'dev':
        app.run(debug=True, host='0.0.0.0')
    else:
        serve(app, host='0.0.0.0', port=5000)

