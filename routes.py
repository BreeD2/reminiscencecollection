# reminiscencecollection/reminiscencecollection/routes.py
from flask import render_template
from . import app

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact/')
def contact():
    return render_template('contact/index.html')

@app.route('/signup/')
def signup():
    return render_template('signup/index.html')

@app.route('/games/')
def games():
    return render_template('games/index.html')

# Define more routes as needed for other pages or game details
