from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'your_database_uri'
app.config['UPLOAD_FOLDER'] = 'uploads'
db = SQLAlchemy(app)


class Petition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    student_id = db.Column(db.String(20))
    advisor_name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    message = db.Column(db.Text)
    type_form = db.Column(db.String(10))
    file_path = db.Column(db.String(200))

    def __init__(self, name, student_id, advisor_name, email, message, type_form, file_path):
        self.name = name
        self.student_id = student_id
        self.advisor_name = advisor_name
        self.email = email
        self.message = message
        self.type_form = type_form
        self.file_path = file_path


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/process_form', methods=['POST'])
def process_form():
    name = request.form['name']
    student_id = request.form['student-id']
    advisor_name = request.form['advisor-name']
    email = request.form['email']
    message = request.form['message']
    type_form = request.form['type-form']

    file = request.files['file']
    if file:
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)
    else:
        file_path = None

    petition = Petition(name, student_id, advisor_name, email, message, type_form, file_path)
    db.session.add(petition)
    db.session.commit()

    return 'Form submitted successfully!'


if __name__ == '__main__':
    app.run()
