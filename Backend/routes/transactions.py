from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Book, Student, Transaction
from datetime import datetime

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/transactions', methods=['GET', 'POST'])
def manage_transactions():
    if request.method == 'POST':
        book_id = request.form.get('book_id')
        student_id = request.form.get('student_id')
        
        book = Book.query.get(book_id)
        if book and book.available:
            book.available = False
            today_str = datetime.now().strftime("%Y-%m-%d")
            new_tx = Transaction(book_id=book_id, student_id=student_id, issue_date=today_str)
            db.session.add(new_tx)
            db.session.commit()
        return redirect(url_for('transactions.manage_transactions'))
        
    all_transactions = Transaction.query.all()
    available_books = Book.query.filter_by(available=True).all()
    all_students = Student.query.all()
    
    return render_template('transactions.html', 
                           transactions=all_transactions, 
                           books=available_books, 
                           students=all_students)

@transactions_bp.route('/transactions/return/<int:tx_id>', methods=['POST'])
def return_book(tx_id):
    tx = Transaction.query.get(tx_id)
    if tx:
        book = Book.query.get(tx.book_id)
        if book:
            book.available = True
        db.session.delete(tx)
        db.session.commit()
    return redirect(url_for('transactions.manage_transactions'))