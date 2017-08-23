from feature_requests import data
import feature_requests.data.client

def get():
    return data.client.get_all()

def _save_all(updated_clients):
    existing_clients = get()
    for updated_client in updated_clients:
        existing_client = next(
            (c for c in existing_clients if c.id == updated_client.id), None
        )
        if existing_client == None:
            yield data.client.add(updated_client)
        else:
            data.client.update(updated_client)
            yield existing_client.id

def save_all(updated_clients):
    return list(_save_all(updated_clients))
        
