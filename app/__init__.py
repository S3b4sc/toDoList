from flask import Flask
from flask_bootstrap import Bootstrap
from flask_login import login_required

from flask_login import LoginManager   #Authenticate login
from .models import UserModel  #To use on load_user

from .config import Config
from .auth.views import authBlueprint


login_manager = LoginManager()
login_manager.login_view = 'auth.login'


#To solve the probem 'mising test_loader'
@login_manager.user_loader
def load_user(username):
    return  UserModel.query(username)       #Look for the user on the data base using the query


def create_app():
    '''
    Here the app is created as an object of the class Flask
    
    retunrs:
    The app
    '''
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)      #We configurate the app, using the properties from the opject Config.
    
    login_manager.init_app(app) #start the app
    
    app.register_blueprint(authBlueprint)
    
    return app