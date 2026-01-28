class Book:
    
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True
    
    def __str__(self):
        return f"{self.title} by {self.author}"


class Library:
    #manages collection 
    
    def __init__(self):
        self.books = []
    
    def add_book(self, book):
        #  if book already exists
        for b in self.books:
            if b.isbn == book.isbn:
                print(f"Book with ISBN {book.isbn} already exists!")
                return False
        
        self.books.append(book)
        print(f"Added: {book.title}")
        return True
    
    def find_book(self, isbn):
        #Find book by ISBN
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    def borrow_book(self, isbn):
        book = self.find_book(isbn)
        
        if book is None:
            print(f"Book with ISBN {isbn} not found")
            return False
        
        if not book.is_available:
            print(f"'{book.title}' is already borrowed")
            return False
        
        book.is_available = False
        print(f"You borrowed: {book.title}")
        return True
    
    def return_book(self, isbn):
        book = self.find_book(isbn)
        
        if book is None:
            print(f"Book with ISBN {isbn} not found")
            return False
        
        book.is_available = True
        print(f"You returned: {book.title}")
        return True
    
    def remove_book(self, isbn):
        #Remove book from library
        book = self.find_book(isbn)
        
        if book is None:
            print(f"Book with ISBN {isbn} not found")
            return False
        
        if not book.is_available:
            print(f"Cannot remove '{book.title}' - currently borrowed")
            return False
        
        self.books.remove(book)
        print(f"Removed: {book.title}")
        return True
    
    def list_books(self):
        #Display books
        if len(self.books) == 0:
            print("No books in library")
            return
        
        print("\nLibrary Books:")
        for book in self.books:
            status = "Available" if book.is_available else "Borrowed"
            print(f"  - {book.title} by {book.author} [{status}]")


def main():
    
    library = Library()
    
    
    print("=== Adding Books ===")
    book1 = Book("Python Basics", "John Doe", "001")
    book2 = Book("Java Programming", "Jane Smith", "002")
    book3 = Book("Data Science", "Bob Johnson", "003")
    
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    
    # Try  duplicate
    duplicate = Book("Python Basics", "John Doe", "001")
    library.add_book(duplicate)
    
    # List books
    library.list_books()
    
    # Borrow books
    print("\n=== Borrowing Books ===")
    library.borrow_book("001")
    library.borrow_book("002")
    library.borrow_book("001")  
    
    # List books
    library.list_books()
    
    # Return book
    print("\n=== Returning Books ===")
    library.return_book("001")
    
    # Remove book
    print("\n=== Removing Books ===")
    library.remove_book("002")  
    library.remove_book("003")  
    
    # Final list
    library.list_books()


if __name__ == "__main__":
    main()