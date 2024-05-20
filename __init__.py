from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config


def create_app():
    '''
    Here the app is created as an object of the class Flask
    
    retunrs:
    The app
    '''
    app = Flask(__name__)
    bootstrap = Bootstrap(app)

    app.config.from_object(Config)      #We configurate the app, using the properties from the opject Config.
    
    return app