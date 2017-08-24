from .models import ProductArea, db
from feature_requests import domain
import feature_requests.domain.models

def get_all():
    product_areas = db.session.query(ProductArea).all()
    return [
        domain.models.ProductArea.create(product_area)
        for product_area in product_areas]
