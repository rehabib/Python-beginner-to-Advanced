class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
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
    if self.is_available:
        self.is_available = False
        print(f"Sorry, '{self.title}' is currently not available.")
    else:   
        print(f"You have borrowed '{self.title}'.")
# return_book method
def return_book(self):
    if not self.is_available:
        self.is_available = True
        print(f"You have returned '{self.title}'. Thank you!")
    else:
        print(f"'{self.title}' was not borrowed.")  
class Library:
    def __init__(self):
        self.books = [] # List to store books in the library

    def add_book(self, book):
        self.self.books.append(book)
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


class User():
