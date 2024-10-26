import random
from datetime import datetime, timedelta
import uuid
import re

class Book:
    """
    Represents a book in the library system.
    Each book has a unique ID, title, author, publication year, publisher,
    total number of copies, number of available copies, and publication date.
    """
    def __init__(self, title, author, year, publisher, num_total, publication_date):
        """
        Initialize a new book instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The year the book was published.
            publisher (str): The publisher of the book.
            num_total (int): The total number of copies of the book.
            publication_date (str): The publication date in 'YYYY-MM-DD' format.
        """
        self.id = uuid.uuid4()
        self.title = title
        self.author = author
        self.year = year
        self.publisher = publisher
        self.num_total = num_total
        self.num_available = num_total
        self.publication_date = publication_date #this might need to be an actual datetime

    def set_title(self, title):
        """Set the title of the book."""
        self.title = title

    def set_author(self, author):
        """Set the author of the book."""
        self.author = author

    def set_year(self, year):
        """Set the year of publication."""
        self.year = year

    def set_publisher(self, publisher):
        """Set the publisher of the book."""
        self.publisher = publisher.strip()

    def set_num_available(self, num_available):
        """
        Set the number of available copies.
        
        Args:
            num_available (int): The number of available copies.
        """
        if num_available <= self.num_total:
            self.num_available = num_available
    
    def set_num_total(self, num_total):
        """
        Set the total number of copies.
        
        Args:
            num_total (int): The new total number of copies.
        
        Raises:
            ValueError: If the new total is less than the number of borrowed copies.
        """
        borrowed_copies = self.num_total - self.num_available
        if num_total < borrowed_copies:
            raise ValueError("Cannot set total copies less than the number of borrowed copies.")
        self.num_total = num_total
        self.num_available = self.num_total - borrowed_copies

    def set_publication_date(self, publication_date):
        """Set the publication date of the book."""
        self.publication_date = publication_date
        
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

class BookList:
    """
    A collection to manage a list of books in the library system.
    """
    def __init__(self):
        """Initialize an empty dictionary to store books."""
        self.books = {} # Store books with book_id as key

    def add_book(self, book):
        """Store a new book instance in the collection."""
        self.books[book.id] = book

    def remove_book(self, book_to_remove): 
        """
        Remove a book from the collection by its ID.
        
        Args:
            book_to_remove (Book): The book instance to remove.
        """
        print(f"\nRemoved book '{book_to_remove.title}' with ID: '{book_to_remove.id}'\n")
        del self.books[book_to_remove.id]

    def find_book(self, search): 
        """
        Find books by a search term.
        
        Args:
            search (str): The term to search for in the book's title, author, publisher, or publication date.
        
        Returns:
            list: A list of matching books or a message if no books are found.
        """
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
     
class User:
    """
    Represents a user in the library system.
    """
    def __init__(self, username, firstname, lastname, house_num, street_name, postcode, email, dob):
        """
        Initialize a new user instance.
        
        Args:
            username (str): The user's username.
            firstname (str): The user's first name.
            lastname (str): The user's last name.
            house_num (int): The user's house number.
            street_name (str): The street name of the user's address.
            postcode (str): The postcode of the user's address.
            email (str): The user's email address.
            dob (str): The user's date of birth.
        """
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.house_num = house_num
        self.street_name = street_name
        self.postcode = postcode
        self.email = email
        self.dob = dob

    def set_username(self, username):
        """Set the username of the user."""
        self.username = username

    def set_firstname(self, firstname):
        """Set the first name of the user."""
        self.firstname = firstname

    def set_lastname(self, lastname):
        """Set the last name of the user."""
        self.lastname = lastname

    def set_house_num(self, house_num):
        """Set the house number of the user's address."""
        self.house_num = house_num

    def set_street_name(self, street_name):
        """Set the street name of the user's address."""
        self.street_name = street_name

    def set_postcode(self, postcode):
        """Set the postcode of the user's address."""
        self.postcode = postcode

    def set_email(self, email):
        """Set the email address of the user."""
        self.email = email

    def set_dob(self, dob):
        """Set the date of birth of the user."""
        self.dob = dob

    def get_username(self):
        """Return the username of the user."""
        return self.username
    
    def get_firstname(self):
        """Return the first name of the user."""
        return self.firstname
    
    def get_lastname(self):
        """Return the last name of the user."""
        return self.lastname
    
    def get_house_num(self):
        """Return the house number of the user's address."""
        return self.house_num
    
    def get_street_name(self):
        """Return the street name of the user's address."""
        return self.street_name
    
    def get_postcode(self):
        """Return the postcode of the user's address."""
        return self.postcode
    
    def get_email(self):
        """Return the email address of the user."""
        return self.email
    
    def get_dob(self):
        """Return the date of birth of the user."""
        return self.dob

    def __str__(self):
        """Return a string representation of the user record."""
        return (f"Username: {self.username}\nFirstname: {self.firstname}\nLastname: {self.lastname}\n"
                f"House Number: {self.house_num}\nStreet Name: {self.street_name}\n"
                f"Postcode: {self.postcode}\nEmail: {self.email}\n"
                f"Date of Birth: {self.dob}\n")
    
