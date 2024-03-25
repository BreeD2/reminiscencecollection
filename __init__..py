from flask import Flask

app = Flask(__name__)

from reminiscencecollection import routes
