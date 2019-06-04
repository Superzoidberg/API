from flask import render_template, flash, redirect, url_for, request, session, make_response
from app import app, db
from app.forms import LoginForm, RegistrationForm, NewProjectForm, EditProjectForm, ResetPasswordRequestForm, ResetPasswordForm
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
from app.models import User
from werkzeug.urls import url_parse
from sqlalchemy import func, cast, Integer
from app.email import send_password_reset_email
import os
import datetime



basedir = os.path.abspath(os.path.dirname(__file__))
jfile = basedir + "/static/javascript.js"
cfile = basedir + "/static/styles.css"
c2file = basedir + "/static/indexstyles.css"
jfilesize = int(os.path.getmtime(jfile))
cfilesize = int(os.path.getmtime(cfile))
c2filesize = int(os.path.getmtime(c2file))


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        if user.role == "user":
            flash('You do not have the proper authority')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form, jfilesize=jfilesize, cfilesize=cfilesize)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    dev = "Projects"
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, role="user")
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form, jfilesize=jfilesize, cfilesize=cfilesize, dev=dev)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            send_password_reset_email(user)
        flash('Check your email for the instructions to reset your password')
        return redirect(url_for('login'))
    return render_template('reset_password_request.html', title='Reset Password', form=form, jfilesize=jfilesize, cfilesize=cfilesize)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = User.verify_reset_password_token(token)
    if not user:
        return redirect(url_for('index'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been reset.')
        return redirect(url_for('login'))
    return render_template('reset_password.html', form=form, title='Reset Password', jfilesize=jfilesize, cfilesize=cfilesize)






#*****************
#** Catch ALL
#*****************
@app.route('/<path:path>')
def catch_all(path):
    return redirect(url_for('index'))