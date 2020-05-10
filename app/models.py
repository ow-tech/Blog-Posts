from . import db, login_manager
from datetime import datetime
from datetime import datetime
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
class Quote:
    '''
    Quote class to define Quote Objects
    '''
    def __init__(self, author, quote):
        self.author = author
        self.quote = quote

class User (db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), unique = True, nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(60), nullable = False)
    posts = db.relationship('Post', backref='author', lazy= True)
    comments = db.relationship('Comment', backref='author', lazy=True)

    def __repr__(self):
        return f'User ("{self.username}","{self.email}")'

class Post (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)


    def __repr__(self):
        return f'Post ("{self.title}")'

class Comment (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date_posted = db.Column(db.DateTime, nullable = False, default= datetime.utcnow)
    content = db.Column(db.Text, nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

    def __repr__(self):
        return f'Comment ("{self.content}")'