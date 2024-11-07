class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def mark_as_borrowed(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            return f"{self.title} has been borrowed."
        else:
            return f"{self.title} is already borrowed."

    def mark_as_returned(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"{self.title} has been returned."
        else:
            return f"{self.title} was not borrowed."


class LibraryMember:
    def __init__(self, name, member_id):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = []

    def borrow_book(self, book):
        if not book.is_borrowed:
            self.borrowed_books.append(book)
            return book.mark_as_borrowed()
        else:
            return f"Sorry, {book.title} is currently borrowed by someone else."

    def return_book(self, book):
        if book in self.borrowed_books:
            self.borrowed_books.remove(book)
            return book.mark_as_returned()
        else:
            return f"{self.name} did not borrow {book.title}."

    def list_borrowed_books(self):
        if self.borrowed_books:
            return f"Books borrowed by {self.name}:\n" + "\n".join(
                f" - {book.title} by {book.author}" for book in self.borrowed_books
            )
        else:
            return f"{self.name} has not borrowed any books."


if __name__ == "__main__":
    
    books = [
        Book("1984", "George Orwell"),
        Book("To Kill a Mockingbird", "Harper Lee"),
        Book("The Great Gatsby", "F. Scott Fitzgerald")
    ]
    member = LibraryMember("Alice", "M001")

    while True:
        print("\nLibrary Management System:")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. List Borrowed Books")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            print("Available books:")
            for idx, book in enumerate(books, start=1):
                status = "Available" if not book.is_borrowed else "Borrowed"
                print(f"{idx}. {book.title} by {book.author} - {status}")
            book_choice = int(input("Enter the book number to borrow: ")) - 1
            if 0 <= book_choice < len(books):
                print(member.borrow_book(books[book_choice]))
            else:
                print("Invalid choice.")

        elif choice == '2':
            if member.borrowed_books:
                print("Your borrowed books:")
                for idx, book in enumerate(member.borrowed_books, start=1):
                    print(f"{idx}. {book.title} by {book.author}")
                return_choice = int(input("Enter the book number to return: ")) - 1
                if 0 <= return_choice < len(member.borrowed_books):
                    print(member.return_book(member.borrowed_books[return_choice]))
                else:
                    print("Invalid choice.")
            else:
                print("No books to return.")

        elif choice == '3':
            print(member.list_borrowed_books())

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")
