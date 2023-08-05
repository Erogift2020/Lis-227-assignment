class Book:
    def __init__(self, title, author, genre, book_id):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_id = book_id
        self.is_available = True

    def __str__(self):
        availability = "Available" if self.is_available else "Borrowed"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Availability: {availability}"


class Library:
    def __init__(self):
        self.books = {}
        self.next_book_id = 1

    def add_book(self, title, author, genre):
        book = Book(title, author, genre, self.next_book_id)
        self.books[self.next_book_id] = book
        self.next_book_id += 1
        print(f"Book '{title}' added with ID {book.book_id}")

    def borrow_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if book.is_available:
                book.is_available = False
                print(f"Book '{book.title}' with ID {book_id} has been borrowed.")
            else:
                print(f"Book '{book.title}' with ID {book_id} is already borrowed.")
        else:
            print(f"Book with ID {book_id} not found in the library.")

    def return_book(self, book_id):
        if book_id in self.books:
            book = self.books[book_id]
            if not book.is_available:
                book.is_available = True
                print(f"Book '{book.title}' with ID {book_id} has been returned.")
            else:
                print(f"Book '{book.title}' with ID {book_id} is already available in the library.")
        else:
            print(f"Book with ID {book_id} not found in the library.")

    def display_books(self):
        if not self.books:
            print("Library is empty.")
        else:
            print("Books in the library:")
            for book in self.books.values():
                print(book)

    def search_book_by_title(self, title):
        found_books = [book for book in self.books.values() if title.lower() in book.title.lower()]
        if found_books:
            print(f"Books matching the title '{title}':")
            for book in found_books:
                print(book)
        else:
            print(f"No books found with the title '{title}' in the library.")

    def search_book_by_author(self, author):
        found_books = [book for book in self.books.values() if author.lower() in book.author.lower()]
        if found_books:
            print(f"Books by the author '{author}':")
            for book in found_books:
                print(book)
        else:
            print(f"No books found by the author '{author}' in the library.")


def main():
    library = Library()

    while True:
        print("\n===== Library Management Menu =====")
        print("1. Add a Book")
        print("2. Borrow a Book")
        print("3. Return a Book")
        print("4. Display All Books")
        print("5. Search by Title")
        print("6. Search by Author")
        print("7. Exit")

        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            title = input("Enter the book title: ")
            author = input("Enter the book author: ")
            genre = input("Enter the book genre: ")
            library.add_book(title, author, genre)

        elif choice == "2":
            book_id = int(input("Enter the book ID to borrow: "))
            library.borrow_book(book_id)

        elif choice == "3":
            book_id = int(input("Enter the book ID to return: "))
            library.return_book(book_id)

        elif choice == "4":
            library.display_books()

        elif choice == "5":
            title = input("Enter the title to search: ")
            library.search_book_by_title(title)

        elif choice == "6":
            author = input("Enter the author to search: ")
            library.search_book_by_author(author)

        elif choice == "7":
            print("Exiting Library Management. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
