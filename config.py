import os

class Config:
    # App Security Key
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret-key-146'
    
    # PostgreSQL Database URL
    # Replace 'username', 'password', 'localhost', '5432', 'dbname' with your PostgreSQL setup
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:1234@127.0.0.1:5432/postgres'
        
    SQLALCHEMY_TRACK_MODIFICATIONS = False