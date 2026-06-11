from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Student, Book, Transaction

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


@students_bp.route('/students/delete/<int:student_id>', methods=['POST'])
def delete_student(student_id):
    student_to_delete = Student.query.get_or_404(student_id)
    try:
        student_transactions = Transaction.query.filter_by(student_id=student_id).all()
        
        for transaction in student_transactions:
            book = Book.query.get(transaction.book_id)
            if book:
                book.available = True
            db.session.delete(transaction)
            
        # Move the student deletion right here, before committing
        db.session.delete(student_to_delete)
        
        # ONE commit to save everything safely
        db.session.commit()
        
    except Exception as e:
        db.session.rollback()
        print(f"Error deleting student: {e}")
        
    return redirect(url_for('students.manage_students'))