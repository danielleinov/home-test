from threading import Thread

import json_logging
from flask import Flask

from app.routes import *
from app.models import *


def create_app():
    app = Flask(__name__)
    json_logging.ENABLE_JSON_LOGGING = True
    json_logging.init_flask()
    json_logging.init_request_instrument(app)
    app.register_blueprint(main_route, url_prefix='/')
    
    # Consume messages from kafka in background
    Thread(target=customer.consume_write_mongo).start()
    return app
