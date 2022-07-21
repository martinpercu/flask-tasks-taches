from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SignupForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Signup')


class TodoForm(FlaskForm):
    description = StringField('Task description', validators=[DataRequired()])
    submit = SubmitField('Add / Ajouter')


class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Delete Task / Efacer Tâche')


class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Changer task status / Modifier l\'état de la tâche')