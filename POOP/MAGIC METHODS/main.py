class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.pages == other.pages
        
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages
    
    def __add__(self, other):
        return self.pages + other.pages
    
    def __contains__(self, keyword):
        return keyword in self.title
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return "Invalid key"
book1 = Book("Python", "Guido van Rossum", 300)
book2 = Book("Harry potter","JK Rowling", 240)

print(book2)