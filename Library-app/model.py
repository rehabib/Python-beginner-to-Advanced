from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    borrowed_books = db.relationship('Book', backref='borrower', lazy=True)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    isbn = db.Column(db.String(13), unique=True, nullable=False)
    available_copies = db.Column(db.Integer, default=1)
    due_date = db.Column(db.DateTime)
    book_user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)

    def borrow(self, user_name=None):
        if self.available_copies > 0:
            self.available_copies -= 1
            self.due_date = datetime.utcnow()

            if user_name:
                user = User.query.filter_by(name=user_name).first()
                if not user:
                    user = User(name=user_name)
                    db.session.add(user)
                    db.session.commit()
                self.borrower = user
            return True
        return False

    def return_book(self):
        self.available_copies += 1
        self.due_date = None
        self.book_user_id = None
