class FeatureRequest:
    def __init__(self, id=None, title='',
                 description='', target_date=None,
                 client_id=None, product_area_id=None):
        self.id = id
        self.title = title
        self.description = description
        self.target_date = target_date
        self.client_id = client_id
        self.product_area_id = product_area_id

    @classmethod
    def create(cls, entity):
        return cls(
            id = entity.id,
            title = entity.title,
            description = entity.description,
            target_date = entity.target_date,
            client_id = entity.client_id,
            product_area_id = entity.product_area_id,
        )

    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'target_date': self.target_date,
            'client_id': self.client_id,
            'product_area_id': self.product_area_id,
        }

class Client:
    def __init__(self, id=None, name='', priority=None, is_archived=None):
        self.id = id
        self.name = name
        self.priority = priority
        self.is_archived = is_archived

    @classmethod
    def create(cls, entity):
        return cls(
            id = entity.id,
            name = entity.name,
            priority = entity.priority,
            is_archived = entity.is_archived,
        )

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'priority': self.priority,
            'is_archived': self.is_archived,
        }

class ProductArea:
    def __init__(self, id=None, name=''):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, entity):
        return cls(
            id = entity.id,
            name = entity.name,
        )

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }
