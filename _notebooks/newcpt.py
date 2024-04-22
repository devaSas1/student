library = []

def addbook(library):
    title = input("Enter the book's title: ")
    author = input("Enter the book's author: ")
    year = input("Enter the book's year of publication: ")
    book = {"title": title, "author": author, "year": year}
    library.append(book)
    print("Book Added")
