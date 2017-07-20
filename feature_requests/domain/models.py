class FeatureRequest:
    title = ''
    description = ''
    target_date = None

    @classmethod
    def create(cls, feature_request):
        result = cls()
        result.title = feature_request.title
        result.description = feature_request.description
        result.target_date = feature_request.target_date
        return result

    def serialize(self):
        return {
            'title': self.title,
            'description': self.description,
            'target_date': self.target_date
        }
