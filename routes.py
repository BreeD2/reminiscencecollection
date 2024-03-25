# reminiscencecollection/reminiscencecollection/routes.py
from flask import render_template
from . import app

@app.route('/signup/')
def signup():
    return render_template('signup/index.html')