class UserList:
    """
    A collection to manage a list of users in the library system.
    """
    def __init__(self):
        """Initialize an empty dictionary to store users."""
        self.users = {}

    def add_user(self, user):
        """Store a new user instance in the collection."""
        self.users[user.username] = user

    def remove_user(self, firstname):
        """
        Remove a user from the collection by first name.
        
        Args:
            firstname (str): The first name of the user to remove.
        """
        firstname_lower = firstname.lower().strip()
        users_to_remove = [user for user in self.users.values() if firstname_lower in (user.firstname.lower())]
        if not users_to_remove:
            print(f'\nNo users found with the firstname: {firstname}\n')
            return
        
        user_to_remove = filter_selection(users_to_remove, firstname)

        print(f"\nRemoved user '{user_to_remove.firstname} {user_to_remove.lastname}' with username: '{user_to_remove.username}'\n")
        del self.users[user_to_remove.username]

    def get_total_users(self):
        """Return the total number of users in the system."""
        return len(self.users)
    
    def get_user(self, username):
        """
        Retrieve user details by username.
        
        Args:
            username (str): The username of the user.
        
        Returns:
            User: The User instance if found, else None.
        """
        return self.users.get(username, None)
    
    def __iter__(self):
        """Allow iteration over the users in the UserList."""
        return iter(self.users.items())

class Loans:
    """
    Manages the borrowing and returning of books in the library system.
    """
    def __init__(self):
        """Initialize an empty dictionary to store loans with the username as the key."""
        self.loans = {} # Dictionary with user as key and a list of borrowed books as value

    def borrow_book(self, username, book, due_days=14):
        """
        Allow a user to borrow a book if available.
        
        Args:
            username (User): The user who wants to borrow the book.
            book (Book): The book to be borrowed.
            due_days (int, optional): Number of days until the book is due. Default is 14.
        """
        try:
            if book.get_num_available() > 0:
                if username not in self.loans:
                    self.loans[username] = []
                # Set the due date to the specified number of days from today
                due_date = datetime.now() + timedelta(days=due_days)
                loan_record = {'book': book, 'due_date': due_date}
                self.loans[username].append(loan_record)
                book.set_num_available(book.get_num_available() - 1)
                print(f"\nBook '{book.title}' has been successfully borrowed by user '{username.get_username()}'. Due date is {due_date.strftime('%Y-%m-%d')}.")
            else:
                print(f"\nNo available copies of '{book.title}' to borrow.")
        except Exception as e:
            print(f"\nAn error occurred while borrowing the book: {e}")
    
    def return_book(self, username, book_id):
        """
        Allow a user to return a book.
        
        Args:
            username (User): The user who wants to return the book.
            book_id (UUID): The ID of the book being returned.
        """
        try:
            if username in self.loans:
                for loan in self.loans[username]:
                    if loan['book'].id == book_id:
                        self.loans[username].remove(loan)
                        loan['book'].set_num_available(loan['book'].get_num_available() + 1)
                        print(f"Book '{loan['book'].get_title()}' successfully returned by user '{username.get_username()}'.")
                        return
                print("\nBook not found in user's borrowed books.")
        except Exception as e:
            print(f"\nAn error occurred while returning the book: {e}")
    
    def count_borrowed_books(self, username):
        """
        Count the total number of books a user is currently borrowing.
        
        Args:
            username (User): The user whose borrowed books are being counted.
        
        Returns:
            int: The number of books borrowed by the user.
        """
        return len(self.loans.get(username, []))

    def print_borrowed_books(self, username):
        """
        Display all the books borrowed by a user.
        
        Args:
            username (User): The user whose borrowed books are being displayed.
        """
        borrowed_loans = self.loans.get(username, [])
        if not borrowed_loans:
            print("\nYou have no borrowed books.")
            return
        
        print("\nYour Borrowed Books:")
        for i, loan_record in enumerate(borrowed_loans, 1):
            book = loan_record['book']
            due_date_str = loan_record['due_date'].strftime('%Y-%m-%d')
            print(f"{i}. {book.title} (Due Date: {due_date_str})")
    
    def print_overdue_books(self):
        """Print all overdue books along with the users' details."""
        try:
            overdue_found = False
            current_date = datetime.now()
            for username, loan_records in self.loans.items():
                if not username:
                    continue  # Skip if user not found
                for loan_record in loan_records:
                    if loan_record['due_date'] < current_date:
                        overdue_found = True
                        book = loan_record['book']
                        due_date_str = loan_record['due_date'].strftime('%Y-%m-%d')
                        print(f"Username: {username.get_username()}, First Name: {username.get_firstname()}, Book: '{book.title}', Due Date: {due_date_str}")
            if not overdue_found:
                print("No overdue books.\n")
        except Exception as e:
            print(f"\nAn error occurred while printing overdue books: {e}")


