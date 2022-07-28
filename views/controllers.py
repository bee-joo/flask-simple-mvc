from flask import Blueprint, render_template, make_response

from views.form import Form
from model import Client, db

import pyqrcode


controller = Blueprint('controller', __name__, template_folder='templates')

@controller.route('/', methods=['get', 'post'])
def index():

    form = Form()
      
    if form.validate_on_submit():
    
        exists = db.session.query(Client).filter_by(email=form.email.data).first() is not None 
        if exists:
            error = "E-mail уже зарегистрирован"
            return render_template('layout.html', content='error.html', error=error)
                  
        cl = Client(
            first_name = form.first_name.data,
            last_name = form.last_name.data,
            email = form.email.data,
            city = form.city.data,
            post_index = int(form.post_index.data),
            address = form.address.data
        )
                
                
        db.session.add(cl)
        db.session.commit()
    
        url = pyqrcode.create(f'https://FlaskMVC.danilabukin.repl.co/users/{cl.id}/')
        url.svg(f'images/{cl.id}.svg', scale=8)
                
        return render_template('layout.html', content='post.html', cl=cl)
        
    return render_template('layout.html', content='form.html', form=form)
        

@controller.route('/users/')
def show_all_users():
    users = db.session.query(Client).all()
    return render_template('layout.html', content='allusers.html', users=users)


@controller.route('/users/<int:id>/')
def show_user(id):
    user = db.session.query(Client).get(id)
    if user is None:
        return page_not_found(404)
        
    return render_template('layout.html', content='user.html', cl=user)


@controller.route('/images/<int:id>.svg/')
def show_image(id):
    try:
        file = open(f"images/{id}.svg").read()
    except Exception:
        return page_not_found(404)
    else:
        response = make_response(file)
        response.headers["Content-Type"] = 'image/svg+xml'
    
        return response


@controller.errorhandler(404)
def page_not_found(error):
    return render_template("404.html"), 404