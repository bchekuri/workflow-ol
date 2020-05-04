import logging
import os
from logging.handlers import RotatingFileHandler
import urllib3
import errno

LOGGER = logging.getLogger(__name__)

DEFAULT_LOG_NAME = 'app.log'
DEFAULT_LOG_LEVEL = 'DEBUG'

def mkdir_c(path):
    """ Trying to create log directory """
    try:
        os.makedirs(path, exist_ok=True)
    except TypeError:
        try:
            os.makedirs(path)
        except OSError as ose:
            if ose.errno == errno.EEXIST and os.path.isdir(path):
                pass
            else:
                LOGGER.error('Log directory creation failed!')
                raise



def setup_logging():
    """
    Setup application logger
    """
    urllib3.disable_warnings()

    # Set the logger formatter
    log_formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s():%(lineno)s] "
        "[Thread:%(thread)d] %(message)s", "%d/%m/%y %H:%M:%S")

    # Get the log directory
    log_directory = os.getcwd()
    if os.environ.get('LOG_DIR'):
        log_directory = os.environ.get('LOG_DIR')
    
    # Create log directory if not present
    mkdir_c(log_directory)

    # set log file name
    file_name = DEFAULT_LOG_NAME
    if os.environ.get('LOG_NAME'):
        file_name = os.environ.get('LOG_NAME')

    # Set log Level
    log_level = DEFAULT_LOG_LEVEL
    if os.environ.get('LOG_LEVE'):
        log_level = os.environ.get('LOG_LEVE')

    # Setup logger
    file_handler = RotatingFileHandler(
        os.path.join(log_directory, file_name), maxBytes=9000000, backupCount=3)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(log_formatter)
    file_handler.setFormatter(log_formatter)
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.addHandler(file_handler)
    root_logger.addHandler(stream_handler)

    LOGGER.info('Logger setup complete.')
    