from flask import jsonify, render_template, request
import logging
from . import routes
from service import auth_service
from core import env_config as config


LOGGER = logging.getLogger(__name__)


@routes.route('/api/v1/job/<int:jobId>/approve', methods=['GET'])
def approve(jobId):
     token = request.args.get('_token')
     emailId = request.args.get('_emailId')
     LOGGER.debug("Approval Request started with token: %s, jobId: %s, submitter: %s", token, jobId, emailId)
     if token is None or len(token) == 0 or emailId is None or len(emailId) == 0:
            return render_template('error_view.html', message="Invalid Request!")
     return render_template('approve_view.html')