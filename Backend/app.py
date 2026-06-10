from flask import Flask, render_template
from flask_cors import CORS

from config import Config
from models import db, Book, Student, Transaction  # Imported models for statistics

from routes.auth import auth_bp
from routes.books import books_bp
from routes.students import students_bp
from routes.transactions import transactions_bp

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

db.init_app(app)

app.register_blueprint(auth_bp)
app.register_blueprint(books_bp)
app.register_blueprint(students_bp)
app.register_blueprint(transactions_bp)

with app.app_context():
    db.create_all()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dashboard")
def dashboard():
    # Fetch total counts to show stats on the dashboard dashboard
    total_books = Book.query.count()
    total_students = Student.query.count()
    total_transactions = Transaction.query.count()
    return render_template("dashboard.html", books_count=total_books, students_count=total_students, tx_count=total_transactions)

if __name__ == "__main__":
    app.run(debug=True)