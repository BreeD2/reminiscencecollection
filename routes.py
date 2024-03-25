# reminiscencecollection/reminiscencecollection/routes.py
from flask import render_template, abort
from . import app
from .models import Game  # Assuming you have a Game model defined

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

@app.route('/game/<string:game_slug>/')
def game_details(game_slug):
    game = Game.query.filter_by(slug=game_slug).first()
    if game is None:
        abort(404)
    return render_template('game_details.html', game=game)

# Add more routes as needed for other pages
