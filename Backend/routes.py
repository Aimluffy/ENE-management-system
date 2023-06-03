from flask import Flask
from app import app
from models import Student,Teacher,Admin

# sign in route
@app.route('/student/signup', methods=['POST'])
def signup():
    return Student().signup()

@app.route('/teacher/signup', methods=['POST'])
def signup():
    return Teacher().signup()

@app.route('/admin/signin', methods=['POST'])
def signup():
    return Admin().signup()

#sign out route
@app.route('/student/signout')
def signout():
    return Student().signout()

@app.route('/teacher/signout')
def signout():
    return Teacher().signout()

@app.route('/admin/signout')
def signout():
    return Admin().signout()

#login routes

@app.route('/student/login',method=['POST'])
def login():
    return Student().login()

@app.route('/teacher/login',method=['POST'])
def login():
    return Teacher().login()

@app.route('/admin/login')
def login():
    return Admin().login()