# 1) Create a Book class with attributes for title, author, publisher, publication date, ISBN, and number of pages.
# 2) Create an Author class with attributes for name, birthdate, and nationality.
# 3) Create a Publisher class with attributes for name, location, and year founded.
# 4) Use inheritance to create a FictionBook class and a NonFictionBook class that inherit from the Book class.
# 5) Create an AbstractBook class with an abstract method for calculating the book’s price(don’t calculate here)
# 6) Inherit AbstractBook class in Fiction and Non-Fiction.
# 	6.1) Use this to calculate price using AbstractBook class.
# 7) Create a Singleton class for a library catalog that only allows one instance of the catalog to be created.
# 	7.1) Design pattern(
# 			A dictionary to store the library catalog's information.
# 			Add book, Remove book, Search Book, Display all books, Calculate total value)
# 8) Create a Factory class that can create instances of different book types based on user input.
# 	8.1) BookFactory class (Fiction /non Fiction)
# 9) A function to add,remove , display and calculate a book to the library's collection.
# 10) A loop to display a menu of options for the user to choose from
# 1. Add book
# 	2. Remove book
# 	3. Display all books
# 	4. Calculate total value of collection
# 	5. Exit
#
# A loop to allow the user to continue using the program until they choose to exit
from abc import ABC,abstractmethod
class Book:
    def __init__(self,title,author,publisher,publication_date,isbn,numpages):
        self.title = title
        self.author=author
        self.publisher=publisher
        self.publication_date=publication_date
        self.isbn = isbn
        self.numpages = numpages



class AbstractBook(ABC):
    @abstractmethod
    def calculate_price(self):
        pass

class Author:
    def __init__(self,name,birthdate,nationality):
        self.name=name
        self.birthdate=birthdate
        self.nationality=nationality

class Publisher:
    def __init__(self, name, location, year_founded):
        self.name = name
        self.location = location
        self.year_founded = year_founded

class FictionBook(Book,AbstractBook):
    def __init__(self,title,author,publisher,publication_date,isbn,numpages,genre):
        super().__init__(title,author,publisher,publication_date,isbn,numpages)
        self.genre=genre
    def calculate_price(self):
        return self.numpages * 0.02
class NonFiction(Book,AbstractBook):
    def __init__(self,title,author,publisher,publication_date,isbn,numpages,subject):
        super().__init__(title,author,publisher,publication_date,isbn,numpages)
        self.subject=subject

    def calculate_price(self):
        return self.numpages * 0.04

class LibraryCatalog:
    __instance=None
    catalog={}
    def __new__(cls):
        if cls.__instance is None:
            cls.__instance=super().__new__(cls)
        return  cls.__instance


    def add_book(self, book):
        self.catalog[book.isbn]=book

    def remove_book(self,isbn):
        if isbn in self.catalog:
            del self.catalog[isbn]
        else:
            print('Book Not Found')

    def display_book(self):
        for book in self.catalog.values():
            print(book.title)
            print(book.publisher)

def display_menu():
    print('1: Add Book')
    print('2:Remove') #crtl + D
    print('3: Search')
    print('4: Display all books')
    print('5: calculate')
    print('6: Exit')

if __name__=="__main__":
    catalog=LibraryCatalog()
    while True:
        display_menu()
        choice=input("Enter choice")
        if choice=='1':
            book_type=("Enter book type")
            title='xyx'
            author='xyz'
            publisher='abc'
            publication_date=("YYYY-MM-DD")
            isbn=22
            numpages=200