class MainMenu:
    """
    The main menu for interacting with the library system.
    Provides options for managing books, users, and loans.
    """
    def __init__(self, book_list, user_list, book_loans):
        """
        Initialize the main menu with references to the main data structures.
        
        Args:
            book_list (BookList): The collection of books.
            user_list (UserList): The collection of users.
            book_loans (Loans): The loans management system.
        """
        self.book_list = book_list
        self.user_list = user_list
        self.book_loans = book_loans

    def display(self):
        """Display the main menu and handle user input for navigation."""
        print("\nWelcome to the Library System!")
        while True:
            print_header("Main Menu:")
            print("1. Manage Books")
            print("2. Manage Users")
            print("3. Manage Loans")
            print("4. Exit")

            choice = input("Please select an option (1-4): \n").strip()
            if choice == '1':
                books_menu = BooksMenu(self.book_list)
                books_menu.display()
            elif choice == '2':
                users_menu = UsersMenu(self.user_list)
                users_menu.display()
            elif choice == '3':
                loans_menu = LoansMenu(self.book_list, self.user_list, self.book_loans)
                loans_menu.display()
            elif choice == '4':
                self.exit_program()
                break
            else:
                print("\nInvalid input, please select a valid option.")

    def exit_program(self):
        """Exit the library system."""
        print("\nExiting the Library System. Goodbye!")



