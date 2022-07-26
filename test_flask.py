from unittest import TestCase

from app import app
from models import db, User

# Use test database and don't clutter tests with SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///user_test_db'
app.config['SQLALCHEMY_ECHO'] = False

# Make Flask errors be real errors, rather than HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()


class UserViewsTestCase(TestCase):
    """Tests for views for Users."""

    def setUp(self):
        """Add sample User."""

        User.query.delete()

        user = User(first_name="test", last_name="testerino", image_url='https://cdn.pixabay.com/photo/2016/09/14/23/06/poznan-1670738__340.jpg')
        db.session.add(user)
        db.session.commit()

        self.User_id = user.id

    def tearDown(self):
        """Clean up any fouled transaction."""

        db.session.rollback()

    def test_list_Users(self):
        """tests the list of users"""
        with app.test_client() as client:
            
            resp = client.get("/", follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('test', html)

    def test_show_User(self):
        """tests showing a particular user's page"""
        with app.test_client() as client:
            resp = client.get(f"/{self.User_id}")
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn('<h2>test  testerino</h2>', html)

    def test_add_User(self):
        """ tests adding a new user"""
        with app.test_client() as client:
            d = {"firstname": "test2", "lastname": "testerino", "image": 'https://cdn.pixabay.com/photo/2016/09/14/23/06/poznan-1670738__340.jpg'}
            resp = client.post("/", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("<li> test2 testerino</li>", html)

    def test_delete_user(self):
        """tests deleting user """
        with app.test_client() as client:
            d = {"id": "1"}
            resp = client.post("/users", data=d, follow_redirects=True)
            html = resp.get_data(as_text=True)
            self.assertNotIn("<li> test2 testerino</li>", html)


