class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False


class Library:
    def __init__(self):
        self.__books = []
    
    def add_book(self, book):
        if isinstance(book, Book):
            self.__books.append(book)
        else:
            print("Only Book instances can be added.")

    def check_out_book(self, title):
        for book in self.__books:
            if (book.title == title and book._is_checked_out == False):
                book._is_checked_out = True
                print(f"{title} checked out")
            else:
                print(f"{title} is not available")

    def return_book(self, title):
        for book in self.__books:
            if (book.title == title and book._is_checked_out == True):
                book._is_checked_out = False
                print(f"{title} Returned")
            else:
                print(f"{title} is not not checked out")

    def list_available_books(self):
            for book in self.__books:
                if (book._is_checked_out == False):
                    print(f"{book.title} by {book.author}")
