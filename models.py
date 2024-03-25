# reminiscencecollection/reminiscencecollection/models.py
from reminiscencecollection import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Define other fields...
