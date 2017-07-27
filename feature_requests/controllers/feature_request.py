from flask import Blueprint, jsonify, request
from feature_requests import facades
from feature_requests import domain
import feature_requests.domain.models
import feature_requests.facades.feature_request

feature_request = Blueprint('feature_request', __name__)

@feature_request.route('/', methods=['GET'])
def GET():
    return jsonify([
        feature.serialize()
    for feature in facades.feature_request.get()])

@feature_request.route('/', methods=['POST'])
def POST():
    f = request.get_json()
    return jsonify([
        facades.feature_request.add(
            domain.models.FeatureRequest(
                title = f['title'],
                description = f['description'],
                target_date = f['target_date']
            )
        )
    ])
