import random
from datetime import datetime, timedelta
import uuid

class Book():
    def __init__(self, title, author, year, publisher, num_total, publication_date):
        #for consistency this needs a docstring
        #might be smart to use setter methods to automatically validate object construction

        self.id = uuid.uuid4()
        self.title = title.strip()
        self.author = author.strip()
        self.year = year
        self.publisher = publisher.strip()
        self.num_total = num_total
        self.num_available = num_total
        self.publication_date = publication_date #this might need to be an actual datetime
        
    def set_title(self, title):
        """Set the title of the book."""
        if not title:
            raise ValueError("\nTitle cannot be empty.")
        self.title = title.strip()

    def set_author(self, author):
        """Set the author of the book."""
        if not author:
            raise ValueError("\nAuthor cannot be empty.")
        self.author = author.strip()

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
        self.publisher = publisher.strip()

    def set_num_available(self, num_available):
        """Set the number of available copies."""
        if isinstance(num_available, int) and 0 <= num_available <= self.num_total: #this should be reworked
            self.num_avaialble = num_available
        else:
            raise ValueError("\nNumber of copies must be a non-negative integer.")
    
    def set_num_total(self, num_total):
        """Set the number of total copies."""
        if isinstance(num_total, int) and num_total >= 0:
            borrowed_copies = self.num_total - self.num_available
            if num_total < borrowed_copies:
                raise ValueError("\nCannot set total copies less than the number of borrowed copies.")
            self.num_total = num_total
            self.num_available = self.num_total - borrowed_copies
        else:
            raise ValueError("\nNumber of total copies must be a non-negative integer.")

    def set_publication_date(self, publication_date):
        """Set the publication date of the book."""
        if isinstance(publication_date, str):
            self.publication_date = publication_date.strip()
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
        return self.num_total

    def get_num_available(self):
        """Return the number of available copies of the book."""
        return self.num_available

    def get_publication_date(self):
        """Return the publication date of the book."""
        return self.publication_date

    def __str__(self):
        """Return a string representation of the book record."""
        return (f"Book ID: {self.id}\nTitle: {self.title}\nAuthor: {self.author}\n"
                f"Year: {self.year}\nPublisher: {self.publisher}\n"
                f"Total Copies: {self.num_total}\nAvailable Copies: {self.num_available}\n"
                f"Publication Date: {self.publication_date}\n")

class BookList():
    def __init__(self):
        self.books = {} # Store books with book_id as key

    def add_book(self, book):
        """Store a new book instance in the collection."""
        self.books[book.id] = book

    def remove_book(self, title): 
        """Remove a book from the collection by title."""
        title_lower = title.lower().strip()
        books_to_remove = [book for book in self.books.values() if title_lower in (book.title.lower())]
        if not books_to_remove:
            print(f'\nNo books found with the title: {title}\n')
            return
        
        book_to_remove = filter_selection(books_to_remove, title)

        print(f"Removed book '{book_to_remove.title}' with ID: '{book_to_remove.id}'\n")
        del self.books[book_to_remove.id]

    def find_book(self, search): 
        """Find books by search term."""
        search_lower = search.lower()
        book_to_find = [book for book in self.books.values() if search_lower in (book.title.lower(), book.author.lower(), book.publisher.lower(), book.publication_date.lower())]
        if not book_to_find:
            return [f'No books found with the search term: {search}']
        else:
            return book_to_find

    def get_total_books(self):
        """Return the total number of books stored in the collection."""
        return len(self.books)
    
    def __iter__(self):
        """Allow iteration over the books in the BookList."""
        return iter(self.books.items())
    
    
