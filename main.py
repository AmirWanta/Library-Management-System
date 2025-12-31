from library import Library
from book import Book

lib = Library()


def menu():
    print('MENU: \n1) List of Books' \
    '\n2) Search Books' \
    '\n3) Borrow Books' \
    '\n4) Return Books' \
    '\n 5) Add Book' \
    '\n6) Exit')

def main():
    while True:
        menu()
        choice = input("Which option would you like to use today?").strip()
                
        if choice == "1":
            books = lib.list_books()
            for book in books:
                print(book.id, book.title, book.author, book.category)
        elif choice == "2":
            keyword = input('What book would you like to find?').strip()
            result = lib.search_books(keyword)

            if not result:
                print('No books found.')
            else:
                for book in result:
                    print(book.title)

        
        elif choice == "3":
            
            book_id = input("What's the book id you would like to borrow?").upper().strip()
            borrower_name = input('What is the borrower name?').strip()

            success = lib.borrow_book(book_id, borrower_name)

            if success:
                print('Book borrowed successfully')
            else:
                print("Borrowed failed, it's either being borrowed or already borrowed")
        elif choice == "4":

            book_id = input('What is the id of your book').strip().upper()

            success = lib.return_book(book_id)

            if success:
                print('Your book was successfully returned')
            else:
                print('There was an error returning your book please call')
        elif choice == "5":
            newBookID = input('Please input the ID for the book').upper().strip()
            newTitle = input('What is the title of this book?').strip()
            newAuthor = input('Who is the author?').strip()
            newCategory = input('What is the category?').strip()

            book = Book(newBookID, newTitle, newAuthor, newCategory)

            success = lib.add_book(book)

            if success:
                print('Successfully added!')
            else:
                print('Failed to add please call')
        
        elif choice == "6":
            print('Thank you please visit again')
            break
        else:
            print('INVALID Please try again')
         
if __name__ == "__main__":
    main()