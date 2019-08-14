from sqlalchemy.orm import validates
from app import db

class Alias(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    alias = db.Column(db.String(20), index=True, unique=True, nullable=False)
    target = db.Column(db.String(128), index=True, nullable=False)

    @validates('target')
    def validate_target(self, key, target):
        assert 'http' in target
        return target

    def __repr__(self):
        return f'<Alias {self.alias}>'
