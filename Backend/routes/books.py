from flask import Blueprint, render_template, request, redirect, url_for
from models import db, Book

books_bp = Blueprint('books', __name__)

@books_bp.route('/books', methods=['GET', 'POST'])
def manage_books():
    if request.method == 'POST':
        title = request.form.get('title')
        author = request.form.get('author')
        
        if title and author:
            new_book = Book(title=title, author=author, available=True)
            db.session.add(new_book)
            db.session.commit()
        return redirect(url_for('books.manage_books'))
        
    all_books = Book.query.all()
    # This line forces Flask to load the HTML file instead of printing []
    return render_template('books.html', books=all_books)


@books_bp.route('/books/delete/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    book_to_delete = Book.query.get_or_404(book_id)
    try:
        db.session.delete(book_to_delete)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        # If a book is currently borrowed, database foreign keys might prevent deletion safely
        print(f"Error deleting book: {e}")
    return redirect(url_for('books.manage_books'))