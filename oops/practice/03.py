class Library:
    def __init__(self,book_count):
        self.availabe_books = book_count

    def add_book(self):
        new_book_count = int(input("Enter the number of books you want to add: "))
        self.availabe_books += new_book_count
        return f"{new_book_count} books added successfully!"
    def issue_book(self):
        issued_book_count = int(input("Enter the number of books you want to take: "))
        self.availabe_books -= issued_book_count
        return f"{issued_book_count} books issued successfully"
    def book_count(self):
        return f"Availabe Books: {self.availabe_books}"
    
p1 = Library(5)
print(p1.add_book())
print(p1.issue_book())
print(p1.book_count())

