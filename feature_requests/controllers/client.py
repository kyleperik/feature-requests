from flask import Blueprint, jsonify, request, abort
from feature_requests import facades
from feature_requests import domain
import feature_requests.domain.models
import feature_requests.facades.client

client = Blueprint('client', __name__)

@client.route('/', methods=['GET'])
def GET_ALL():
    return jsonify([
        client.serialize()
    for client in facades.client.get()])
