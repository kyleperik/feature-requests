from feature_requests import data
import feature_requests.data.client

def get():
    return data.client.get_all()
