from flask import Flask, g, jsonify
import logging
from core import app_logger
from core import auth_guard
from core import env_config as config
from routes import routes

LOGGER = logging.getLogger(__name__)

# Setup application logging
app_logger.setup_logging()

app = Flask(__name__)

app.register_blueprint(routes)


if __name__ == '__main__':
    LOGGER.info('Application "%s" about to bootstrap', config.get('app_name1'))
    app.run(host='0.0.0.0')