class BooksMenu:
    """
    A sub-menu for managing book-related operations in the library system.
    """
    def __init__(self, book_list):
        """
        Initialize the BooksMenu with a reference to the collection of books.
        
        Args:
            book_list (BookList): The collection of books.
        """
        self.book_list = book_list

    def display(self):
        """Display the Books Menu and handle user input for book operations."""
        while True:
            print_header("Books Menu:")
            print("1. Add a New Book")
            print("2. Remove a Book")
            print("3. Find a Book")
            print("4. Modify a Book")
            print("5. Display Book Count")
            print("6. Back to Main Menu")

            choice = input("\nEnter your choice (1-6):\n").strip()
            if choice == '1':
                self.add_book_interface()
            elif choice == '2':
                self.remove_book_interface()
            elif choice == '3':
                self.find_book_interface()
            elif choice == '4':
                self.modify_book_interface()
            elif choice == '5':
                self.count_book_interface()
            elif choice == '6':
                print("\nReturning to the Main Menu.")
                break
            else:
                print("\nInvalid input, please select a valid option.")
    
    def add_book_interface(self):
        """Interface to add a new book to the system."""
        print("\nAdd a New Book")

        title = get_input("Enter the title of the book:\n", non_empty, "Title cannot be empty.")
        author = get_input("Enter the author of the book:\n", non_empty, "Author cannot be empty.")
        year = int(get_input("Enter the year of publication:\n", positive_int, "Year must be a positive integer."))
        publisher = get_input("Enter the publisher of the book:\n", non_empty, "Publisher cannot be empty.")
        num_copies = int(get_input("Enter the number of copies:\n", non_negative_int, "Number of copies must be a non-negative integer."))
        publication_date = get_input("Enter the publication date (YYYY-MM-DD):\n", valid_date, "Invalid date format. Please enter date as YYYY-MM-DD.")

        # Create and add the new book
        new_book = Book(title, author, year, publisher, num_copies, publication_date)
        self.book_list.add_book(new_book)
        print("\nNew book added successfully.")

    def remove_book_interface(self):
        """Interface to remove a book from the system."""
        print("\nRemove a Book")
        book = search_books(self.book_list, "Enter the name of the book you would like to remove:", "No book found with title")
        if isinstance(book, Book):
            self.book_list.remove_book(book)

    def find_book_interface(self):
        """Interface to search for a book in the system."""
        print("\nSearch Books:")
        book = search_books(self.book_list, "Enter the title, author, publisher, or publication date of the book you want to search:", "No book found with data", False)
        if isinstance(book, Book):
            print(f'\nBook found!\n{book}')

    def modify_book_interface(self):
        """Interface to modify a book's details."""
        print("\nBook List:")
        book = search_books(self.book_list, "Enter the name of the book you would like to modify:", "No book found with title")
        if isinstance(book, Book):
            print(f'\nCurrent details:\n{book}')
            while True:
                print("\nWhat would you like to modify?")
                print("1. Title")
                print("2. Author")
                print("3. Year")
                print("4. Publisher")
                print("5. Total Number of Copies")
                print("6. Exit")

                try:
                    choice = input("\nEnter your choice (1-6):\n").strip()

                    if choice == '1':
                        new_title = get_input("\nEnter new title:\n", non_empty, "Title cannot be empty.")
                        book.set_title(new_title)
                        break
                    elif choice == '2':
                        new_author = get_input("\nEnter new author:\n", non_empty, "Author cannot be empty.")
                        book.set_author(new_author)
                        break
                    elif choice == '3':
                        new_year = int(get_input("\nEnter new year:\n", positive_int, "Year must be a positive integer."))
                        book.set_year(new_year)
                        break
                    elif choice == '4':
                        new_publisher = get_input("\nEnter new publisher:\n", non_empty, "Publisher cannot be empty.")
                        book.set_publisher(new_publisher)
                        break
                    elif choice == '5':
                        new_copies = int(get_input("\nEnter new number of copies:\n", non_negative_int, "Number of copies must be a non-negative integer."))
                        book.set_num_total(new_copies)
                        break
                    elif choice == '6':
                        return
                    else:
                        print("Invalid choice. Please select again.\n")
                except ValueError as e:
                    print(e)
            print("\nBook details updated successfully.\n")
            print(f'New details:\n{book}')
            
    def count_book_interface(self):
        """Display the total number of books in the library."""
        print("\nBook Count:")
        print(f'There are {self.book_list.get_total_books()} total books in the library system.')
    
