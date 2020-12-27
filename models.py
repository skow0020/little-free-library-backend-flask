from app import db


class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String())

    def __init__(self, url):
        self.id = id

    def __repr__(self):
        return '<title: {}>'.format(self.title)
