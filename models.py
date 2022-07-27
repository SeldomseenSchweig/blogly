"""Models for Blogly."""
from datetime import datetime
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
    # I don't know why users are allowed to have blank name if they are not allowed to be null
                    nullable= False)
    last_name = db.Column(db.String(100),
                    nullable= False)
    image_url= db.Column(db.String(100),
    # I don't know why this doesn't give a default image to a user who doesn't choose an image
                    nullable=True, default="https://cdn.pixabay.com/photo/2021/06/07/13/46/user-6318005__340.png")

class Post(db.Model):
    __tablename__='posts'
    

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
    date_time = db.Column(db.DateTime, nullable=False,default=datetime.utcnow)
    user_id = db.Column(db.Integer, 
                db.ForeignKey('users.id'))
    users = db.relationship('User', backref = 'posts')


                    