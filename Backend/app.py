from flask import Flask
from flask_cors import CORS

from config import Config
from models import db

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
    return {
        "message": "Library Management System Running"
    }

if __name__ == "__main__":
    app.run(debug=True)