class User():
    def __init__(self, username, firstname, lastname, house_num, street_name, postcode, email, dob):
        self.username = username.strip()
        self.firstname = firstname.strip()
        self.lastname = lastname.strip()
        self.house_num = house_num
        self.street_name = street_name.strip()
        self.postcode = postcode.strip()
        self.email = email.strip()
        self.dob = dob.strip()

    def set_username(self, username):
        if not username:
            raise ValueError("\nUsername cannot be empty")
        self.username = username.strip()

    def set_firstname(self, firstname):
        if not firstname:
            raise ValueError("\nFirstname cannot be empty")
        self.firstname = firstname.strip()

    def set_lastname(self, lastname):
        if not lastname:
            raise ValueError("\nLastname cannot be empty")
        self.lastname = lastname.strip()

    def set_house_num(self, house_num):
        if house_num.isnumeric() and int(house_num) >= 0:
            self.house_num = house_num
        else:
            raise ValueError("\nHouse number must be a non negative integer")

    def set_street_name(self, street_name):
        if not street_name:
            raise ValueError("\nStreet name cannot be empty")
        self.street_name = street_name.strip()

    def set_postcode(self, postcode):
        if not postcode:
            raise ValueError("\nPostcode cannot be empty")
        self.postcode = postcode.strip()

    def set_email(self, email):
        if not email:
            raise ValueError("\nEmail cannot be empty")
        self.email = email.strip()

    def set_dob(self, dob):
        if not dob:
            raise ValueError("\nDate of birth cannot be empty")
        self.dob = dob.strip()

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
        firstname_lower = firstname.lower().strip()
        users_to_remove = [user for user in self.users.values() if firstname_lower in (user.firstname.lower())]
        if not users_to_remove:
            print(f'\nNo users found with the firstname: {firstname}\n')
            return
        
        user_to_remove = filter_selection(users_to_remove, firstname)

        print(f"Removed user '{user_to_remove.firstname} {user_to_remove.lastname}' with username: '{user_to_remove.username}'\n")
        del self.users[user_to_remove.username]

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
        """Allow a user to borrow a book if available."""
        try:
            if book.get_num_available() > 0:
                if username not in self.loans:
                    self.loans[username] = []
                # Set the due date to 14 days from today
                due_date = datetime.datetime.now() + datetime.timedelta(days=14)
                loan_record = {'book': book, 'due_date': due_date}
                self.loans[username].append(loan_record)
                book.set_num_available(book.get_num_available() - 1)
                print(f"\nBook '{book.title}' has been borrowed by user '{username}'. Due date is {due_date.strftime('%Y-%m-%d')}.")
            else:
                print(f"\nNo available copies of '{book.title}' to borrow.")
        except Exception as e:
            print(f"\nAn error occurred while borrowing the book: {e}")
    
    def return_book(self, username, book_id):
        """Allow a user to return a book."""
        try:
            if username in self.loans:
                for loan in self.loans[username]:
                    if loan['book'].id == book_id:
                        self.loans[username].remove(loan)
                        loan['book'].set_num_available(loan['book'].get_num_available() + 1)
                        return f"Book '{loan['book'].get_title()}' returned."
            print("\nBook not found in user's borrowed books.")
        except Exception as e:
            print(f"\nAn error occurred while returning the book: {e}")
    
    def count_borrowed_books(self, username):
        """Count and return the total number of books a user is currently borrowing."""
        return len(self.loans.get(username, []))
    
    def print_overdue_books(self, user_list):
        """Print out all overdue books along with the users’ details."""
        try:
            print("\nOverdue Books:")
            overdue_found = False
            current_date = datetime.datetime.now()
            for username, loan_records in self.loans.items():
                user = user_list.get_user(username)
                if not user:
                    continue  # Skip if user not found
                for loan_record in loan_records:
                    if loan_record['due_date'] < current_date:
                        overdue_found = True
                        book = loan_record['book']
                        due_date_str = loan_record['due_date'].strftime('%Y-%m-%d')
                        print(f"Username: {user.get_username()}, First Name: {user.get_firstname()}, Book: '{book.title}', Due Date: {due_date_str}")
            if not overdue_found:
                print("No overdue books.")
        except Exception as e:
            print(f"\nAn error occurred while printing overdue books: {e}")
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
    while True:
        #no exception handling needed here - EXPLAIN WHY
        print("\nBook List:")
        for book_id, book in list(book_list): print(book)
        book_name = input("\nEnter the name of the book you want to modify:\n").strip()
        book = book_list.find_book(book_name)
        if isinstance(book[0], str): 
            print("no book found")
            break
        else:
            book = filter_selection(book, book_name)
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
                        new_title = input("\nEnter new title:\n") #whitespace shouldn't need stripping here as the class constructor already does this, same for inputs below
                        book.set_title(new_title)
                        break
                    elif choice == '2':
                        new_author = input("\nEnter new author:\n")
                        book.set_author(new_author)
                        break
                    elif choice == '3':
                        new_year = input("\nEnter new year:\n")
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
                        return
                    else:
                        print("Invalid choice. Please select again.\n")
                except ValueError as e:
                    print(e)

            print("\nBook details updated successfully.\n")
            print(f'New details:\n{book}')

def modify_user(user_list):
    """Modify a user's details."""
    while True:
        #no exception handling needed here - EXPLAIN WHY
        print("\nUser List:")
        for user_id, user in list(user_list): print(user)
        username = input("\nEnter the username of the user you want to modify:\n").strip()
        user = user_list.users.get(username) #there is a method specifically for this - MAKE SURE THIS USES IT

        if not user:
            print(f"\nNo user found with username: {username}\n")
            break
        
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
                choice = input("\nEnter your choice (1-6): \n").strip()

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

