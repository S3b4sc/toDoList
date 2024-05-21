from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest

from app import create_app
from app.forms import LoginForm

app = create_app()
 
 #------------------To run tests
@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')  #run all tests stores in directory tests.
    unittest.TextTestRunner().run(tests)        #afetr discoreving the tests we run them.

#-------------------------------
 
 
 
@app.route('/')
def index():
    
    user_ip = request.remote_addr
    response = make_response(redirect('hello'))
    session['user_ip'] = user_ip
    
    return response

@app.route('/hello', methods= ['GET', 'POST'])  #For the  form to be allowed.
def hello():
    
    user_ip = session.get('user_ip')
    login_form = LoginForm()
    username = session.get('username')
    
    if login_form.validate_on_submit():     #Is the form is sended and its correct, then...
        username = login_form.username.data             #We get the data form the form
        session['username'] = username          #save the name on the session.
        
        flash('Nombre de usuario registrado con éxito')
        
        return redirect(url_for('index'))           #Once sended we go back to the form to be filled.
    
    
    context = {
        'user_ip': user_ip,
        'login_form': login_form,
        'username': username
    }
    
    return render_template('hello.html', **context)
