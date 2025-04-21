from flask import Flask, render_template, request, redirect, flash, url_for
from flask_migrate import Migrate
from config import Config
from model import Book, User, db

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()
    if not Book.query.first():
        db.session.add_all([
            Book(title="The Alchemist", author="Paulo Coelho", isbn="123456789", available_copies=3),
            Book(title="Atomic Habits", author="James Clear", isbn="987654321", available_copies=2)
        ])
        db.session.commit()

@app.route('/')
def home():
    books = Book.query.all()
    return render_template('index.html', books=books)

@app.route('/search')
def search_books():
    title = request.args.get('title', '')
    author = request.args.get('author', '')
    query = Book.query
    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    books = query.all()
    return render_template('index.html', books=books)

@app.route('/borrow/<int:book_id>', methods=['POST'])
def borrow_book(book_id):
    user_name = request.form.get('user_name')
    book = Book.query.get_or_404(book_id)
    if book.borrow(user_name):
        db.session.commit()
        flash(f"You borrowed '{book.title}'", 'success')
    else:
        flash("Book not available", 'danger')
    return redirect(url_for('home'))



# not returning the not borrowed book when clicking on return book button
@app.route('/return_book/<int:book_id>', methods=['POST'])
def return_book(book_id):
    book = Book.query.get_or_404(book_id)
    if book.book_user_id is not None:
        book.return_book()
        db.session.commit()
        flash(f"You returned '{book.title}'", 'info')
    else:
        flash("This book was not borrowed", 'warning')
    return redirect(url_for('home'))

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        isbn = request.form['isbn']
        copies = int(request.form['copies'])

        new_book = Book(title=title, author=author, isbn=isbn, available_copies=copies)
        db.session.add(new_book)
        db.session.commit()
        flash("Book added successfully!", "success")
        return redirect(url_for('home'))

    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)
