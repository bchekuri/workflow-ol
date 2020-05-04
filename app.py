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

@app.errorhandler(Exception)
def error_handler(e):
    return jsonify({
        'error_id' : 500,
        'developer_text': 'Internal Server Error!',
        'message' : 'Internal Server Error!'
    }), 500


if __name__ == '__main__':
    LOGGER.info('Application "%s" about to bootstrap', config.get('app_name1'))
    app.run(host='0.0.0.0')