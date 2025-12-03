import json
from pathlib import Path
from json import JSONDecodeError
from .book import Book

class LibraryInventory:
    def __init__(self, data_file):
        self.data_file = Path(data_file)
        self.books = []
        self.load_from_file()

    def add_book(self, book):
        self.books.append(book)
        self.save_to_file()

    def search_by_title(self, title):
        title = title.lower()
        return [b for b in self.books if title in b.title.lower()]

    def search_by_isbn(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                return b
        return None

    def display_all(self):
        if not self.books:
            print("No books in inventory.")
        else:
            for b in self.books:
                print(b)

    def issue_book(self, isbn):
        b = self.search_by_isbn(isbn)
        if b and b.is_available():
            b.issue()
            self.save_to_file()
            return True
        return False

    def return_book(self, isbn):
        b = self.search_by_isbn(isbn)
        if b:
            b.return_book()
            self.save_to_file()
            return True
        return False

    def save_to_file(self):
        data = [b.to_dict() for b in self.books]
        try:
            with self.data_file.open("w") as f:
                json.dump(data, f)
        except:
            pass

    def load_from_file(self):
        if not self.data_file.exists():
            self.books = []
            return
        try:
            with self.data_file.open("r") as f:
                data = json.load(f)
            self.books = [Book.from_dict(d) for d in data]
        except (JSONDecodeError, FileNotFoundError):
            self.books = []
