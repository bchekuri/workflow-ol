"""
    Reading environment config
"""
import os
from jsonmerge import merge
import json
import sys
import logging

_DEFAULT_ENV_CONFIG_FILE_DIR = 'resource'
_DEFAULT_ENV_CONFIG_FILE = 'default.json'

LOGGER = logging.getLogger(__name__)

def read_env_config():
    """
    Read environment specific config file
    """
    try:
        default_config_data = {}
        default_config_file_name = os.path.join(os.getcwd(), 
            _DEFAULT_ENV_CONFIG_FILE_DIR, 
            _DEFAULT_ENV_CONFIG_FILE)
        if os.path.exists(default_config_file_name):
            with open(default_config_file_name, 'r') as default_file:
                default_config_data = json.loads(default_file.read())
        env_specific_config_data = {}    
        if os.environ.get('ENV'):
            file_name = os.path.join(os.getcwd(), 
                _DEFAULT_ENV_CONFIG_FILE_DIR, 
                ('%s.%s' % (os.environ.get('ENV'), 'json')))
            if os.path.exists(file_name):
                with open(file_name, 'r') as env_specific_file:
                    env_specific_config_data = json.loads(env_specific_file.read())       
        config_data = merge(default_config_data, env_specific_config_data)
        return config_data
    except json.JSONDecodeError as jde:
        LOGGER.error('Invalid JSON environment config file!; %s', jde.msg)
        raise jde
    except FileNotFoundError:
        LOGGER.warn('Environment config file missing!')
        pass
    except:
        LOGGER.error('Unexpected error %s', sys.exc_info()[0])



_APP_ENV_CONFIG = None

if _APP_ENV_CONFIG is None:
    LOGGER.info('Init app environment config')
    _APP_ENV_CONFIG = read_env_config()


def get_config(config, keys, index):
    try:
        if isinstance(config, dict) and keys is not None and (index >= 0 and index < len(keys)):
            if index == len(keys) - 1:
                return config.get(keys[index])
            else:
                return get_config(config.get(keys[index]), keys, (index + 1))
    except KeyError:
        LOGGER.debug('Environment config %s missing!', keys[index])


def get(key):
    if key:
        key_array = key.split('.')
        return get_config(_APP_ENV_CONFIG, key_array, 0)