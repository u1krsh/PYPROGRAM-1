class Library:
    def __init__(self,name):
        self.name = name
        self.books = []
        
    def add_books(self,books):
        self.books.append(books)
    
    def list_books(self):
        return [f"{book.title} by{book.author}"for book in self.books]

class Book:
    def __call__(self, title, author):
        self.title = title
        self.author = author
        
lib = Library("SIST Library")

book1 = Book("Harry Potter","JK Rowling")
book2 = Book("The Hobbit","JRR Tolkien")
book3 = Book("Color of magic","Terry Pratchett")

Library.addBook(book1)