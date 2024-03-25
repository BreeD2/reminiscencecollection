# reminiscencecollection/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)

# Example configuration
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['\x16vJ\x8c\x0ecg\xe7$\x0e\x8b\xd6\xab\x9b-['
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask extensions
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Specify what is the login view
login_manager.login_message_category = 'info'

from .models import User

@login_manager.user_loader
def load_user(user_id):
    """
    Flask-Login uses this callback to load the current user.
    """
    return User.query.get(int(user_id))

# Import routes
from . import routes
