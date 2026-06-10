from flask import Blueprint, request, jsonify
from datetime import date

from models import db
from models import Book
from models import Transaction

transactions_bp = Blueprint(
    "transactions",
    __name__
)


@transactions_bp.route(
    "/issue-book",
    methods=["POST"]
)
def issue_book():

    data = request.get_json()

    user_id = data["user_id"]
    book_id = data["book_id"]

    book = Book.query.get(book_id)

    if not book:
        return jsonify({
            "message": "Book not found"
        }), 404

    if book.quantity <= 0:
        return jsonify({
            "message": "Book not available"
        }), 400

    transaction = Transaction(
        user_id=user_id,
        book_id=book_id,
        issue_date=date.today(),
        status="Issued"
    )

    book.quantity -= 1

    db.session.add(transaction)
    db.session.commit()

    return jsonify({
        "message": "Book issued successfully"
    })


@transactions_bp.route(
    "/return-book/<int:id>",
    methods=["POST"]
)
def return_book(id):

    transaction = Transaction.query.get(id)

    if not transaction:
        return jsonify({
            "message": "Transaction not found"
        }), 404

    if transaction.status == "Returned":
        return jsonify({
            "message": "Book already returned"
        }), 400

    transaction.status = "Returned"
    transaction.return_date = date.today()

    book = Book.query.get(
        transaction.book_id
    )

    if book:
        book.quantity += 1

    db.session.commit()

    return jsonify({
        "message": "Book returned successfully"
    })


@transactions_bp.route(
    "/issued-books",
    methods=["GET"]
)
def issued_books():

    transactions = Transaction.query.all()

    result = []

    for transaction in transactions:

        result.append({
            "id": transaction.id,
            "user_id": transaction.user_id,
            "book_id": transaction.book_id,
            "issue_date": str(transaction.issue_date),
            "return_date": str(transaction.return_date),
            "status": transaction.status
        })

    return jsonify(result)