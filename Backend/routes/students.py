from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Student

students_bp = Blueprint('students', __name__)

@students_bp.route('/students', methods=['GET', 'POST'])
def manage_students():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        
        if name and email:
            student_exists = Student.query.filter_by(email=email).first()
            if not student_exists:
                new_student = Student(name=name, email=email)
                db.session.add(new_student)
                db.session.commit()
        return redirect(url_for('students.manage_students'))
        
    all_students = Student.query.all()
    return render_template('students.html', students=all_students)