import random
from datetime import datetime, timedelta

class Book():
    def __init__(self, title, author, year, publisher, num_total, publication_date):
        #for consistency this needs a docstring
        #might be smart to use setter methods to automatically validate object construction

        self.id = random.randint(0, 9999)
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher 
        self.num_total = num_total
        self.num_avaialble = num_total
        self.publication_date = publication_date
        booklist.add_book(self)
        
    def set_title(self, title):
        """Set the title of the book."""
        if not title:
            raise ValueError("Title cannot be empty.")
        self.title = title

    def set_author(self, author):
        """Set the author of the book."""
        if not author:
            raise ValueError("Author cannot be empty.")
        self.author = author

    def set_year(self, year):
        """Set the year of publication."""
        if isinstance(year, int) and year > 0:
            self.year = year
        else:
            raise ValueError("Year must be a positive integer.")

    def set_publisher(self, publisher):
        """Set the publisher of the book."""
        if not publisher:
            raise ValueError("Publisher cannot be empty.")
        self.publisher = publisher

    def set_num_available(self, num_available):
        """Set the number of available copies."""
        if isinstance(num_available, int) and num_available >= 0: #this should be reworked
            self.num_avaialble = num_available
        else:
            raise ValueError("Number of copies must be a non-negative integer.")

    def set_publication_date(self, publication_date):
        """Set the publication date of the book."""
        if isinstance(publication_date, str):
            self.publication_date = publication_date
        else:
            raise ValueError("Publication date must be a string.")
        
    def get_title(self):
        """Return the title of the book."""
        return self.title

    def get_author(self):
        """Return the author of the book."""
        return self.author

    def get_year(self):
        """Return the year of publication."""
        return self.year

    def get_publisher(self):
        """Return the publisher of the book."""
        return self.publisher

    def get_num_copies(self):
        """Return the total number of copies of the book."""
        return self.num_copies

    def get_available_copies(self):
        """Return the number of available copies of the book."""
        return self.available_copies

    def get_publication_date(self):
        """Return the publication date of the book."""
        return self.publication_date

    def __str__(self):
        """Return a string representation of the book record."""
        return (f"Book ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\n"
                f"Year: {self.year}\nPublisher: {self.publisher}\n"
                f"Total Copies: {self.num_total}\nAvailable Copies: {self.num_avaialble}\n"
                f"Publication Date: {self.publication_date}\n")

class BookList():
    def __init__(self):
        self.books = {} # Store books with book_id as key

    def add_book(self, book):
        """Store a new book instance in the collection."""
        self.books[book.id] = book

    def remove_book(self, title): # this should user the code style in the function below for brevity
        """Remove a book from the collection by title."""
        for book_id, book in list(self.books.items()):
            if book.get_title().lower() == title.lower():
                del self.books[book_id]
                return f"'{title}' was removed from the book list."
        return f"Book with title:'{title}', could not be found."

    def find_book(self, search): #returns a list of books meeting the criteria
        #find book by search term
        book_to_find = [book for book in self.books.values() if search in (book.title, book.author, book.publisher, book.publication_date)]
        if not book_to_find:
            return [f'No books found with the search term: {search}']
        else:
            return [f'\n{len(book_to_find)} books found with the search term found:\n'] + book_to_find

    def get_total_books(self):
        """Return the total number of books stored in the collection."""
        return len(self.books)
    
class User():
    def __init__(self, username, firstname, lastname, house_num, street_name, postcode, email, dob):
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.house_num = house_num
        self.street_name = street_name
        self.postcode = postcode
        self.email = email
        self.dob = dob #date of birth
        userlist.add_user(self)

    def set_username(self, username):
        if not username:
            raise ValueError("Username cannot be empty")
        self.username = username

    def set_firstname(self, firstname):
        if not firstname:
            raise ValueError("Firstname cannot be empty")
        self.firstname = firstname

    def set_lastname(self, lastname):
        if not lastname:
            raise ValueError("Lastname cannot be empty")
        self.lastname = lastname

    def set_house_num(self, house_num):
        if not house_num or not isinstance(house_num, int):
            raise ValueError("House number must be a non negative integer")
        self.house_num = house_num

    def set_street_name(self, street_name):
        if not street_name:
            raise ValueError("Street name cannot be empty")
        self.street_name = street_name

    def set_postcode(self, postcode):
        if not postcode:
            raise ValueError("Postcode cannot be empty")
        self.postcode = postcode

    def set_email(self, email):
        if not email:
            raise ValueError("Email cannot be empty")
        self.email = email

    def set_lastname(self, dob):
        if not dob:
            raise ValueError("Date of birth cannot be empty")
        self.dob = dob

    def get_username(self):
        return self.username
    
    def get_firstname(self):
        return self.firstname
    
    def get_lastname(self):
        return self.lastname
    
    def get_house_num(self):
        return self.house_num
    
    def get_street_name(self):
        return self.street_name
    
    def get_postcode(self):
        return self.postcode
    
    def get_email(self):
        return self.email
    
    def get_dob(self):
        return self.dob

    def __str__(self):
        """Return a string representation of the user record."""
        return (f"Username: {self.username}\nFirstname: {self.firstname}\nLastname: {self.lastname}\n"
                f"House Number: {self.house_num}\nStreen Name: {self.street_name}\n"
                f"Postcode: {self.postcode}\nEmail: {self.email}\n"
                f"Date of Birth: {self.dob}\n")

    
