import os
import sys
import traceback
from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from config import Config
from models import db, User, Task

app = Flask(__name__)
app.config.from_object(Config)

# Flask-Login setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Initialize Database tables automatically inside app context
db.init_app(app)
with app.app_context():
    try:
        db.create_all()
    except Exception as e:
        print(f"Database init error: {e}")

# 1. Home Route
@app.route('/')
def home():
    return render_template('index.html')

# 2. Dashboard Route
@app.route('/dashboard')
@login_required
def dashboard():
    user_tasks = Task.query.filter_by(user_id=current_user.id).all()
    return render_template('dashboard.html', tasks=user_tasks)

# 3. Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid email or password!', 'danger')
            
    return render_template('login.html')

# 4. Register Route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash('Email already registered!', 'warning')
            return redirect(url_for('register'))
            
        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, email=email, password_hash=hashed_pw)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Account created successfully! Please login.', 'success')
        return redirect(url_for('login'))
        
    return render_template('register.html')

# 5. Post Task Route
@app.route('/post-task', methods=['GET', 'POST'])
@login_required
def post_task():
    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        budget = request.form.get('budget')
        
        new_task = Task(
            title=title,
            description=description,
            budget=float(budget) if budget else 0.0,
            user_id=current_user.id
        )
        
        db.session.add(new_task)
        db.session.commit()
        
        flash('Task posted successfully!', 'success')
        return redirect(url_for('dashboard'))
        
    return render_template('post-task.html')

# Explore/Browse All Tasks Route
@app.route('/tasks')
def explore_tasks():
    all_tasks = Task.query.order_by(Task.created_at.desc()).all()
    return render_template('explore.html', tasks=all_tasks)

# Task Detail Route
@app.route('/task/<int:task_id>')
def task_detail(task_id):
    task = Task.query.get_or_404(task_id)
    return render_template('task_detail.html', task=task)

# Mark Task as Completed Route
@app.route('/task/<int:task_id>/complete', methods=['POST'])
@login_required
def mark_completed(task_id):
    task = Task.query.get_or_404(task_id)
    if task.user_id == current_user.id:
        task.status = 'Completed'
        db.session.commit()
        flash('Task marked as completed!', 'success')
    else:
        flash('Unauthorized action.', 'danger')
        
    return redirect(url_for('dashboard'))

# 6. Logout Route
@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logged out successfully.', 'info')
    return redirect(url_for('login'))

app = app