def filter_selection(items, search_term): #method to handle logic for search queries with multiple items
        if len(items) == 1:
            return items[0]
        else:
            print(f"\nMultiple items found with the value '{search_term}'\n")

            for i, item in enumerate(items, 1):
                print(f"{i}. \n{item}")

            try:
                choice = int(input("Please specify which item you would like to select(enter the number): "))
                if 1 <= choice <= len(items):
                    selected_item = items[choice - 1]
                    return selected_item
                else:
                    return "Invalid selection. No item selected." #this may need a while loop to properly take input
            except ValueError:
                return "Invalid input. Please enter a valid number."

def init_library():

    #this could be done with a json file

    book_list = BookList()
    user_list = UserList()
    book_loans = Loans()

    book_list.add_book(Book("The Hobbit", "John Doe", 1960, "Books Inc", 12, "1960-02-24"))
    book_list.add_book(Book("The Hobbit", "Bob Marley", 1960, "Cooks Inc", 12, "1990-06-24"))
    book_list.add_book(Book("James Bond", "John Doe", 1930, "Blob Corp", 5, "1930-01-12"))
    book_list.add_book(Book("1984", "Max Smith", 1930, "Big Publishing", 5, "2008-09-07"))

    user_list.add_user(User("raringgarlic118", "Tim", "Lee", 12, "Park avenue", "BO21HK", "timlee@email.com","2000-01-01"))
    user_list.add_user(User("blobfish772", "Tim", "Lee", 1, "river avenue", "OJ6XKG", "timlee2@email.com","2002-11-31"))
    user_list.add_user(User("firequake122", "Bob", "Smith", 1, "birch street", "YTH87P", "bobsmith122@email.com","1992-06-19"))

    # print(f'{book_list.get_total_books()} total books')
    # print(f'{user_list.get_total_users()} total users')

    return book_list, user_list, book_loans


def books_menu(book_list):
    """Sub-menu for Books-related operations."""
    while True:
        print("\nBooks Menu:")
        print("1. Modify a Book")
        print("2. Add a New Book")
        print("3. Remove a Book")
        print("4. Display All Books")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice (1-5):\n").strip()
        if choice == '1':
            modify_book(book_list)
        elif choice == '2':
            add_new_book(book_list)
        elif choice == '3':
            remove_book_interface(book_list)
        elif choice == '4':
            display_all_books(book_list)
        elif choice == '5':
            print("\nReturning to the Main Menu.")
            break
        else:
            print("\nInvalid input, please select a valid option.")

def users_menu(user_list):
    """Sub-menu for Users-related operations."""
    while True:
        print("\nUsers Menu:")
        print("1. Add a New User")
        print("2. Remove a User")
        print("3. Modify a User")
        print("4. Display User Count")
        print("5. Get User Details")
        print("6. Back to Main Menu")

        choice = input("\nEnter your choice (1-5):\n").strip()
        if choice == '1':
            user_list.add_user(user_list)
        elif choice == '2':
            user_list.remove_user(user_list)
        elif choice == '3':
            modify_user(user_list) #this should probably be part of the user/userlist class
        elif choice == '4':
            user_list.get_total_users(user_list)
        elif choice == '5':
            user_list.get_user(user_list)
        elif choice == '6':
            print("\nReturning to the Main Menu.")
            break
        else:
            print("\nInvalid input, please select a valid option.")

def loans_menu(book_list, user_list, book_loans):
    """Sub-menu for Loans-related operations."""
    while True:
        print("\nLoans Menu:")
        print("1. Borrow a Book")
        print("2. Return a Book")
        print("3. Display User's Borrowed Books")
        print("4. Show Overdue Books")
        print("5. Back to Main Menu")

        choice = input("\nEnter your choice (1-5):\n").strip()
        if choice == '1':
            book_loans.borrow_book(book_list, user_list, book_loans)
        elif choice == '2':
            book_loans.return_book(book_list, user_list, book_loans)
        elif choice == '3':
            book_loans.count_borrowed_books(book_loans, user_list)
        elif choice == '4':
            book_loans.print_overdue_books(user_list) 
        elif choice == '5':
            print("\nReturning to the Main Menu.")
            break
        else:
            print("\nInvalid input, please select a valid option.")

def main():
    book_list, user_list, book_loans, = init_library()
    print("\nWelcome to the Library System!")

    while True:
        print(f'\nMain Menu:\n'
              f'1. Books\n'
              f'2. Users\n'
              f'3. Loans\n'
              f'4. Exit\n')
        try:
            choice = int(input("Please specify which option you would like (enter the number): \n"))
            if choice == 1:
                books_menu(book_list)
            elif choice == 2:
                users_menu(user_list)
            elif choice == '3':
                loans_menu(book_list, user_list, book_loans)
            elif choice == 4:
                print("\nExiting the Library System.")
                break
            else:
                print("\nInvalid input, please pick one of the following options.")
        except ValueError:
                print("\nInvalid input. Please enter a valid number.")

if __name__ == '__main__':
    main()