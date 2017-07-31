from .models import FeatureRequest, db
from feature_requests import domain
import feature_requests.domain.models

def get_all():
    features = db.session.query(FeatureRequest).all()
    return [
        domain.models.FeatureRequest.create(feature)
    for feature in features]

def get(id):
    feature = (db.session.query(FeatureRequest)
               .filter(FeatureRequest.id == id)
               .first())
    if feature is None: return None
    return domain.models.FeatureRequest.create(feature)

def add(feature):
    new_feature = FeatureRequest.create(feature)
    db.session.add(new_feature)
    db.session.flush();
    id = new_feature.id
    db.session.commit()
    return id

def update(id, f):
    feature = (db.session.query(FeatureRequest)
               .filter(FeatureRequest.id == id)
               .first())
    feature.title = f.title
    feature.description = f.description
    feature.target_date = f.target_date
    return db.session.commit()
