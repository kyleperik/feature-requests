from feature_requests.data.models import FeatureRequest, db

def get_all():
    features = db.session.query(FeatureRequest).all()
    return [feature.title for feature in features]
