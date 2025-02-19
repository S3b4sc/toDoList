import unittest
from flask import request, make_response, redirect, render_template, session, url_for, flash

from flask_login import login_required, current_user

from app import create_app
from app.forms import TodoForm, DeleteTodoform, UpdateTodoform

from app.firestore_service import update_todo, get_todos, put_todo, delete_todo



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
@login_required
def hello():

    
    user_ip = session.get('user_ip')
    username = current_user.id
    todo_form = TodoForm()
    delete_form = DeleteTodoform()
    update_form = UpdateTodoform()
    
    
    context = {
        'user_ip': user_ip,
        'todos': get_todos(user_id=username), #get the todos from  the logged user
        'username': username,
        'todo_form': todo_form,
        'delete_form': delete_form,
        'update_form': update_form
    
    }
    
    if todo_form.validate_on_submit():
        put_todo(user_id=username, description=todo_form.description.data)
        
        flash('Tu tarea se ha creado con éxito')
        
        return redirect(url_for('hello'))
    
    return render_template('hello.html', **context)
    
@app.route('/todos/delete/<todo_id>', methods= ['POST'])
def delete(todo_id):
    user_id = current_user.id
    delete_todo (user_id=user_id, todo_id=todo_id)
    
    return redirect(url_for('hello'))

@app.route('/todos/update/<todo_id>/<done>', methods=['POST'])
def update(todo_id, done):
    user_id = current_user.id
    
    update_todo(user_id=user_id, todo_id=todo_id, done=done)
    return redirect(url_for('hello'))