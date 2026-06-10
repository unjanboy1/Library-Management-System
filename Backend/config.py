from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

class Config:
    SECRET_KEY = "library_secret_key"

    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BASE_DIR}/library.db"

    SQLALCHEMY_TRACK_MODIFICATIONS = False