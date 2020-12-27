from models import Result, Book
import json
import os

import psycopg2
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

# DATABASE_URL = os.environ['DATABASE_URL']

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
# conn = psycopg2.connect(DATABASE_URL)

# if conn is not None:
#     print('Connection established to PostgreSQL.')
# else:
#     print('Connection not established to PostgreSQL.')

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route("/books", methods=['GET'])
def get_books():
    return Book.query.all()
    # with conn:
    #     with conn.cursor() as curs:
    #         curs.execute("SELECT * FROM books;")

    #         records = curs.fetchall()
    #         print("Total rows are:  ", len(records))
    #         print("Printing each row")
    #         for row in records:
    #             print("Id: ", row[0])

    #         return json.dumps(records)


if __name__ == '__main__':
    app.run()
