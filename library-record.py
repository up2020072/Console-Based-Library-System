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
        
    def set_title(self, title):
        """Set the title of the book."""
        if not title:
            raise ValueError("\nTitle cannot be empty.")
        self.title = title

    def set_author(self, author):
        """Set the author of the book."""
        if not author:
            raise ValueError("\nAuthor cannot be empty.")
        self.author = author

    def set_year(self, year):
        """Set the year of publication."""
        if isinstance(year, int) and year > 0:
            self.year = year
        else:
            raise ValueError("\nYear must be a positive integer.")

    def set_publisher(self, publisher):
        """Set the publisher of the book."""
        if not publisher:
            raise ValueError("\nPublisher cannot be empty.")
        self.publisher = publisher

    def set_num_available(self, num_available):
        """Set the number of available copies."""
        if num_available.isnumeric() and int(num_available) >= 0: #this should be reworked
            self.num_avaialble = num_available
        else:
            raise ValueError("\nNumber of copies must be a non-negative integer.")
    
    def set_num_copies(self, num_total):
        """Set the number of total copies."""
        if num_total.isnumeric() and int(num_total) >= 0: #this should be reworked
            self.num_total = num_total
        else:
            raise ValueError("\nNumber of copies must be a non-negative integer.")

    def set_publication_date(self, publication_date):
        """Set the publication date of the book."""
        if isinstance(publication_date, str):
            self.publication_date = publication_date
        else:
            raise ValueError("\nPublication date must be a string.")
        
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

    def get_num_available(self):
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
    
    def __iter__(self):
        """Allow iteration over the books in the BookList."""
        return iter(self.books.items())
    
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

    def set_username(self, username):
        if not username:
            raise ValueError("\nUsername cannot be empty")
        self.username = username

    def set_firstname(self, firstname):
        if not firstname:
            raise ValueError("\nFirstname cannot be empty")
        self.firstname = firstname

    def set_lastname(self, lastname):
        if not lastname:
            raise ValueError("\nLastname cannot be empty")
        self.lastname = lastname

    def set_house_num(self, house_num):
        if house_num.isnumeric() and int(house_num) >= 0:
            self.house_num = house_num
        else:
            raise ValueError("\nHouse number must be a non negative integer")

    def set_street_name(self, street_name):
        if not street_name:
            raise ValueError("\nStreet name cannot be empty")
        self.street_name = street_name

    def set_postcode(self, postcode):
        if not postcode:
            raise ValueError("\nPostcode cannot be empty")
        self.postcode = postcode

    def set_email(self, email):
        if not email:
            raise ValueError("\nEmail cannot be empty")
        self.email = email

    def set_lastname(self, dob):
        if not dob:
            raise ValueError("\nDate of birth cannot be empty")
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
    
    def __iter__(self):
        """Allow iteration over the users in the UserList."""
        return iter(self.users.items())

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
    


# print(f'{booklist.get_total_books()} total books')
# print(f'{userlist.get_total_users()} total users')

# # searchtest = booklist.find_book("James Bond")
# # for b in searchtest:
# #     print(b)

# #userlist.remove_user("Tim")
# bookloans.borrow_book(user2.username, book1)
# print(f'{user2.username} is currently borrowing {bookloans.count_borrowed_books(user2.username)} books')

def modify_book(book_list):
    """Modify a book's details."""
    try:
        print("\nBook List:")
        for book_id, book in list(book_list): print(book)
        book_id = int(input("\nEnter the Book ID of the book you want to modify:\n"))
        book = book_list.books.get(book_id)

        if not book:
            print(f"\nNo book found with ID: {book_id}\n")
            main()
    except ValueError:
            print("\nInvalid input. Please enter a valid ID.")
            modify_book(book_list)

    print(f'\nCurrent details:\n{book}')

    while True:
        print("\nWhat would you like to modify?")
        print("1. Title")
        print("2. Author")
        print("3. Year")
        print("4. Publisher")
        print("5. Number of Copies")
        print("6. Exit")

        try:
            choice = input("\nEnter your choice (1-6):\n")

            if choice == '1':
                new_title = input("\nEnter new title:\n")
                book.set_title(new_title)
                break
            elif choice == '2':
                new_author = input("\nEnter new author:\n")
                book.set_author(new_author)
                break
            elif choice == '3':
                new_year = (input("\nEnter new year:\n"))
                book.set_year(new_year)
                break
            elif choice == '4':
                new_publisher = input("\nEnter new publisher:\n")
                book.set_publisher(new_publisher)
                break
            elif choice == '5':
                new_copies = (input("\nEnter new number of copies:\n"))
                book.set_num_copies(new_copies)
                break
            elif choice == '6':
                main()
            else:
                print("Invalid choice. Please select again.\n")
        except ValueError as e:
            print(e)

    print("\nBook details updated successfully.\n")
    print(f'New details:\n{book}')
    main()

