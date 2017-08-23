from .models import Client, db
from feature_requests import domain
import feature_requests.domain.models

def get_all():
    clients = db.session.query(Client).order_by(Client.priority).all()
    return [
        domain.models.Client.create(client)
    for client in clients]

def update(updated_client):
    client = (db.session.query(Client)
              .filter(Client.id == updated_client.id)).first()
    client.name = updated_client.name
    client.priority = updated_client.priority
    client.is_archived = updated_client.is_archived
    db.session.commit()

def add(new_client):
    client = Client.create(new_client)
    db.session.add(client)
    db.session.flush()
    id = client.id
    db.session.commit()
    return id

