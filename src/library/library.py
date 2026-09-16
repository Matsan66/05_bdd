class Library:
    """
    Represents a library of books
    """
    def __init__(self):
        self.books = []

    # ------------------------------------------------------------

    def add_book(self, book):
        """
        Adds a book to the library
        :param book: The book to add
        """
        self.books.append(book)

    # ------------------------------------------------------------

    def search_by_title(self, title):
        """
        Search books by title
        :param title: Book title to search for
        :return: A list of books or an empty list
        """
        found_books = []
        for book in self.books:
            if book.title == title:
                found_books.append(book)

        return found_books

    # ------------------------------------------------------------

    def search_by_author(self, author):
        """
        Search books by author
        :param author: Book author to search for
        :return: A list with books by found authors or an empty list
        """
        found_books = []

        for book in self.books:
            if book.author == author:
                found_books.append(book)

        return found_books

    # ------------------------------------------------------------

    def borrow_book(self, title):
        """
        Borrows a book if available
        :param title: The book to borrow
        :return: The book to borrow or None
        """

        found_books = self.search_by_title(title)

        for book in found_books:
            if book.is_available:
                book.is_available = False
                return book

        return None

    # ------------------------------------------------------------

    def return_book(self, title):
        """
        Returns a book if borrowed
        :param title: The book to return
        :return: The book returned or None
        """

        found_books = self.search_by_title(title)

        for book in found_books:
            if not book.is_available:
                book.is_available = True
                return book

        return None

    # ------------------------------------------------------------

    def is_book_borrowed(self, title):
        """
        Returns if a book is borrowed or not
        :param title: The book to check
        :return: True if the book is borrowed, False otherwise
        """

        found_books = self.search_by_title(title)

        for book in found_books:
            if not book.is_available:
                return True

        return False
