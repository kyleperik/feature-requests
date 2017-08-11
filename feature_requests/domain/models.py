class FeatureRequest:
    def __init__(self, id=None, title='',
                 description='', target_date=None,
                 client_id=None):
        self.id = id
        self.title = title
        self.description = description
        self.target_date = target_date
        self.client_id = client_id

    @classmethod
    def create(cls, feature_request):
        return cls(
            id = feature_request.id,
            title = feature_request.title,
            description = feature_request.description,
            target_date = feature_request.target_date,
            client_id = feature_request.client_id
        )

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'target_date': self.target_date,
            'client_id': self.client_id
        }

class Client:
    def __init__(self, id=None, name='', priority=None):
        self.id = id
        self.name = name
        self.priority = priority

    @classmethod
    def create(cls, client):
        return cls(
            id = client.id,
            name = client.name,
            priority = client.priority
        )

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'priority': self.priority
        }
