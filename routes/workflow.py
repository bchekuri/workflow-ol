from flask import jsonify
from . import routes
from core.auth_guard import auth


@routes.route('/api/v1/workflow', methods=['POST'])
@auth.login_required
def create_workflow():
    return jsonify({
        'status' : 200
    })