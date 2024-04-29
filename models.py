import datetime as dt
from flask_sqlalchemy import SQLAlchemy
from utils import load_posts

db = SQLAlchemy()

class Post(db.Model):

    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.String(500), nullable=False)
    create_date = db.Column(db.DateTime, default=dt.datetime.now)
    update_date = db.Column(db.DateTime, default=dt.datetime.now, onupdate=dt.datetime.now)
    comments = db.relationship('Comment', backref='post', lazy=True)

class User(db.Model):

    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(20), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    text = db.Column(db.Text, nullable=False)
    create_date = db.Column(db.DateTime, default=dt.datetime.now, nullable=False)

def populate_post():
    if Post.query.count() == 0:
        posts = load_posts()
        for post_data in posts:
            post = Post(title=post_data['title'], content=post_data['content'])
            db.session.add(post)
        db.session.commit()

def create_admin_user():
    admin = User.query.filter_by(username='admin').first()
    if not admin:
        admin = User(username='admin', password='admin')
        db.session.add(admin)
        db.session.commit()