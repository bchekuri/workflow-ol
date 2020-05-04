import jwt
import logging
from datetime import datetime, timedelta
from core import env_config as config

LOGGER = logging.getLogger(__name__)

def generate_token(data=None):
    payload = {
        'exp': datetime.utcnow() 
            + timedelta(milliseconds=config.get('jwt.expiration_time')),
        'iss': config.get('jwt.issuer'),
        'aud': config.get('jwt.audience'),
        'iat': datetime.utcnow()
    }
    if data:
        payload['data'] = data
    encoded = jwt.encode(payload, 
        config.get('jwt.secret_key'), 
        algorithm=config.get('jwt.algorithm')).decode("utf-8")
    LOGGER.debug('JWT Token %s', encoded)
    return encoded


def decode_token(token):
    if token:
        try:
            return jwt.decode(jwt=token, 
                key=config.get('jwt.secret_key'),
                audience=config.get('jwt.audience'),
                verify=True,
                algorithms=[config.get('jwt.algorithm')])
        except Exception:
            LOGGER.error('JWT Token decode failed!')
            return False