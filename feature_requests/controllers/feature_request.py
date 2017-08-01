from flask import Blueprint, jsonify, request, abort
from feature_requests import facades
from feature_requests import domain
import feature_requests.domain.models
import feature_requests.facades.feature_request

feature_request = Blueprint('feature_request', __name__)

@feature_request.route('/', methods=['GET'])
def GET_ALL():
    return jsonify([
        feature.serialize()
    for feature in facades.feature_request.get()])

@feature_request.route('/<int:id>', methods=['GET'])
def GET(id):
    result = facades.feature_request.get(id)
    if result is None: abort(404)
    return jsonify(
        result.serialize()
    )

@feature_request.route('/', methods=['POST'])
def POST():
    f = request.get_json()
    return jsonify(
        facades.feature_request.add(
            domain.models.FeatureRequest(
                title = f['title'],
                description = f['description'],
                target_date = f['target_date']
            )
        )
    )

@feature_request.route('/<int:id>', methods=['PATCH'])
def PATCH(id):
    f = request.get_json()
    return jsonify(
        facades.feature_request.update(
            id,
            domain.models.FeatureRequest(
                title = f['title'],
                description = f['description'],
                target_date = f['target_date']
            )
        )
    )

@feature_request.route('/<int:id>', methods=['DELETE'])
def DELETE(id):
    return jsonify(facades.feature_request.delete(id))
