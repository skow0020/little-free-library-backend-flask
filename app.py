from models import *
import os
from random import randint

from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/books", methods=['GET'])
def get_books():
    return jsonify([
        {
            'book': book.title,
            'id': book.id
        } for book in Book.query.all()
    ])


@app.route("/book", methods=['POST'])
def post_book():
    randomID = int(''.join(["{}".format(randint(0, 9)) for num in range(0, 4)]))

    data = request.get_json()

    book = Book(
        title=data['title'],
        id=randomID
    )

    db.session.add(book)
    db.session.commit()
    return {'title': book.title, 'id': book.id}, 201


if __name__ == '__main__':
    app.run()
