class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    def display_book_details(self):
        print(f"Title: {self.title}\nAuthor: {self.author}\nISBN: {self.isbn}")
def create_book_details():
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    isbn = input("Enter the ISBN of the book: ")
    book = Book(title,author,isbn)
    return book
def main():
    Books=[]
    while True:
        Books.append(create_book_details())
        choice = input("Do you want to add more books? (y/n): ")
        if choice == 'n' or choice == 'N':
            break
    for i in Books:
        i.display_book_details()
    
main()