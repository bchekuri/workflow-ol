from flask import Blueprint
routes = Blueprint('workflow-ol', __name__)

from .auth import *
from .workflow import *