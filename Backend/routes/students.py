from flask import Blueprint, jsonify
from models import User

students_bp = Blueprint("students", __name__)


@students_bp.route("/students", methods=["GET"])
def get_students():

    students = User.query.filter_by(role="student").all()

    result = []

    for student in students:
        result.append({
            "id": student.id,
            "name": student.name,
            "email": student.email
        })

    return jsonify(result)