class UsersMenu:
    """
    A sub-menu for managing user-related operations in the library system.
    """
    def __init__(self, user_list):
        """
        Initialize the UsersMenu with a reference to the collection of users.
        
        Args:
            user_list (UserList): The collection of users.
        """
        self.user_list = user_list

    def display(self):
        """Display the Users Menu and handle input for user operations."""
        while True:
            print_header("Users Menu:")
            print("1. Add a New User")
            print("2. Remove a User")
            print("3. Modify a User")
            print("4. Get User Details")
            print("5. Display User Count")
            print("6. Back to Main Menu")

            choice = input("\nEnter your choice (1-6):\n").strip()
            if choice == '1':
                self.add_user_interface()
            elif choice == '2':
                self.remove_user_interface()
            elif choice == '3':
                self.modify_user_interface()
            elif choice == '4':
                self.show_user_details_interface()
            elif choice == '5':
                self.count_user_interface()
            elif choice == '6':
                print("\nReturning to the Main Menu.")
                break
            else:
                print("\nInvalid input, please select a valid option.")
    
    def add_user_interface(self):
        """Interface to add a new user to the system."""
        print("\nAdd a New User")

        def unique_username(x):
            """Check if the username is non-empty and unique."""
            return non_empty(x) and not self.user_list.get_user(x)

        username = get_input("Enter the username:\n", unique_username, "Username cannot be empty or already exists.")
        firstname = get_input("Enter the first name:\n", non_empty, "First name cannot be empty.")
        lastname = get_input("Enter the last name:\n", non_empty, "Last name cannot be empty.")
        house_num = int(get_input("Enter the house number:\n", non_negative_int, "House number must be a non-negative integer."))
        street_name = get_input("Enter the street name:\n", non_empty, "Street name cannot be empty.")
        postcode = get_input("Enter the postcode:\n", non_empty, "Postcode cannot be empty.")
        email = get_input("Enter the email address:\n", valid_email, "Email cannot be empty and must be formatted correctly.")
        dob = get_input("Enter the date of birth (YYYY-MM-DD):\n", valid_date, "Invalid date format. Please enter date as YYYY-MM-DD.")

        # Create and add the new user
        new_user = User(username, firstname, lastname, house_num, street_name, postcode, email, dob)
        self.user_list.add_user(new_user)
        print("\nNew user added successfully.")

    def remove_user_interface(self):
        """Interface to remove a user from the system."""
        print("\nRemove a User")
        username = input("\nEnter the first name of the user you want to remove:\n").strip()
        self.user_list.remove_user(username)

    def modify_user_interface(self):
        """Interface to modify a user's details."""
        print("\nUser List:")
        user = search_users(self.user_list, "Enter the username of the user you would like to modify:", "No user found with username")
        if isinstance(user, User):
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
                        new_firstname = get_input("\nEnter new first name:\n", non_empty, "First name cannot be empty.")
                        user.set_firstname(new_firstname)
                        break
                    elif choice == '2':
                        new_surname = get_input("\nEnter new last name:\n", non_empty, "Last name cannot be empty.")
                        user.set_lastname(new_surname)
                        break
                    elif choice == '3':
                        new_house_number = int(get_input("\nEnter new house number:\n", non_negative_int, "House number must be a non-negative integer."))
                        user.set_house_num(new_house_number)
                        break
                    elif choice == '4':
                        new_street_name = get_input("\nEnter new street name:\n", non_empty, "Street name cannot be empty.")
                        user.set_street_name(new_street_name)
                        break
                    elif choice == '5':
                        new_postcode = get_input("\nEnter new postcode:\n", non_empty, "Postcode cannot be empty.")
                        user.set_postcode(new_postcode)
                        break
                    elif choice == '6':
                        return
                    else:
                        print("Invalid choice. Please select again.\n")
                except ValueError as e:
                    print(e)
            print("\nUser details updated successfully.\n")
            print(f'New details:\n{user}')

    def show_user_details_interface(self):
        """Interface to display details of a specific user."""
        print("\nSearch User Details:")
        user = search_users(self.user_list, "Enter the username of the user you would like to display:", "No user found with username", False)
        if isinstance(user, User):
            print(f'\nUser found!\n{user}')
        
    def count_user_interface(self):
        """Display the total number of users in the system."""
        print("\nUser Count:")
        print(f'There are {self.user_list.get_total_users()} total users in the library system.')


