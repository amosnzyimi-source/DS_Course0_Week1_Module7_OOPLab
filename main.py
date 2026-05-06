# CodeGrade step1
# Replace none with your code
# Define the class and create the __init__ method
class LibraryItem():
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

        # CodeGrade step2
# Define and implement the three methods within your class
# Copy your init method from step 1
class LibraryItem:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.is_available = True

    def display_info(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.publication_year}, Available: {self.is_available}")

    def checkout(self):
        self.is_available = False

    def return_item(self):
        self.is_available = True

        # CodeGrade step3
# Define new Book class that inherits from LibraryItem
# Replace none with your code
class Book(LibraryItem):
    def __init__(self, title, author, publication_year, isbn, publisher):
     
        super().__init__(title, author, publication_year)
       
        self.isbn = isbn
        self.publisher = publisher

    def display_info(self):
       
        super().display_info()
      
        print(f"ISBN: {self.isbn}, Publisher: {self.publisher}")

        # CodeGrade step4
# Define new Magazine class that inherits from LibraryItem
# Replace none with your code
class Magazine(LibraryItem):
    def __init__(self, title, author, publication_year, issue_number, publication_month):
        super().__init__(title, author, publication_year)
        self.issue_number = issue_number
        self.publication_month = publication_month
    
    def display_info(self):
        super().display_info()
        print(f"Issue Number: {self.issue_number}, Month: {self.publication_month}")

        # CodeGrade step5
# Define new DVD class that inherits from LibraryItem
# Replace none with your code
class DVD(LibraryItem):
    def __init__(self, title, publication_year, duration, director, genres, author='N/A'):
        super().__init__(title, author, publication_year)
        self.duration = duration
        self.director = director
        self.genres = genres
    
    def add_genre(self, genre):
        self.genres.add(genre)
    
    def display_info(self):
        super().display_info()
        print(f"Director: {self.director}, Duration: {self.duration} mins, Genres: {self.genres}")

        # Run this cell without changes
book1 = Book(title='Dracula', author='Bram Stoker', publication_year=1897, 
             isbn=1000, publisher='Archibald')

magazine1 = Magazine(title='Forbes', author='Many', publication_year=2021, 
                     issue_number=10, publication_month='February')

dvd1 = DVD(title='The Matrix', publication_year=1999, duration=136, 
           director='The Wachowskis', genres={'action', 'sci-fi'})

# Your code here
print("--- Book Info ---")
book1.display_info()

print("\n--- Magazine Info ---")
magazine1.display_info()

print("\n--- DVD Info ---")
dvd1.display_info()
# Your code here
print("\n--- Testing Availability ---")
print(f"Initial availability: {book1.is_available}")
book1.checkout()
print(f"After checkout: {book1.is_available}")
book1.return_item()
print(f"After return: {book1.is_available}")

# Your code here
print("\n--- Testing DVD Genres ---")
print(f"Genres before: {dvd1.genres}")
dvd1.add_genre('thriller')
print(f"Genres after: {dvd1.genres}")