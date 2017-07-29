from feature_requests import data
import feature_requests.data.feature_request

def get(id=None):
    if id is not None:
        return data.feature_request.get(id)
    return data.feature_request.get_all()

def add(f):
    return data.feature_request.add(f)
