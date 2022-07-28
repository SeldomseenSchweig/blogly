from unittest import TestCase

from app import app
from models import db, User, Post

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///user_test_db'
app.config['SQLALCHEMY_ECHO'] = False

db.drop_all()
db.create_all()


class UerModelTestCase(TestCase):
    """Tests for model for User."""

    def setUp(self):
        """Clean up any existing users."""

        User.query.delete()
        Post.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_first_name(self):
        user = User(first_name="John", last_name="jacob jingelheimerschmidht", image_url='https://cdn.pixabay.com/photo/2022/03/16/01/23/bird-7071408__340.jpg')
        self.assertEqual(user.first_name, "John")

    def test_id(self):
        user2 = User(first_name="Test", last_name="testerino", image_url='https://cdn.pixabay.com/photo/2022/03/16/01/23/bird-7071408__340.jpg' )
        self.assertEqual(user2.last_name, "testerino")

    def test_database(self):
        user2 = User(first_name="Test", last_name="testerino", image_url='https://cdn.pixabay.com/photo/2022/03/16/01/23/bird-7071408__340.jpg' )
        user1 = User(first_name="John", last_name="jacob jingelheimerschmidht", image_url='https://cdn.pixabay.com/photo/2022/03/16/01/23/bird-7071408__340.jpg')
        db.session.add(user1)
        db.session.add(user2)
        db.session.commit()
        first_user = User.query.get(1)
        self.assertEqual(first_user.first_name,"John" )


    def test_post_title(self):
        """tests post title"""
        post1 = Post(title="bleh", content="my first blag post", user_id=2)
        self.assertEqual(post1.title, "bleh")   
    
    def test_post_id(self):
        """tests post id"""
        post2 = Post(title="bleh", content="my second blag post", user_id =1)
        self.assertEqual(post2.user_id, 1)
       

    def test_post_database(self):
        user1 = User.query.get(1)
        post1 = Post(title="bleh", content="my first blag post", user_id=user1.id)
        db.session.add(post1)
        db.session.commit()
        user2 = User.query.get(2)
        post2 = Post(title="bleh", content="my second blag post", user_id =user2.id)
        db.session.add(post2)
        db.session.commit()
        first_post = Post.query.get(1)
        second_post = Post.query.get(2)

        self.assertEqual(first_post.user_id,1)
        self.assertEqual(second_post.title,"bleh")

