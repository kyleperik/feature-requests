from .models import Client, db
from feature_requests import domain
import feature_requests.domain.models

def get_all():
    clients = db.session.query(Client).order_by(Client.priority).all()
    return [
        domain.models.Client.create(client)
    for client in clients]
