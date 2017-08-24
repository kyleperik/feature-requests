from flask import Blueprint, jsonify, request, abort
from feature_requests import facades
from feature_requests import domain
import feature_requests.domain.models
import feature_requests.facades.product_area

product_area = Blueprint('product_area', __name__)

@product_area.route('/', methods=['GET'])
def GET_ALL():
    return jsonify([
        product_area.serialize()
    for product_area in facades.product_area.get()])
