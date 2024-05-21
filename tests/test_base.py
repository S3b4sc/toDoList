from flask_testing import TestCase
from flask import current_app, url_for

#Here each method is a test

from main import app        #We importes the app itself

class MainTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        app.config['WTF CSRF_ENABLED'] = False  #We do not have a active session for the user.
        
        return app
    def test_app_exists(self):      #we check if the app exists.
        self.assertIsNotNone(current_app)
        
    def test_app_in_test_mode(self):  #check if is test mode
        self.assertTrue(current_app.config['TESTING'])
        
    #def test_index_redirects(self):
    #    response = self.client.get(url_for('index'))
        
    #    self.assertRedirects(response, url_for('hello'))        #index redirects correclt to hello?
        #This one is not well implemented
        
    def test_hello_get(self):
        response = self.client.get(url_for('hello'))
        
        self.assert200(response)
        
    #def test_hello_post(self):      #Now we check the form
    #    fake_form = {
    #        'username': 'fake',
    #        'fake_password':'fake-password'             # this tryal is not working wither, flask test in the console to run tests.
    #    }
    #    response = self.client.post(url_for('hello'), data = {})
        
    #    self.assertRedirects(response, url_for('index'))    #After the form we are redirected correctly.
        
        
    def test_auth_blueprint_exists(self):
        self.assertIn('auth', self.app.blueprints)
        
    def test_auth_login_get(self):
        response = self.client.get(url_for('auth.login'))
        
        self.assert200(response)
        
    def test_auth_login_template(self):
        response = self.client.get(url_for('auth.login'))
        
        self.assertTemplateUsed(response, 'login.html')