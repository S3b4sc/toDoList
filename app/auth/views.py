from flask import render_template, flash, session, redirect, url_for
from flask import Blueprint

from app.forms import LoginForm

authBlueprint = Blueprint('auth',__name__)#, url_prefix='/auth')

@authBlueprint.route('/login', methods=['GET', 'POST'])
def login():
    
    login_form = LoginForm()
    
    context = {
        'login_form': LoginForm()
    }
    
    if login_form.validate_on_submit():     #Is the form is sended and its correct, then...
        username = login_form.username.data             #We get the data form the form
        session['username'] = username          #save the name on the session.
        
        flash('Nombre de usuario registrado con éxito')
        
        return redirect(url_for('index'))           #Once sended we go back to the form to be filled.
    

    return render_template('login.html', **context)