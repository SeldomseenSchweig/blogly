"""Seed file to make sample data for Users db."""

from models import User, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()


# Add pets
Tim = User(first_name='Tim', last_name="tebow", image_url="https://cdn.pixabay.com/photo/2018/11/17/22/57/dog-3822183__340.jpg")
Mary = User(first_name='Mary', last_name="Ann", image_url="https://cdn.pixabay.com/photo/2015/09/22/21/35/woman-952506__340.jpg")
Sue = User(first_name='Sue', last_name="kaine", image_url="https://cdn.pixabay.com/photo/2015/05/03/14/40/woman-751236__340.jpg")

# Add new objects to session, so they'll persist
db.session.add(Tim)
db.session.add(Mary)
db.session.add(Sue)

# Commit--otherwise, this never gets saved!
db.session.commit()