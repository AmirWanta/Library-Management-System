import json
from book import Book
from datetime import date

class Library:

    def __init__(self, filePath="data/books.json"):
        self.filePath = filePath
        self.books = [] #array of objects
        self.load_books()

    ##this function will be in the constructor so that if we wanna load data, it won't be empty
    def load_books(self):
        with open(self.filePath, 'r') as f:
            data = json.load(f)

        for book in data:
            newBook = Book.toConstruct(book)
            self.books.append(newBook)

    def save_books(self):

        bookToSave = []

        for book in self.books:
            book = Book.to_dict(book)
            bookToSave.append(book)

        with open(self.filePath, 'w') as f:
            json.dump(bookToSave, f, indent=2)        

    def get_book_id(self, input_id):
        for book in self.books:
            if book.id == input_id:
                return book
        return None
            
    def list_books(self):
        return self.books
    
    def borrow_book(self, book_id, borrower_name):
        book = self.get_book_id(book_id)
        
        if book is None:
            return False
        
        if book and book.is_borrowed == True:
            return False
        
        book.is_borrowed = True
        book.borrowed_by = borrower_name
        book.borrowed_date = date.today().isoformat()

        self.save_books()
        return True

    def return_book(self, book_id):
        book = self.get_book_id(book_id)

        if book is None:
            return False
        
        if book.is_borrowed == False:
            return False
        
        book.is_borrowed = False
        book.borrowed_by = ""
        book.borrowed_date = None

        self.save_books()
        
        return True

    def add_book(self, book):
        check = self.get_book_id(book.id)

        if check:
            return False
        
        self.books.append(book)
        self.save_books()
        return True

    def search_books(self,keyword):
        keyword = keyword.strip().lower()
        results = []

        
        for book in self.books:
            if  (
                keyword in book.id.lower() or
                keyword in book.title.lower() or
                keyword in book.author.lower() or
                keyword in book.category.lower()
            ):

                results.append(book)

        return results

            
