class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"The Title is {self.title}, author is {self.author}, year is {self.year}"

# Child class
class LibraryBook(Book):
    def __init__(self, title, author, year, isbn, copies_available):
        super().__init__(title, author, year)
        self.isbn = isbn
        self.copies_available = copies_available

    def borrow_book(self):
        if self.copies_available > 0:
            self.copies_available -= 1
            return f"{self.title} borrowed. Copies left: {self.copies_available}"
        else:
            return f"No copies of {self.title} available"

    def return_book(self):
        self.copies_available += 1
        return f"{self.title} returned. Copies left: {self.copies_available}"

    def display_info(self):
        return str(self)  # Calls the __str__ method from Book

# Usage
book1 = LibraryBook("Atomic Habits", "James Clear", 2005, 123, 20)

# Display book information
print(book1.display_info())

# Borrow the book
print(book1.borrow_book())

# Return the book
print(book1.return_book())
