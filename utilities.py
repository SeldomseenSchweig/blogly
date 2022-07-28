from flask import redirect, render_template, flash
from models import db, connect_db, User, Post




def is_empty(input):
    """Checks for empty input"""
    empty_string =''
    for item in input:
        if (empty_string == item.strip()):
            flash("One or more of your values are empty, please complete and resubmit")
            return True        
    return False

def make_user(fname,lname,url):
    """ccreates user"""
    new_user = User(first_name=fname, last_name=lname, image_url=url)
    db.session.add(new_user)
    db.session.commit()


def make_post(title, content, user_id):
    new_post = Post(title=title, content=content, user_id=user_id)
    db.session.add(new_post)
    db.session.commit()
