"""Blogly application."""


from crypt import methods
from flask import Flask, request, redirect, render_template
from models import db, connect_db, User

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
    return redirect('/users')

@app.route('/users')
def list_of_users():
    users = User.query.all()
    return render_template('list.html', users=users)


@app.route('/users/new')
def add_user_form():
    return render_template('add_user.html')

@app.route('/', methods=['POST'])
def add_user():
    first_name = request.form['firstname']
    last_name = request.form['lastname']
    image_url = request.form['image']
    
    new_user = User(first_name=first_name, last_name=last_name, image_url=image_url)
    db.session.add(new_user)
    db.session.commit()
    return redirect(f"/{new_user.id}")

@app.route('/<int:new_user_id>')
def show_details(new_user_id):   
    user = User.query.get_or_404(new_user_id)
    """Show details about a single user"""
    return render_template('details.html', user=user)




@app.route('/users/<int:user_id>/edit')
def edit_user_page(user_id):
    user = User.query.get_or_404(user_id)
    return render_template('edit_user.html', user=user)

@app.route('/user/<int:user_id>/edit', methods= ["POST"])
def edit_user(user_id):
    user = User.query.get_or_404(user_id)
    print(user.first_name)
    user.first_name = request.form['firstname']
    user.last_name = request.form['lastname']
    user.image_url = request.form['image']
    db.session.add(user)
    db.session.commit()
    return redirect('/')
    

# Have a cancel button that returns to the detail page for a user, and a save button that updates the user.

# POST /users/[user-id]/edit
# Process the edit form, returning the user to the /users page.
# POST /users/[user-id]/delete
# Delete the user