from flask import Blueprint, jsonify
from feature_requests import facades
import feature_requests.facades.feature_request


feature_request = Blueprint('feature_request', __name__)

@feature_request.route('/', methods=['GET'])
def GET():
    return jsonify(facades.feature_request.get())
