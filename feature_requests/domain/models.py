class FeatureRequest:
    def __init__(self, id=None, title='',
                 description='', target_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.target_date = target_date
    
    @classmethod
    def create(cls, feature_request):
        return cls(
            id = featrue_request.id,
            title = feature_request.title,
            description = feature_request.description,
            target_date = feature_request.target_date
        )

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'target_date': self.target_date
        }

class Client:
    def __init__(self, id=None, name='', priority=None):
        self.id = id
        self.title = title
        self.description = description
        self.target_date = target_date

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
