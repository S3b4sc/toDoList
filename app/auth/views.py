from flask import render_template, flash, session, redirect, url_for
from flask import Blueprint

from werkzeug.security import generate_password_hash, check_password_hash

from app.forms import LoginForm
from app.firestore_service import get_user  #To create the login and logout
from app.firestore_service import user_put 
from app.models import UserModel, UserData

from flask_login import login_user, login_required, logout_user

authBlueprint = Blueprint('auth',__name__)#, url_prefix='/auth')

@authBlueprint.route('/login', methods=['GET', 'POST'])
def login():
    
    login_form = LoginForm()
    
    context = {
        'login_form': LoginForm()
    }
    
    if login_form.validate_on_submit():     #Is the form is sended and its correct, then...
        
        username = login_form.username.data             #We get the data form the form
        password = login_form.password.data
        
        user_doc = get_user(username)
        
        if user_doc.to_dict() is not None:  #If the user is found on the data base
            password_from_db = user_doc.to_dict()['password']
            
            #verify the password
            if check_password_hash(password_from_db, password):
                user_data = UserData(username, password)
                
                #The user we are currently at
                user = UserModel(user_data)  

                login_user(user)
                
                flash('Bienvenido de nuevo')
                redirect(url_for('hello'))
                
            else:
                flash('La información no coincide.')
        else:
            flash('El usuario no existe')
                
        
        return redirect(url_for('index'))           #Once sended we go back to the form to be filled.
    

    return render_template('login.html', **context)

@authBlueprint.route('/signup', methods=['GET','POST'])
def signup():
    signup_form = LoginForm()
    
    
    context = {
        'signup_form': signup_form
    }
    
    if signup_form.validate_on_submit():
        username = signup_form.username.data        #Get the info from the form
        password = signup_form.password.data
        
        user_doc = get_user(username)
        
        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)   #The data to store
            
            user_put(user_data)
            
            user = UserModel(user_data)
            login_user(user)
            
            flash('Bienveido!')
            return redirect(url_for('hello'))
        else:
            flash('El usuario ya existe')
    
    return render_template('signup.html', **context)


@authBlueprint.route('/logout')
@login_required                 #We can only sigout if we are loged.
def logout():
    logout_user()
    flash('Regresa pronto')

    return redirect(url_for('auth.login'))