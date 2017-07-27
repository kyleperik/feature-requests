class FeatureRequest:
    id = None
    title = ''
    description = ''
    target_date = None

    def __init__(self, id=None, title='',
                 description='', target_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.target_date = target_date
    
    @classmethod
    def create(cls, feature_request):
        result = cls()
        result.id = feature_request.id
        result.title = feature_request.title
        result.description = feature_request.description
        result.target_date = feature_request.target_date
        return result

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'target_date': self.target_date
        }
