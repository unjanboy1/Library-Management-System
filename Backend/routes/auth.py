from flask import Blueprint, render_template, request, redirect
from models import db, User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        print(f"--> TRYING TO REGISTER: {username}") # Tracking log
        
        if not username or not password:
            return "Username and Password are required!", 400
            
        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            print("--> REGISTRATION FAILED: Username already taken.")
            return "Username already taken!", 400
            
        new_user = User(username=username, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        print("--> REGISTRATION SUCCESSFUL! Redirecting to login...")
        return redirect('/login') # Direct path link
        
    return render_template('register.html')

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        print(f"--> TRYING TO LOG IN: {username}") # Tracking log
        
        user = User.query.filter_by(username=username, password=password).first()
        if user:
            print("--> LOGIN SUCCESSFUL! Forcing redirect to dashboard...")
            return redirect('/dashboard') # Forcing direct path bypass
            
        print("--> LOGIN FAILED: Incorrect username or password.")
        return "Invalid Credentials", 401
        
    return render_template('login.html')