def modify_user(user_list):
    """Modify a user's details."""
    try:
        print("\nUser List:")
        for user_id, user in list(user_list): print(user)
        username = input("\nEnter the username of the user you want to modify:\n")
        user = user_list.users.get(username)

        if not user:
            print(f"\nNo user found with username: {username}\n")
            main()

    except ValueError:
            print("\nInvalid input. Please enter a valid username.")
            modify_book(user_list)

    print(f'\nCurrent details:\n{user}')

    while True:
        print("\nWhat would you like to modify?")
        print("1. First Name")
        print("2. Surname")
        print("3. House Number")
        print("4. Street Name")
        print("5. Postcode")
        print("6. Exit")

        try:
            choice = input("\nEnter your choice (1-6): \n")

            if choice == '1':
                new_firstname = input("\nEnter new first name:\n")
                user.set_firstname(new_firstname)
                break
            elif choice == '2':
                new_surname = input("\nEnter new surname:\n")
                user.set_lastname(new_surname)
                break
            elif choice == '3':
                new_house_number = input("\nEnter new house number:\n")
                user.set_house_num(new_house_number)
                break
            elif choice == '4':
                new_street_name = input("\nEnter new street name:\n")
                user.set_street_name(new_street_name)
                break
            elif choice == '5':
                new_postcode = input("\nEnter new postcode:\n")
                user.set_postcode(new_postcode)
                break
            elif choice == '6':
                main()
            else:
                print("Invalid choice. Please select again.\n")
        except ValueError as e:
            print(e)

    print("\nUser details updated successfully.\n")
    print(f'New details:\n{user}')
    main()

def init_library():

    #this could be done with a json file

    book_list = BookList()
    user_list = UserList()
    book_loans = Loans()

    book_list.add_book(Book("The Hobbit", "John Doe", 1960, "Books Inc", 12, "1960-02-24"))
    book_list.add_book(Book("James Bond", "John Doe", 1930, "Blob Corp", 5, "1930-01-12"))
    book_list.add_book(Book("1984", "Max Smith", 1930, "Big Publishing", 5, "2008-09-07"))

    user_list.add_user(User("raringgarlic118", "Tim", "Lee", 12, "Park avenue", "BO21HK", "timlee@email.com","2000-01-01"))
    user_list.add_user(User("blobfish772", "Tim", "Lee", 1, "river avenue", "OJ6XKG", "timlee2@email.com","2002-11-31"))
    user_list.add_user(User("firequake122", "Bob", "Smith", 1, "birch street", "YTH87P", "bobsmith122@email.com","1992-06-19"))

    # print(f'{book_list.get_total_books()} total books')
    # print(f'{user_list.get_total_users()} total users')

    return book_list, user_list, book_loans

def main():
    book_list, user_list, book_loans, = init_library()
    print("\nWelcome to the Library System!")
    while True:
        print(f'1. Modify a Book\n'
              f'2. Modify a User\n'
              f'3. Exit\n')
        try:
            choice = int(input("Please specify which option you would like (enter the number): \n"))
            if choice == 1:
                modify_book(book_list)
                break
            elif choice == 2:
                modify_user(user_list)
                break
            elif choice == 3:
                break
            else:
                print("\nInvalid input, please pick one of the following options.")
        except ValueError:
                print("\nInvalid input. Please enter a valid number.")

if __name__ == '__main__':
    main()