"""Blogly application."""


from crypt import methods
from flask import Flask, request, redirect, render_template, flash
from models import db, connect_db, User, Post
from utilities import is_empty, make_user
from datetime import datetime


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
    posts = user.posts
    return render_template('details.html', user=user, posts=posts)




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



@app.route('/users/[user-id]/posts/new')
def add_post():
    """Show form to add a post for that user."""



@app.route('/users/[user-id]/posts/new', methods=["POST"])
def handle_add_form():
    """ Handle add form; add post and redirect to the user detail page."""



@app.route('/posts/[post-id]')
def show_post():

    """Show a post and Show buttons to edit and delete the post."""



@app.route('/posts/[post-id]/edit')
def show_edit_form():
    """Show form to edit a post, and to cancel (back to user page)."""



@app.route('/posts/[post-id]/edit', methods=["POST"])
def edit_post():
     """Handle editing of a post. Redirect back to the post view."""




@app.route('/posts/[post-id]/delete', methods=["POST"])
def delete_post():
    """Delete the post."""


    
