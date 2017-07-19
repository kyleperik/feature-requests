from feature_requests import data
import feature_requests.data.feature_request

def get():
    return data.feature_request.get_all()
