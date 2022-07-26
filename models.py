"""Models for Blogly."""
from datetime import datetime
from tkinter import CASCADE
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()

def connect_db(app):
  db.app = app
  db.init_app(app)


class User(db.Model):
    __tablename__ = 'users'
    

    id = db.Column(db.Integer,
                   primary_key = True,
                   autoincrement=True)
    first_name = db.Column(db.String(100),
                    nullable= False)
    last_name = db.Column(db.String(100),
                    nullable= False)
    image_url= db.Column(db.String(100),
                    nullable=True, default="https://cdn.pixabay.com/photo/2021/06/07/13/46/user-6318005__340.png")
    posts = db.relationship('Post', backref = 'users', cascade="all, delete-orphan")

class Post(db.Model):
    __tablename__='posts'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.DateTime(), nullable=False,default=datetime.utcnow)
    user_id = db.Column(db.Integer, 
                db.ForeignKey('users.id'), nullable='false')

    

class Tag(db.Model):
  __tablename__='tags' 
  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  name = db.Column(db.Text, unique=True)
  posts = db.relationship('Post', backref = 'tags', secondary='post_tags')
  
  
class PostTag(db.Model):
  __tablename__='post_tags'
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'),primary_key = True)
  tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), primary_key=True)

                    