import sqlite3

# Connect with database
conn = sqlite3.connect('library.db')
c = conn.cursor()

# Create table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY,
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')
conn.commit()
conn.close()

# Insert a new book into the database
def insert_book(title, author, year):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("INSERT INTO books (title, author, year) VALUES (?, ?, ?)", (title, author, year))
    conn.commit()
    conn.close()
    print(f"Book '{title}' added to the library.")

# Inserting sample books
insert_book("The Alchemist", "Paulo Coelho", 1988)
insert_book("The Catcher in the Rye", "J.D. Salinger", 1951)
insert_book("To Kill a Mockingbird", "Harper Lee", 1960)

# Fetch and display all books
def fetch_all_books():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Year: {row[3]}")
    conn.close()

fetch_all_books()

# Fetch a book by its title
def fetch_book_by_title(title):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE title=?", (title,))
    row = c.fetchone()
    if row:
        print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Year: {row[3]}")
    else:
        print(f"No book found with title '{title}'")
    conn.close()

fetch_book_by_title("The Alchemist")
fetch_book_by_title("The Great Gatsby")  # Non-existing book

# Fetch books by year in descending order
def fetch_books_by_year_descending():
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books ORDER BY year DESC")
    rows = c.fetchall()
    for row in rows:
        print(f"ID: {row[0]}, Title: {row[1]}, Author: {row[2]}, Year: {row[3]}")
    conn.close()

fetch_books_by_year_descending()

# Update a book's title by its ID
def update_book_title(book_id, new_author, new_title):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("UPDATE books SET title=? WHERE id=?", (new_title, book_id))
    conn.commit()
    conn.close()
    print(f"Book ID {book_id} title updated to '{new_title}'.")

update_book_title(1, "The Alchemist", "The Alchemist: A Journey of Self-Discovery")
update_book_title(2, "The Catcher in the Rye", "The Catcher in the Rye: A Novel of Teenage Rebellion")
update_book_title(3, "To Kill a Mockingbird", "To Kill a Mockingbird: A Classic Novel")
update_book_title(4, "The Great Gatsby", "The Great Gatsby: A Tragic Love Story")  # Non-existing book

# Delete a book by its ID
def delete_book_by_id(book_id):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
    print(f"Book ID {book_id} deleted from the library.")

delete_book_by_id(3)  # Delete book with ID 3
delete_book_by_id(4)  # Try deleting non-existent book with ID 4


