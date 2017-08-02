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

    def __init__(self, id=None, title='', description='', target_date=None,
                 client_id=None):
        self.id = id
        self.title = title
        self.description = description
        self.target_date = target_date
        self.client_id = client_id

    @classmethod
    def create(cls, feature):
        return cls(
            id = feature.id,
            title = feature.title,
            description = feature.description,
            target_date = feature.target_date,
            client_id = feature.client_id
        )

class Client(db.Model):
    __tablename__ = 'client'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(500))
    priority = db.Column(db.Integer)

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
