from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FeatureRequest(db.Model):
    __tablename__ = 'feature_request'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    description = db.Column(db.String(5000))
    target_date = db.Column(db.DateTime)
    client_id = db.Column(db.Integer, db.ForeignKey('client.id'))
    product_area_id = db.Column(db.Integer, db.ForeignKey('product_area.id'))
    
    client = db.relationship('Client')
    product_area = db.relationship('ProductArea')
    def __init__(self, id=None, title='', description='', target_date=None,
                 client_id=None, product_area_id=None):
        self.id = id
        self.title = title
        self.description = description
        self.target_date = target_date
        self.client_id = client_id
        self.product_area_id = product_area_id

    @classmethod
    def create(cls, entitiy):
        return cls(
            id = entitiy.id,
            title = entitiy.title,
            description = entitiy.description,
            target_date = entitiy.target_date,
            client_id = entitiy.client_id,
            product_area_id = entitiy.product_area_id,
        )

class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    priority = db.Column(db.Integer)
    is_archived = db.Column(db.Boolean)

    def __init__(self, id=None, name='', priority=None, is_archived=None):
        self.id = id
        self.name = name
        self.priority = priority
        self.is_archived = is_archived

    @classmethod
    def create(cls, client):
        return cls(
            id = client.id,
            name = client.name,
            priority = client.priority,
            is_archived = client.is_archived
        )

class ProductArea(db.Model):
    __tablename__ = 'product_area'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))

    def __init__(self, id=None, name=''):
        self.id = id
        self.name = name

    @classmethod
    def create(cls, entitiy):
        return cls(
            id = entitiy.id,
            name = entitiy.name
        )
