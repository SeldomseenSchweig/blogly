"""Blogly application."""


from crypt import methods
from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, User
from utilities import is_empty, make_user


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///users'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "SECRET!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

@app.route('/')
def user_list():
    """ home page, redirects to list of users"""
    return redirect('/users')

@app.route('/users')
def list_of_users():
    """ Gives a list of users"""
    users = User.query.all()
    return render_template('list.html', users=users)


@app.route('/users/new')
def add_user_form():
    """ shows the page where user can edit a profile"""
    return render_template('add_user.html')

@app.route('/', methods=['POST'])
def add_user():
    """Adds user from form"""
    first_name = request.form['firstname']
    last_name = request.form['lastname']
    image_url = request.form['image']
    if is_empty([first_name, last_name]):
        return redirect('/users')
    else:
        make_user(first_name,last_name, image_url)
        return redirect("/users")


@app.route('/<int:new_user_id>')
def show_details(new_user_id):   
    """Show details about a single user"""
    user = User.query.get_or_404(new_user_id)
    return render_template('details.html', user=user)




@app.route('/user/<int:user_id>/edit')
def edit_user_page(user_id):
    """renders edit page"""
    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user=user)

@app.route('/user/<int:user_id>/edit', methods= ["POST"])
def edit_user(user_id):
    """processes form that edits user """
    user = User.query.get_or_404(user_id)
    first_name = request.form['firstname']
    last_name = request.form['lastname']
    image_url = request.form['image']
    if is_empty([first_name, last_name]):
        return redirect(f'/user/{user_id}/edit')
    else:
        user.first_name = first_name
        user.last_name = last_name
        user.image_url = image_url
        db.session.commit()
        return redirect('/users')

@app.route('/user/<int:user_id>/delete', methods=["POST"])
def delete_user(user_id):
    """deletes user """
    User.query.filter_by(id=user_id).delete()
    db.session.commit()
    return redirect('/users')


    

# Have a cancel button that returns to the detail page for a user, and a save button that updates the user.

# POST /users/[user-id]/edit
# Process the edit form, returning the user to the /users page.
# POST /users/[user-id]/delete
# Delete the user