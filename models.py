from app import db
from sqlalchemy.dialects.postgresql import JSON


class Scores(db.Model):
    __tablename__ = 'scores'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(20))
    scores = db.Column(JSON)
    timestamp = db.Column(db.DateTime)

    def __init__(self, user_id, scores, timestamp):
        self.user_id = user_id
        self.scores = scores
        self.timestamp = timestamp

    def __repr__(self):
        return '<id {}>'.format(self.id)
