"""
Auth Guard
"""
from flask_httpauth import HTTPTokenAuth
from flask import jsonify
import logging
from core import env_config as config
from service import auth_service

LOGGER = logging.getLogger(__name__)

auth = HTTPTokenAuth(scheme=config.get('jwt.scheme'))

@auth.verify_token
def verify_token(token):
    LOGGER.debug('Auth Token - %s', token)
    if token:
        return auth_service.decode_token(token)
    return False


@auth.error_handler
def auth_error(status):
    return jsonify({
        'error_id' : status,
        'developer_text': 'Unauthorized',
        'message' : 'Unauthorized'
    })