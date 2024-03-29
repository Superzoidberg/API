from flask import render_template, flash, redirect, url_for, request, make_response, jsonify, g
from app import app, db
from app.forms import LoginForm, DeleteUser, ResetPasswordRequestForm, ResetPasswordForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required, UserMixin
from app.models import APIUser
from werkzeug.urls import url_parse
from sqlalchemy import func, cast, Integer
from app.email import send_password_reset_email
import os
import datetime
from app.errors import bad_request
from app.basicauth import basic_auth
from jsonschema import validate
import traceback
import re
import json


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
        user = APIUser.query.filter_by(username=form.username.data).first()
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
@login_required
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = APIUser(username=form.username.data, email=form.email.data, role="user")
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('index'))
    return render_template('register.html', title='Register', form=form, jfilesize=jfilesize, cfilesize=cfilesize)

@app.route('/remove', methods=['GET', 'POST'])
@login_required
def remove():
    form = DeleteUser()
    if form.validate_on_submit():
        APIUser.query.filter_by(username=form.username.data).delete()
        db.session.commit()
        flash('User deleted')
        return redirect(url_for('index'))
    return render_template('deleteuser.html', title='Delete User', form=form, jfilesize=jfilesize, cfilesize=cfilesize)


@app.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = ResetPasswordRequestForm()
    if form.validate_on_submit():
        user = APIUser.query.filter_by(email=form.email.data).first()
        print(user.role)
        if user:
            if user.role == "user":
                flash('You do not have the proper authority')
                return redirect(url_for('login'))
            send_password_reset_email(user)
            flash('Check your email for the instructions to reset your password')
            return redirect(url_for('login'))
        flash('Incorrect Email')
        
    return render_template('reset_password_request.html', title='Reset Password', form=form, jfilesize=jfilesize, cfilesize=cfilesize)


@app.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    user = APIUser.verify_reset_password_token(token)
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
    return bad_request("Invalid endpoint")








#*****************
#** API Routes
#*****************

@app.route('/api/v1/tender', methods=['GET', 'POST', 'PUT'])
@basic_auth.login_required
def apitenderpost():
    print(request.method)
    response = ""    
    if request.method == "POST":
        tenderCount = 0
        try:
            tenders = request.get_json(force=True)
            
        except TypeError:
            return bad_request("Invalid json input")

        for tender in tenders['tenders']:
            tenderCount = tenderCount +1
            try:
                validate(instance=tender, schema=app.config['TENDER_SCHEMA'])
                print(tender['SenderID'])
                print(tender['ReceiverID'])
                print(tender['BillOfLading'])
                print(tender['TenderedDate'])
                print(tender['TenderedTime'])
                print(tender['Hazmat'])
                print(tender['RespondBy']['Date'],tender['RespondBy']['Time'],tender['RespondBy']['TimeZone'])
                for refnum in tender['ReferenceNumbers']:
                    print(refnum['Type'] + "::" + refnum['ReferenceNumber'])

                for comment in tender['Comments']:
                    print(comment['Comment'])

                for location in tender['HeaderLocations']:
                    print(location['Type'])
                    print(location['Name'])
                    print(location['ID'])
                    print(location['Address'])
                    print(location['City'])
                    print(location['State'])
                    print(location['ZipCode'])
                    print(location['Country'])

                print(tender['Equipment']['Initial'])
                print(tender['Equipment']['TrailerNumber'])
                print(tender['Equipment']['TrailerType'])
                print(tender['Equipment']['TrailerSize'])
                
                print("*********")
                print("write file")
                print("*********")
                print("")
                print("")
                response = response + '{"TenderCount": ' + str(tenderCount) + ', "Status" : "Success", "Message": "Tender Posted"},\n'
            except:
                var = traceback.format_exc()
                var = re.sub(r'(.*)\n.*', r'\1', var[376:500])
                response = response + '{"TenderCount": ' + str(tenderCount) + ', "Status" : "Error", "Message": "' + var + '"},\n'

        return '{\n"TenderRespones": [\n' + response + ']\n}'

    elif request.method == "GET":
        try:
            tenderStats = request.get_json(force=True)
        except TypeError:
            return bad_request("Invalid json input")

        return '{\n"TenderRespones": [\n' + response + ']\n}'

    elif request.method == "PUT":
        return '{\n"TenderRespones": [\n' + response + ']\n}'

    else:
        response = '{"Error": "Incorrect method"}'
        return '{\n"TenderRespones": [\n' + response + ']\n}'

