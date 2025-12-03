from library_manager import LibraryInventory, Book
from pathlib import Path

def menu():
    print("\n1. Add Book")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. View All")
    print("5. Search")
    print("6. Exit")

def add_book_cli(inv):
    title = input("Title: ")
    author = input("Author: ")
    isbn = input("ISBN: ")
    if not title or not author or not isbn:
        print("Invalid input.")
        return
    if inv.search_by_isbn(isbn):
        print("Book exists.")
        return
    b = Book(title, author, isbn)
    inv.add_book(b)
    print("Added.")

def issue_book_cli(inv):
    isbn = input("ISBN: ")
    if inv.issue_book(isbn):
        print("Issued.")
    else:
        print("Not available.")

def return_book_cli(inv):
    isbn = input("ISBN: ")
    if inv.return_book(isbn):
        print("Returned.")
    else:
        print("Not found.")

def search_cli(inv):
    print("1. Title")
    print("2. ISBN")
    c = input("Choice: ")
    if c == "1":
        t = input("Enter title: ")
        res = inv.search_by_title(t)
        if res:
            for b in res:
                print(b)
        else:
            print("No results.")
    elif c == "2":
        isbn = input("ISBN: ")
        b = inv.search_by_isbn(isbn)
        if b:
            print(b)
        else:
            print("Not found.")
    else:
        print("Invalid.")

def main():
    inv = LibraryInventory(Path("books.json"))
    while True:
        menu()
        choice = input("Enter choice: ")
        if choice == "1":
            add_book_cli(inv)
        elif choice == "2":
            issue_book_cli(inv)
        elif choice == "3":
            return_book_cli(inv)
        elif choice == "4":
            inv.display_all()
        elif choice == "5":
            search_cli(inv)
        elif choice == "6":
            break
        else:
            print("Invalid.")

if __name__ == "__main__":
    main()
