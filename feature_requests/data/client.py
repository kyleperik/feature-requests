from .models import Client, db
from feature_requests import domain
import feature_requests.domain.models

def get_all():
    client = db.session.query(Client).all()
    return [
        domain.models.Client.create(feature)
    for client in clients]
