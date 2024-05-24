from flask import request, make_response, redirect, render_template, session, url_for
import unittest

from app import create_app
from app.forms import LoginForm

from app.firestore_service import get_users, get_todos

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

@app.route('/hello', methods= ['GET'])  #For the  form to be allowed.
def hello():
    
    
    user_ip = session.get('user_ip')
    username = session.get('username')
    
    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username), #get the todos from  the logged user
        'username': username
    
    }
    
    users = get_users()
    
    for user in users:
        print(user.id)
        print(user.to_dict()['password'])
    
    return render_template('hello.html', **context)
    
