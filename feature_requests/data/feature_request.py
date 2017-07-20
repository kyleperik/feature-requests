from feature_requests.data.models import FeatureRequest, db
from feature_requests import domain
import feature_requests.domain.models

def get_all():
    features = db.session.query(FeatureRequest).all()
    return [
        domain.models.FeatureRequest.create(feature)
    for feature in features]