class LoansMenu:
    """
    A sub-menu for managing loan-related operations in the library system.
    """
    def __init__(self, book_list, user_list, book_loans):
        """
        Initialize the LoansMenu with references to the main data structures.
        
        Args:
            book_list (BookList): The collection of books.
            user_list (UserList): The collection of users.
            book_loans (Loans): The loans management system.
        """
        self.book_list = book_list
        self.user_list = user_list
        self.book_loans = book_loans

    def display(self):
        """Display the Loans Menu and handle user input for loan operations."""
        while True:
            print_header("Loans Menu:")
            print("1. Borrow a Book")
            print("2. Return a Book")
            print("3. Display User's Borrowed Books")
            print("4. Show Overdue Books")
            print("5. Back to Main Menu")

            choice = input("\nEnter your choice (1-5):\n").strip()
            if choice == '1':
                self.borrow_book_interface()
            elif choice == '2':
                self.return_book_interface()
            elif choice == '3':
                self.show_count_loans_interface()
            elif choice == '4':
                self.show_overdue_loans_interface()
            elif choice == '5':
                print("\nReturning to the Main Menu.")
                break
            else:
                print("\nInvalid input, please select a valid option.")

    def borrow_book_interface(self):
        """Interface for borrowing a book."""
        print("\nBorrow a Book")
        
        username = search_users(self.user_list, "Enter the username of the user that would like to borrow a book:", "No user found with username", False)
        if isinstance(username, User): 
            book = search_books(self.book_list, "Enter the name of the book you would like to borrow", "No book found with title")
            if isinstance(book, Book):
                self.book_loans.borrow_book(username, book)

    def return_book_interface(self):
        """Interface for returning a book."""
        print("\nReturn a Book")

        username = search_users(self.user_list, "Enter the username of the user that would like to return a book:", "No user found with username", False)
        if isinstance(username, User):
            self.book_loans.print_borrowed_books(username)
            borrowed_loans = self.book_loans.loans.get(username, [])

            if borrowed_loans:
                while True:
                    choice_input = input("\nEnter the number of the book you want to return (or type 'back' to cancel):\n").strip()
                    if choice_input.lower() == 'back':
                        print("\nReturning to the Loans Menu.")
                        return
                    try:
                        choice = int(choice_input)
                        if 1 <= choice <= len(borrowed_loans):
                            loan_record = borrowed_loans[choice - 1]
                            self.book_loans.return_book(username, loan_record['book'].id)
                            break
                        else:
                            print("Invalid selection. Please enter a valid number.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")

    def show_count_loans_interface(self):
        """Display all books borrowed by a specific user."""
        print("\nDisplay User's Borrowed Books")

        username = search_users(self.user_list, "Enter the username of the user to display borrowed books:", "No user found with username", False)
        self.book_loans.print_borrowed_books(username)

        # Display the total number of borrowed books
        total_borrowed = self.book_loans.count_borrowed_books(username)
        print(f"\n{username.username} is currently borrowing {total_borrowed} book(s).")

    def show_overdue_loans_interface(self):
        """Display all overdue books."""
        print("\nOverdue Books:\n")
        self.book_loans.print_overdue_books(self.user_list)

        
def init_library(): #this could be done with a json file
    """
    Initialize the library system with a set of sample books and users.
    
    Returns:
        tuple: Contains the initialized BookList, UserList, and Loans instances.
    """
    book_list = BookList()
    user_list = UserList()
    book_loans = Loans()

    # Adding sample books to the collection
    book_list.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Charles Scribner's Sons", 8, "1925-04-10"))
    book_list.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960, "J.B. Lippincott & Co.", 15, "1960-07-11"))
    book_list.add_book(Book("Pride and Prejudice", "Jane Austen", 1813, "T. Egerton, Whitehall", 10, "1813-01-28"))
    book_list.add_book(Book("Moby Dick", "Herman Melville", 1851, "Harper & Brothers", 5, "1851-11-14"))
    book_list.add_book(Book("Crime and Punishment", "Leo Tolstoy", 1869, "The Russian Messenger", 9, "1869-01-01"))
    book_list.add_book(Book("Crime and Punishment", "Fyodor Dostoevsky", 1866, "The Russian Messenger", 12, "1866-01-01"))

    # Adding sample users to the collection
    user_list.add_user(User("oceanwave927", "Alice", "Johnson", 3, "Maple Street", "AB12CD", "alice.johnson@email.com", "1990-03-15"))
    user_list.add_user(User("skydreamer503", "Charlie", "Brown", 4, "Elm Avenue", "XY34ZF", "charlie.brown@email.com", "1985-09-22"))
    user_list.add_user(User("mountainpeak334", "Dave", "Wilson", 2, "Pine Road", "LK76HJ", "dave.wilson@email.com", "2001-12-08"))
    user_list.add_user(User("forestlight817", "Eve", "Green", 6, "Cedar Drive", "PO98YU", "eve.green@email.com", "1995-05-30"))
    user_list.add_user(User("sunsetblaze411", "Frank", "Miller", 1, "Oak Lane", "MN45QR", "frank.miller@email.com", "1988-11-11"))
    user_list.add_user(User("starlitpath729", "Frank", "Evans", 2, "Willow Court", "CD23EF", "grace.evans@email.com", "1993-07-24"))

    # Simulating some loan transactions with due dates
    book_loans.borrow_book(user_list.users.get("oceanwave927"), book_list.find_book("The Great Gatsby")[0], -5)
    book_loans.borrow_book(user_list.users.get("oceanwave927"), book_list.find_book("To Kill a Mockingbird")[0], 2)
    book_loans.borrow_book(user_list.users.get("mountainpeak334"), book_list.find_book("Moby Dick")[0], -9)
    book_loans.borrow_book(user_list.users.get("sunsetblaze411"), book_list.find_book("The Great Gatsby")[0], -3)
    book_loans.borrow_book(user_list.users.get("skydreamer503"), book_list.find_book("Pride and Prejudice")[0], 7)

    return book_list, user_list, book_loans


