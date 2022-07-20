from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    username = StringField('User Name', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class TodoForm(FlaskForm):
    description = StringField('Task - Description - de la tache ', validators=[DataRequired()])
    submit = SubmitField('Add / Adjouter')


class DeleteTodoForm(FlaskForm):
    submit = SubmitField('Delete Task / Efacer Tache')


class UpdateTodoForm(FlaskForm):
    submit = SubmitField('Actualize Task / Actualiser Tache')