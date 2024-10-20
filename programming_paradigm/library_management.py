class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False


class Library:
    def __init__(self):
        self._books = []
    
    def add_book(self, book):
        if isinstance(book, Book):
            self._books.append(book)
        else:
            print("Only Book instances can be added.")

    def check_out_book(self, title):
        for book in self._books:
            if (book.title == title and book._is_checked_out == False):
                book._is_checked_out = True
                print(f"{title} checked out")
                break
        else:
            print(f"{title} is not available")

    def return_book(self, title):
        for book in self._books:
            if (book.title == title and book._is_checked_out == True):
                book.return_book()
                print(f"{title} Returned")
                break
        else:
            print(f"{title} is not not checked out")

    def list_available_books(self):
            for book in self._books:
                if (book._is_checked_out == False):
                    print(f"{book.title} by {book.author}")
