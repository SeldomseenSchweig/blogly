from unittest import TestCase

from app import app
from models import db, User

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

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_first_name(self):
        user = User(first_name="John", last_name="jacob jingelheimerschmidht", image_url='https://cdn.pixabay.com/photo/2022/03/16/01/23/bird-7071408__340.jpg')
        self.assertEquals(user.first_name, "John")

    def test_id(self):
        user = User(first_name="Test", last_name="testerino", image_url='https://cdn.pixabay.com/photo/2022/03/16/01/23/bird-7071408__340.jpg' )
        self.assertEquals(user.id, 1)
        

