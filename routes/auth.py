from flask import jsonify
from . import routes
from service import auth_service
from core import env_config as config

@routes.route('/api/v1/auth/token', methods=['POST'])
def index():
    return jsonify({
        'token' : auth_service.generate_token(None),
        "token_type": config.get('jwt.scheme'),
        "expires": config.get('jwt.expiration_time')
    })