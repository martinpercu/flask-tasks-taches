from multiprocessing import context
from flask import render_template, session, redirect, flash, url_for
from flask_login import login_user, login_required, logout_user
from werkzeug.security import generate_password_hash, check_password_hash

from app.forms import LoginForm, SignupForm
from app.models import UserData, UserModel

from . import auth
from app.firestore_service import get_user, user_put
from app.models import UserModel, UserData 


@auth.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()
    context = {
        'login_form': login_form
    }

    if login_form.validate_on_submit():
        username = login_form.username.data
        # session['username'] = username
        password = login_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is not None:
            #password_from_db = user_doc.to_dict()['password']

            if check_password_hash(user_doc.to_dict()['password'], password):
                user_data = UserData(username, password)
                user = UserModel(user_data)
                print(f'-user: {user}')
                status=login_user(user)
               
                redirect(url_for('hello'))
            else:
                flash('The info not match with Database')

        else:
            flash('The user name is not finded')

            

        # flash('Nombre de usuario registrado con éxito!')


        return redirect(url_for('index'))


    return render_template('login.html', **context)
    
@auth.route('signup', methods=['GET', 'POST'])
def signup():
    signup_form = SignupForm()
    context = {
        'signup_form': signup_form
    }

    if signup_form.validate_on_submit():
        username = signup_form.username.data
        password = signup_form.password.data

        user_doc = get_user(username)

        if user_doc.to_dict() is None:
            password_hash = generate_password_hash(password)
            user_data = UserData(username, password_hash)
            user_put(user_data)

            user = UserModel(user_data)

            login_user(user)

            flash('Welcome!! You are registered and logged. ---- Bienvenue!! Vous est enregistré et logged')

            return redirect(url_for('hello'))

        else:
            flash('This user name is already Register!! ------ Cet nom d\'utilisateur existe déjà ! !')
            flash('Register another name ------- Utilisez un autre nom pour s\'enregistrer !!')
            # return redirect(url_for('auth.login'))


    return render_template('signup.html', **context)
    


@auth.route('logout')
@login_required
def logout():
    logout_user()
    flash('You are logged out   ---   Vous êtes déconnecté')

    return redirect(url_for('auth.login'))
    