class UserList():
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        """Store a new user instance in the collection."""
        self.users[user.username] = user

    def remove_user(self, firstname):
        """Remove a user from the collection by first name."""
        #include option to pick between options, if two users exist with the same first name
        #display their full details when doing this along with select option [1/2/3/...]
        users_to_remove = [user for user in self.users.values() if firstname in (user.firstname)]
        if not users_to_remove:
            print(f'\nNo users found with the firstname: {firstname}\n')
        elif len(users_to_remove) == 1:
            del self.users[users_to_remove[0].username]
            print(f"\nUser with firstname: '{firstname}' removed.\n")
        else:
            print(f"\nMultiple users found with the first name '{firstname}'")

            for i, user in enumerate(users_to_remove, 1):
                print(f"{i}. {user.firstname} {user.lastname} (Username: {user.username})")

            try:
                choice = int(input("Please specify which user to remove (enter the number): "))
                if 1 <= choice <= len(users_to_remove):
                    selected_user = users_to_remove[choice - 1]
                    del self.users[selected_user.username]
                    return f"User '{selected_user.firstname} {selected_user.lastname}' removed."
                else:
                    return "Invalid selection. No user removed."
            except ValueError:
                return "Invalid input. Please enter a valid number."

    def get_total_users(self):
        """Return the total number of users in the system."""
        return len(self.users)
    
    def get_user(self, username):
        """Return user details by username."""
        return self.users.get(username, None)

class Loans():
    def __init__(self):
        self.loans = {} #dictionary with username as key and array of borrowed books as value
    
    def borrow_book(self, username, book):
        """Allow a user to borrow a book."""
        if username not in self.loans:
            self.loans[username] = []
        self.loans[username].append(book)
    
    def return_book(self, username, book_id):
        """Allow a user to return a book."""
        if username in self.loans:
            for book in self.loans[username]:
                if book.book_id == book_id:
                    self.loans[username].remove(book)
                    return f"Book '{book.get_title()}' returned."
        return "Book not found."
    
    def count_borrowed_books(self, username):
        """Count and return the total number of books a user is currently borrowing."""
        return len(self.loans.get(username, []))
    
    def overdue_books(self):
        """Print out all overdue books along with the users’ details."""
        #might need to send the lecturer a message about this
        #nowhere else is due dates for books explicitly mentioned
        #this isnt hard to implement but worth checking

        return
    


booklist = BookList()
book1 = Book("The Hobbit", "John Doe", 1960, "Books Inc", 12, "1960-02-24")
book2 = Book("James Bond", "John Doe", 1930, "Blob Corp", 5, "1930-01-12")
book3 = Book("1984", "Max Smith", 1930, "Big Publishing", 5, "2008-09-07")

userlist = UserList()
user1 = User("raringgarlic118", "Tim", "Lee", 12, "Park avenue", "BO21HK", "timlee@email.com","2000-01-01")
user2 = User("blobfish772", "Tim", "Lee", 1, "river avenue", "OJ6XKG", "timlee2@email.com","2002-11-31")
user3 = User("firequake122", "Bob", "Smith", 1, "birch street", "YTH87P", "bobsmith122@email.com","1992-06-19")

bookloans = Loans()

print(f'{booklist.get_total_books()} total books')
print(f'{userlist.get_total_users()} total users')

# searchtest = booklist.find_book("James Bond")
# for b in searchtest:
#     print(b)

#userlist.remove_user("Tim")
bookloans.borrow_book(user2.username, book1)
print(f'{user2.username} is currently borrowing {bookloans.count_borrowed_books(user2.username)} books')
