from flask import jsonify, request
from . import routes
from service import auth_service
from core import env_config as config

@routes.route('/api/v1/auth/token', methods=['POST'])
def auth_token():
    return jsonify({
        'token' : auth_service.generate_token(None),
        "token_type": config.get('jwt.scheme'),
        "expires": config.get('jwt.expiration_time')
    })


@routes.route('/api/v1/job/<int:jobId>/token', methods=['POST'])
def job_action_token(jobId):
    if not request.json:
        return jsonify({
            'message' : 'Invalid Request!'
        }),400
    return jsonify({
        'token' : auth_service.generate_token(None),
        "token_type": config.get('jwt.scheme'),
        "expires": config.get('jwt.expiration_time')
    })