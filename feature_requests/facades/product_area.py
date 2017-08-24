from feature_requests import data
import feature_requests.data.product_area

def get():
    return data.product_area.get_all()
        