def main():
    """
    Main function to initialize the library and start the main menu.
    """
    book_list, user_list, book_loans = init_library()
    main_menu = MainMenu(book_list, user_list, book_loans)
    main_menu.display()

def print_header(title):
    """
    Print a formatted header for section titles.
    
    Args:
        title (str): The title to be displayed as a header.
    """
    print("\n" + "="*len(title))
    print(title)
    print("="*len(title) + "\n")

def filter_selection(items, search_term): #method to handle logic for search queries with multiple items
    """
    Handle the selection of a specific item from a list of items.
    
    Args:
        items (list): The list of items to choose from.
        search_term (str): The term used to search or filter items.
    
    Returns:
        The selected item if a valid choice is made, otherwise None.
    """
    if len(items) == 1:
        #if there is only one item, return it directly
        return items[0]
    else:
        print(f"\nMultiple items found with the value '{search_term}'\n")
        for i, item in enumerate(items, 1):
            print(f"{i}. \n{item}")

        try:
            #ask the user to select one of the items
            choice = int(input("Please specify which item you would like to select (enter the number): "))
            if 1 <= choice <= len(items):
                return items[choice - 1]
            else:
                print("Invalid selection. No item selected.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    return None

def search_users(user_list, prompt, error_message, show_users=True):
    """
    Search for a user in the user list based on input.
    
    Args:
        user_list (UserList): The collection of users to search.
        prompt (str): The prompt message to display for input.
        error_message (str): The message to display if the user is not found.
        show_users (bool, optional): Whether to display all users before searching. Default is True.
    
    Returns:
        User: The found User instance or None if not found.
    """
    while True:
        if show_users:
            #optionally display all users - make true by default
            for user_id, user in user_list:
                print(user)
        username = get_input(f'\n{prompt}\n', non_empty, "Search cannot be empty!")
        user = user_list.users.get(username)

        if not user:
            print(f"\n{error_message} '{username}'")
            break
        else:
            return user

def search_books(book_list, prompt, error_message, show_books=True):
    """
    Search for a book in the book list based on input.
    
    Args:
        book_list (BookList): The collection of books to search.
        prompt (str): The prompt message to display for input.
        error_message (str): The message to display if the book is not found.
        show_books (bool, optional): Whether to display all books before searching. Default is True.
    
    Returns:
        Book: The found Book instance or None if not found.
    """
    while True:
        if show_books:
            #optionally display all books - make true by default
            for book_id, book in book_list:
                print(book)
        book_name = get_input(f'\n{prompt}\n', non_empty, "Search cannot be empty!")
        books = book_list.find_book(book_name)

        if isinstance(books[0], str):
            # If no books found, show error message
            print(f"\n{error_message} '{book_name}'")
            break
        else:
            # Let the user select from the list of found books
            book = filter_selection(books, book_name)
            return book
            
def get_input(prompt, validation_func, error_message):
    """
    Get user input and validate it with a specified lambda function.
    
    Args:
        prompt (str): The prompt message for the input.
        validation_func (function): A function to validate the input.
        error_message (str): The error message to display for invalid input.
    
    Returns:
        str: The validated input value.
    """
    while True:
        value = input(prompt).strip()
        if validation_func(value):
            return value
        else:
            print(error_message)
    
# Validation functions
non_empty = lambda x: x != ''
positive_int = lambda x: x.isdigit() and int(x) > 0
non_negative_int = lambda x: x.isdigit() and int(x) >= 0
    
def valid_date(x):
    """Validate if a string is a valid date in 'YYYY-MM-DD' format."""
    return re.match(r"^(16|20)\d{2}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$", x) is not None

def valid_email(x):
    """Validate if a string is a properly formatted email."""
    return re.match(r"[^@]+@[^@]+\.[^@]+", x) is not None

if __name__ == '__main__':
    #entry point for the script
    main()
