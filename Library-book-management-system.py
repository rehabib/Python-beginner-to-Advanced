from datetime import datetime, timedelta
# Library Book Management System
class Book:
    def __init__(self, title, author, isbn, total_copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.due_date = None
        self.total_copies = total_copies  # Total number of copies of the book
        self.available_copies = total_copies  # Number of available copies of the book
        self.is_available = True
    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"# added __str__ method for better representation

## self represents the instance of the class, and __str__ method is used to define a string representation of the object.
# This is useful for printing the object in a readable format.
#my_book = Book("The Alchemist", "Paulo Coelho", "123456789") # Example of creating a book object
#my_book.is_available = False  # Mark the book as not available
#print(my_book)  # Output: The Alchemist by Paulo Coelho (ISBN: 123456789)

# borow_book method
    def borrow_book(self):

        if self.available_copies > 0:
            self.available_copies -= 1
            self.due_date = datetime.now() + timedelta(days=14)  # Set due date to 14 days from now
            print(f"✅ You have borrowed '{self.title}'. Return by {self.due_date.strftime('%Y-%m-%d')}")
        else:
            print(f"❌ Sorry, '{self.title}' is currently not available.")

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            print(f"📚 Book '{self.title}' has been returned. Thank you!")
        else:
            print(f"⚠️ All copies of '{self.title}' are already in the library.")

book1 = Book("1984", "George Orwell", "1234567890", 2)

book1.borrow_book()  # 1 copy left
book1.borrow_book()  # 0 copies left
book1.borrow_book()  # No copies available

book1.return_book()  # 1 copy returned
book1.return_book()  # 2 copies total (full again)
book1.return_book()  # All copies already in
class Library:
    def __init__(self):
        self.books = [] # List to store books in the library

    def add_book(self, book):
        self.books.append(book)
        print(f"'{book.title}' has been added to the library.")

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"'{book.title}' has been removed from the library.")
                return
            print(f"No book found with ISBN: {isbn}")


    def search_book(self, title=None, author=None):
        results = []
        for book in self.books:
            # Check if the book matches the search criteria
            if (title and title.lower() in book.title.lower()) or (author and author.lower() in book.author.lower()):
                results.append(book)
        if results:
            print("Search results:")
            for book in results:
                print(book) 

        return results
book1 = Book("The Alchemist", "Paulo Coelho", "123456789")
book2 = Book("Atomic Habits", "James Clear", "987654321")

library = Library()
library.add_book(book1)
library.add_book(book2)

# Search by title
library.search_book(title="alchemist")

# Search by author
library.search_book(author="clear")


class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # List to store borrowed books

    def borrow_book(self, book):
        if book.is_available:
            book.borrow_book()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")
class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []  # List to store borrowed books

    def borrow_book(self, book):
        if book.is_available:
            book.borrow_book()
            self.borrowed_books.append(book)
            print(f"{self.name} has borrowed '{book.title}'.")
        else:
            print(f"Sorry, '{book.title}' is currently not available.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            print(f"{self.name} has returned '{book.title}'.")
        else:
            print(f"{self.name} did not borrow '{book.title}'.")


# Example usage
user = User("Alice")
user.borrow_book(book1)  # Alice borrows The Alchemist
user.return_book(book1)  # Alice returns The Alchemist
user.borrow_book(book1)  # Alice borrows The Alchemist again
user.return_book(book2)  # Alice tries to return a book she didn't borrow



    
