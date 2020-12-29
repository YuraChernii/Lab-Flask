from app import app
from app import auth
from flask_login import login_user, login_required, logout_user
from flask import request, url_for, jsonify, render_template, redirect, flash
from flask_api import FlaskAPI, status, exceptions
from . import db
from app import Student
from werkzeug.security import generate_password_hash, check_password_hash
from flask_testing import TestCase


users = {
    "john": generate_password_hash("hell"),
    "susan": generate_password_hash("bye")
}

#@auth.verify_password
#def verify_password(username, password):
#    if username in users and \
#            check_password_hash(users.get(username), password):
#        return username
#@app.route('/api2')
#def index2():
#    return "Hello, %s!"
#
#@app.route("/ajax/")
#def some_json():
#    return jsonify(success=True)
#
#@app.route('/api')
#@login_required
#def index():
#    return "Hello, %s!"#
#
#@app.route('/login', methods=['GET', 'POST'])
#def login_page():
#    print(1)
#    login = request.form.get('login')
#    password = request.form.get('password')
#    print(2)
#    if login and password:
#        user = Student.query.filter_by(userName=login).first()
#        print(3)
#        if check_password_hash(user.password, password):
#            login_user(user)
 #           next_page = request.args.get('next')
  #          redirect(next_page)
   #     else:
    #        flash('incorrect')
#
 #   else:
  #      flash('Please fill login and password fields')
   #     return 1#render_template('login.html')


