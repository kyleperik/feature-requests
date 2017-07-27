from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FeatureRequest(db.Model):
    __tablename__ = 'feature_request'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    description = db.Column(db.String(5000))
    target_date = db.Column(db.DateTime)
    
    def __init__(self, id=None, title='', description='', target_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.target_date = target_date

    @classmethod
    def create(cls, feature):
        return cls(
            id = feature.id,
            title = feature.title,
            description = feature.description,
            target_date = feature.target_date
        )
