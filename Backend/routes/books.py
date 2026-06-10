from flask import Blueprint, request, jsonify

from models import db, Book

books_bp = Blueprint(
    "books",
    __name__
)


@books_bp.route(
    "/books",
    methods=["GET"]
)
def get_books():

    books = Book.query.all()

    result = []

    for book in books:
        result.append({
            "id": book.id,
            "title": book.title,
            "author": book.author,
            "category": book.category,
            "quantity": book.quantity
        })

    return jsonify(result)


@books_bp.route(
    "/books",
    methods=["POST"]
)
def add_book():

    data = request.get_json()

    book = Book(
        title=data["title"],
        author=data["author"],
        category=data["category"],
        quantity=data["quantity"]
    )

    db.session.add(book)
    db.session.commit()

    return jsonify({
        "message": "Book added successfully"
    })


@books_bp.route(
    "/books/<int:id>",
    methods=["DELETE"]
)
def delete_book(id):

    book = Book.query.get(id)

    if not book:
        return jsonify({
            "message": "Book not found"
        }), 404

    db.session.delete(book)
    db.session.commit()

    return jsonify({
        "message": "Book deleted"
    })