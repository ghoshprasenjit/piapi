from datetime import datetime
from app import db
from app.user.model import User


class Post(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable = False)
    date_posted = db.Column(db.DateTime, nullable = False, default = datetime.now)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    

    def __repr__(self):
        return f"User({self.title}, {self.date_posted})"

