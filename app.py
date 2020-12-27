import os
import operator
import json
from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

import os
import psycopg2
from sqlalchemy.sql.elements import Null

DATABASE_URL = os.environ['DATABASE_URL']

# conn = psycopg2.connect(DATABASE_URL, sslmode='require')
conn = Null
try:
    conn = psycopg2.connect(DATABASE_URL, sslmode='require')
 
    if conn is not None:
        print('Connection established to PostgreSQL.')
    else:
        print('Connection not established to PostgreSQL.')
        
except (Exception, psycopg2.DatabaseError) as error:
    print(error)
 
finally:
    if conn is not None:
        conn.close()
        print('Finally, connection closed.')


app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


# from models import *


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/books", methods=['GET'])
def get_books():
    with conn:
      with conn.cursor() as curs:
        curs.execute("SELECT * FROM books;")

    conn.close()
    


if __name__ == '__main__':
    app.run()