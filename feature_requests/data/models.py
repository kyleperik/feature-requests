from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class FeatureRequest(db.Model):
    __tablename__ = 'feature_request'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(500))
    description = db.Column(db.String(5000))
    target_date = db.Column(db.DateTime)
    
    def __init__(self, title='', description='', target_date=None):
        self.title = title
        self.description = description
        self.target_date = target_date
