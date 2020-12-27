import json
import os

from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import *


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/books", methods=['GET'])
def get_books():
    books = Book.query.all()
    return {
        'book': books[0].title
    }


if __name__ == '__main__':
    app.run()
