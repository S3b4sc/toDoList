from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField       #Necessary things for the forms
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):          #we have to extend the class we imported from flask_wtf
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    
    #Now we button
    submit = SubmitField('Enviar')
    
class TodoForm(FlaskForm):
    description = StringField('Descripción', validators=[DataRequired()])
    submit = SubmitField('Crear')
    
class DeleteTodoform(FlaskForm):
    submit = SubmitField('Borrar')
    
class UpdateTodoform(FlaskForm):
    submit = SubmitField('Cambiar estado')