from flask import Flask, request, session, jsonify, redirect
from passlib.hash import pbkdf2_sha256
from app import studentdb, teacherdb, admindb
import uuid

class Student():
    
  def start_session (self,student):
        del student['password']
        session['logged_in'] = True
        session['student'] = student
        return jsonify(student),200
    
  def signup(self):

    print(request.form)

        #create a new student account
    student = {
            "_id": uuid.uuid4().hex,
      "firstname": request.form.get('firstname'),
       "lastname": request.form.get('lastname'),
       "password": request.form.get('password'),
          "email": request.form.get('email'),
      "studentid": request.form.get('studentid'),
     "department": request.form.get('department'),
          "major": request.form.get('major'),
          "phone": request.form.get('phone'),
        }
    #Encrypt the password
    student['password'] = pbkdf2_sha256.encrypt(student['password'])
    

    if studentdb.students.find_one({"email": student['email']}):
       return jsonify({"error": "Email Account Already Used"}), 400

    if studentdb.students.insert_one(student):
       return self.start_session(student)

    return jsonify({"error":"signup failed"}), 400
  
  def signout(self):
     session.clear()
     return redirect('/')
  
  def login(self):
     student = studentdb.student.find_one({
        "email": request.form.get('email')
     })

     if student and pbkdf2_sha256.verify(request.form.get('password'), student['password']):
        return self.start_session(student)

     return jsonify({"error":"Invalid login credentials"}),401

class Teacher():
    
  def signup(self):

    print(request.form)

        #create a new teacher account
    teacher = {
            "_id": uuid.uuid4().hex,
      "firstname": request.form.get('firstname'),
       "lastname": request.form.get('lastname'),
       "password": request.form.get('password'),
          "email": request.form.get('email'),
        "subject": request.form.get('subject'),
     "department": request.form.get('department'),
          "major": request.form.get('major'),
          "phone": request.form.get('phone'),
        }

    #Encrypt the password
    teacher['password'] = pbkdf2_sha256.encrypt(teacher['password'])
    

    if teacherdb.teachers.find_one({"email": teacher['email']}):
        return jsonify({"error": "Email Account Already Used"}), 400

    if teacherdb.teachers.insert_one(teacher):
        return jsonify(teacher), 200

    return jsonify({"error":"signup failed"}), 400
  
  def signout(self):
     session.clear()
     return redirect('/')
  
  def login(self):
     teacher = teacherdb.teacher.find_one({
        "email": request.form.get('email')
     })

     if teacher and pbkdf2_sha256.verify(request.form.get('password'), teacher['password']):
        return self.start_session(teacher)

     return jsonify({"error":"Invalid login credentials"}),401  

class Admin():
    
  def signup(self):
    print(request.form)

        #create a new admin account

    admin = {
        "_id": uuid.uuid4().hex,
        "firstname": request.form.get('firstname'),
        "lastname": request.form.get('lastname'),
        "password": request.form.get('password'),
        "email": request.form.get('email'),
        "position": request.form.get('position'),
        "department": request.form.get('department'),
        "major": request.form.get('major'),
        "phone": request.form.get('phone'),
        }

    #Encrypt the password
    admin['password'] = pbkdf2_sha256.encrypt(admin['password'])

    if admindb.admins.find_one({"email": admin['email']}):
       return jsonify({"error": "Email Account Already Used"}), 400

    if admindb.admins.insert_one(admin):
        return jsonify(admin), 200

    return jsonify({"error":"signup failed"}), 400
  
  def signout(self):
     session.clear()
     return redirect('/')
  
  def login(self):
     admin = admindb.admin.find_one({
        "email": request.form.get('email')
     })

     if admin and pbkdf2_sha256.verify(request.form.get('password'), admin['password']):
        return self.start_session(admin)

     return jsonify({"error":"Invalid login credentials"}),401
  
