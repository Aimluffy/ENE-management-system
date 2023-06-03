from flask import Flask,render_template,session,redirect,request
from functools import wraps
import pymongo


app = Flask(__name__)
app.secret_key = b'\xe7\xa1H\xbb\xc4\x9c\x85b5X%\xd9+\x86\x8av'

#Database
cilent = pymongo.MongoClient('localhost',27017)
studentdb = cilent.student_login_system
teacherdb = cilent.teacher_login_system
admindb = cilent.admin_login_system
documentdb = cilent.document_system
petitiondb = cilent.petition_system
traineesdb = cilent.trainee_system
classesdb = cilent.classes_system
activitydb = cilent.activity_system
staffdb = cilent.staff_system
#Routes
from routes import Student, Teacher, Admin


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            return redirect('/')
        
    return wrap

# route home
@app.route('/home')
@login_required
def home():
    return render_template('home.html')


#route staff
@app.route('/staff')
@login_required
def staff():
    staff = {
        "name": request.form.get('name'),
        "email": request.form.get('email'),
        "phone": request.form.get('phone'),
        "department": request.form.get('department'),
        "major": request.form.get('major'),
        "position": request.form.get('position')
        #"created_at": request.time

    }

    if request.method == 'POST':
        return staffdb.staff.insert_one(staff)
    if request.method == 'GET':
        return staffdb.staff.get_all(staff)
    return render_template('staff.html')

# route trainee
@app.route('/document',methods=['Post'])
@login_required
def document():
    document = {
        "name": request.form.get('name'), 
        "info": request.form.get('info'),
        "file": request.file.get('file'),
    }
    if request.method == 'POST':
        return documentdb.document.insert_one(document)
    if request.method == 'GET':
        return documentdb.document.get_all(document)

    return render_template('document.html')

#route trainee
@app.route('/trainee',Methods=['GET', 'POST'])
@login_required
def trainee():
    trainee = {
        "name": request.form.get('name'), 
        "info": request.form.get('info'),
        "file": request.file.get('file'),
    }
    if request.method == 'POST':
        return traineesdb.trainee.insert_one(trainee)
    if request.method == 'GET':
        return traineesdb.trainee.get_all(trainee)
    return render_template('petition_page.html')


# routes activity
@app.route('/activity', methods=['GET', 'POST'])
@login_required
def activity():
    activity = {
        "name": request.form.get('name'),
        "information": request.form.get('information'),
        "files": request.form.get('files'),
    }
    if request.method == 'POST':
        return activitydb.activity.insert_one(activity)
    return render_template('activity.html')
    

@app.route('/link_class', methods=['GET', 'POST','PUT'])
@login_required
def link_class():
    classes = {
        "header": request.form.get('header'),
        "info": request.form.get('info'),
        "year": request.form.get('year'),
        "courses": request.form.get('courses')
        
    }

    if request.method == 'POST':
        return classesdb.classes.insert_one(classes)
    return render_template('link_class.html')

@app.route('/petition', methods=['GET', 'POST'])
@login_required
def petition():
    petition = {
    "name": request.form.get('name'),
    "studentid": request.form.get('studentid'),
    "advisor": request.form.get('advisoryid'),
    "message": request.form.get('message'),
    "file": request.file.get('file'),
    "type": request.form.get('type'),
    }
    petitiondb.petiton.insert_one(petition)
    return render_template('petition.html')