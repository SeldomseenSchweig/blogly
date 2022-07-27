"""Seed file to make sample data for Users db."""

from models import User, db, Post
from app import app
from datetime import datetime

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
User.query.delete()
Post.query.delete()


# Add users
Tim = User(first_name='Tim', last_name="tebow", image_url="https://cdn.pixabay.com/photo/2018/11/17/22/57/dog-3822183__340.jpg")
Mary = User(first_name='Mary', last_name="Ann", image_url="https://cdn.pixabay.com/photo/2015/09/22/21/35/woman-952506__340.jpg")
Sue = User(first_name='Sue', last_name="kaine", image_url="https://cdn.pixabay.com/photo/2015/05/03/14/40/woman-751236__340.jpg")




# Add new objects to session, so they'll persist
db.session.add(Tim)
db.session.add(Mary)
db.session.add(Sue)

db.session.commit()
# Add posts

post_1 = Post(title = "Cicero says" ,content="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum!", user_id = 1)
post_2 = Post(title = "Poppy Cock!" ,content="Cras eu enim arcu. Nulla quis porta elit. Nulla tristique ullamcorper odio et tempus. Aliquam sodales massa eget libero mollis, vitae gravida leo tempor. Mauris aliquam risus sed vehicula sodales. Aenean at posuere eros. Integer quam tellus, volutpat vel pretium nec, semper in nibh. Curabitur ac enim vel odio ullamcorper facilisis. Vestibulum volutpat nulla mi, lacinia ultrices nisi pharetra et. Curabitur scelerisque volutpat cursus. Donec fringilla dui magna, ac blandit lectus tristique non.!", user_id = 2)
post_3 = Post(title = "Rubish!" ,content="Aliquam faucibus vulputate iaculis. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos. Nullam ac aliquam justo. Fusce et lorem hendrerit, aliquam lorem et, tempor odio. Mauris pellentesque in nibh a auctor. Cras faucibus lorem eget nisl interdum accumsan. Aenean condimentum venenatis nulla, eget vehicula lectus fermentum sed. Nulla in lectus sit amet quam euismod rutrum. Pellentesque sit amet arcu eget nibh consectetur volutpat id at tortor. Aliquam ac eros nunc. Donec pretium arcu sed turpis congue ultricies. Morbi laoreet ultrices !", user_id = 1)
db.session.add(post_1)
db.session.add(post_2)
db.session.add(post_3)

# Commit--otherwise, this never gets saved!
db.session.commit()