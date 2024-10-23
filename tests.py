# tests.py

import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime, timedelta
from library_record import (
    Book, BookList, User, UserList, Loans, get_input, filter_selection, search_users, search_books,
    non_empty, positive_int, non_negative_int, valid_date, valid_email
)
from library_record import BooksMenu, UsersMenu, LoansMenu, init_library


class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("Test Title", "Test Author", 2020, "Test Publisher", 5, "2020-01-01")

    def test_book_initialization(self):
        self.assertEqual(self.book.title, "Test Title")
        self.assertEqual(self.book.author, "Test Author")
        self.assertEqual(self.book.year, 2020)
        self.assertEqual(self.book.publisher, "Test Publisher")
        self.assertEqual(self.book.num_total, 5)
        self.assertEqual(self.book.num_available, 5)
        self.assertEqual(self.book.publication_date, "2020-01-01")

    def test_set_title(self):
        self.book.set_title("New Title")
        self.assertEqual(self.book.title, "New Title")
        with self.assertRaises(ValueError):
            self.book.set_title("")

    def test_set_author(self):
        self.book.set_author("New Author")
        self.assertEqual(self.book.author, "New Author")
        with self.assertRaises(ValueError):
            self.book.set_author("")

    def test_set_year(self):
        self.book.set_year(2021)
        self.assertEqual(self.book.year, 2021)
        with self.assertRaises(ValueError):
            self.book.set_year(-1)

    def test_set_publisher(self):
        self.book.set_publisher("New Publisher")
        self.assertEqual(self.book.publisher, "New Publisher")
        with self.assertRaises(ValueError):
            self.book.set_publisher("")

    def test_set_num_total(self):
        self.book.set_num_total(10)
        self.assertEqual(self.book.num_total, 10)
        self.assertEqual(self.book.num_available, 10)
        with self.assertRaises(ValueError):
            self.book.set_num_total(-1)

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User("testuser", "John", "Doe", 123, "Test Street", "12345", "test@example.com", "1990-01-01")

    def test_user_initialization(self):
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.firstname, "John")
        self.assertEqual(self.user.lastname, "Doe")
        self.assertEqual(self.user.house_num, 123)
        self.assertEqual(self.user.street_name, "Test Street")
        self.assertEqual(self.user.postcode, "12345")
        self.assertEqual(self.user.email, "test@example.com")
        self.assertEqual(self.user.dob, "1990-01-01")

    def test_set_firstname(self):
        self.user.set_firstname("Jane")
        self.assertEqual(self.user.firstname, "Jane")
        with self.assertRaises(ValueError):
            self.user.set_firstname("")

    def test_set_email(self):
        self.user.set_email("new@example.com")
        self.assertEqual(self.user.email, "new@example.com")
        with self.assertRaises(ValueError):
            self.user.set_email("")

class TestBookList(unittest.TestCase):
    def setUp(self):
        self.book_list = BookList()
        self.book = Book("Test Title", "Test Author", 2020, "Test Publisher", 5, "2020-01-01")
        self.book_list.add_book(self.book)

    def test_add_book(self):
        self.assertIn(self.book.id, self.book_list.books)

    def test_remove_book(self):
        self.book_list.remove_book("Test Title")
        self.assertNotIn(self.book.id, self.book_list.books)

    def test_find_book(self):
        found_books = self.book_list.find_book("Test Title")
        self.assertIn(self.book, found_books)

class TestUserList(unittest.TestCase):
    def setUp(self):
        self.user_list = UserList()
        self.user = User("testuser", "John", "Doe", 123, "Test Street", "12345", "test@example.com", "1990-01-01")
        self.user_list.add_user(self.user)

    def test_add_user(self):
        self.assertIn("testuser", self.user_list.users)

    def test_remove_user(self):
        self.user_list.remove_user("John")
        self.assertNotIn("testuser", self.user_list.users)

    def test_get_user(self):
        user = self.user_list.get_user("testuser")
        self.assertEqual(user, self.user)

class TestLoans(unittest.TestCase):
    def setUp(self):
        self.loans = Loans()
        self.user = User("testuser", "John", "Doe", 123, "Test Street", "12345", "test@example.com", "1990-01-01")
        self.book = Book("Test Title", "Test Author", 2020, "Test Publisher", 5, "2020-01-01")
        self.user_list = UserList()
        self.user_list.add_user(self.user)
        self.book_list = BookList()
        self.book_list.add_book(self.book)

    def test_borrow_book(self):
        self.loans.borrow_book("testuser", self.book)
        self.assertEqual(self.book.num_available, 4)
        self.assertIn("testuser", self.loans.loans)

    def test_return_book(self):
        self.loans.borrow_book("testuser", self.book)
        self.loans.return_book("testuser", self.book.id)
        self.assertEqual(self.book.num_available, 5)
        self.assertEqual(len(self.loans.loans["testuser"]), 0)

    def test_print_borrowed_books(self):
        self.loans.borrow_book("testuser", self.book)
        with patch('builtins.print') as mocked_print:
            self.loans.print_borrowed_books("testuser")
            mocked_print.assert_called_with("\nYour Borrowed Books:\n1. Test Title (Due Date: " + (datetime.now() + timedelta(days=14)).strftime('%Y-%m-%d') + ")")

    def test_print_overdue_books(self):
        self.loans.borrow_book("testuser", self.book)
        # Simulate overdue by setting the due date in the past
        self.loans.loans["testuser"][0]['due_date'] = datetime.now() - timedelta(days=1)
        with patch('builtins.print') as mocked_print:
            self.loans.print_overdue_books(self.user_list)
            mocked_print.assert_any_call("Username: testuser, First Name: John, Book: 'Test Title', Due Date: " + (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d'))

    def test_count_borrowed_books(self):
        self.assertEqual(self.loans.count_borrowed_books("testuser"), 0)
        self.loans.borrow_book("testuser", self.book)
        self.assertEqual(self.loans.count_borrowed_books("testuser"), 1)


class TestUtilityFunctions(unittest.TestCase):
    def test_filter_selection_single_item(self):
        items = ["item1"]
        result = filter_selection(items, "item")
        self.assertEqual(result, "item1")

    def test_filter_selection_multiple_items(self):
        items = ["item1", "item2"]
        with patch('builtins.input', return_value='1'):
            result = filter_selection(items, "item")
            self.assertEqual(result, "item1")

    def test_search_users_found(self):
        user_list = UserList()
        user = User("testuser", "John", "Doe", 123, "Test Street", "12345", "john@example.com", "1980-05-20")
        user_list.add_user(user)
        with patch('builtins.input', return_value="testuser"):
            result = search_users(user_list, "Enter the username:", "No user found")
            self.assertEqual(result, user)

    def test_search_users_not_found(self):
        user_list = UserList()
        with patch('builtins.input', return_value="unknown"):
            result = search_users(user_list, "Enter the username:", "No user found")
            self.assertIsNone(result)

    def test_search_books_found(self):
        book_list = BookList()
        book = Book("Test Book", "Author", 2020, "Publisher", 5, "2020-01-01")
        book_list.add_book(book)
        with patch('builtins.input', return_value="Test Book"):
            result = search_books(book_list, "Enter the book name:", "No book found")
            self.assertEqual(result, book)

    def test_search_books_not_found(self):
        book_list = BookList()
        with patch('builtins.input', return_value="Unknown Book"):
            result = search_books(book_list, "Enter the book name:", "No book found")
            self.assertIsNone(result)


class TestBooksMenu(unittest.TestCase):
    def setUp(self):
        self.book_list = BookList()
        self.menu = BooksMenu(self.book_list)

    def test_add_book_interface(self):
        with patch('builtins.input', side_effect=["Title", "Author", "2021", "Publisher", "10", "2021-01-01"]):
            with patch('builtins.print'):
                self.menu.add_book_interface()
        self.assertEqual(self.book_list.get_total_books(), 1)

    def test_display(self):
        with patch('builtins.input', side_effect=['6']):
            with patch('builtins.print') as mocked_print:
                self.menu.display()
                mocked_print.assert_any_call("\nReturning to the Main Menu.")


class TestUsersMenu(unittest.TestCase):
    def setUp(self):
        self.user_list = UserList()
        self.menu = UsersMenu(self.user_list)

    def test_add_user_interface(self):
        with patch('builtins.input', side_effect=["username", "John", "Doe", "123", "Street", "12345", "email@example.com", "1990-01-01"]):
            with patch('builtins.print'):
                self.menu.add_user_interface(self.user_list)
        self.assertEqual(self.user_list.get_total_users(), 1)

    def test_display(self):
        with patch('builtins.input', side_effect=['6']):
            with patch('builtins.print') as mocked_print:
                self.menu.display()
                mocked_print.assert_any_call("\nReturning to the Main Menu.")


class TestLoansMenu(unittest.TestCase):
    def setUp(self):
        self.book_list = BookList()
        self.user_list = UserList()
        self.loans = Loans()
        self.menu = LoansMenu(self.book_list, self.user_list, self.loans)

    def test_borrow_book_interface(self):
        book = Book("Test Book", "Author", 2020, "Publisher", 5, "2020-01-01")
        self.book_list.add_book(book)
        user = User("testuser", "John", "Doe", 123, "Test Street", "12345", "john@example.com", "1980-05-20")
        self.user_list.add_user(user)

        with patch('builtins.input', side_effect=["testuser", "Test Book"]):
            self.menu.borrow_book_interface()
        self.assertEqual(book.num_available, 4)

    def test_display(self):
        with patch('builtins.input', side_effect=['5']):
            with patch('builtins.print') as mocked_print:
                self.menu.display()
                mocked_print.assert_any_call("\nReturning to the Main Menu.")

class TestBookAdditional(unittest.TestCase):
    def setUp(self):
        self.book = Book("Title", "Author", 2000, "Publisher", 3, "2000-01-01")

    def test_set_publication_date(self):
        self.book.set_publication_date("2021-05-12")
        self.assertEqual(self.book.publication_date, "2021-05-12")
        with self.assertRaises(ValueError):
            self.book.set_publication_date("invalid-date")

    def test_get_methods(self):
        self.assertEqual(self.book.get_title(), "Title")
        self.assertEqual(self.book.get_author(), "Author")
        self.assertEqual(self.book.get_year(), 2000)
        self.assertEqual(self.book.get_publisher(), "Publisher")
        self.assertEqual(self.book.get_num_copies(), 3)
        self.assertEqual(self.book.get_publication_date(), "2000-01-01")

class TestUserAdditional(unittest.TestCase):
    def setUp(self):
        self.user = User("username", "First", "Last", 123, "Street", "12345", "user@example.com", "1990-01-01")

    def test_set_username(self):
        self.user.set_username("newusername")
        self.assertEqual(self.user.username, "newusername")
        with self.assertRaises(ValueError):
            self.user.set_username("")

    def test_set_lastname(self):
        self.user.set_lastname("NewLast")
        self.assertEqual(self.user.lastname, "NewLast")
        with self.assertRaises(ValueError):
            self.user.set_lastname("")

    def test_set_house_num(self):
        self.user.set_house_num("456")
        self.assertEqual(self.user.house_num, "456")
        with self.assertRaises(ValueError):
            self.user.set_house_num("-1")

class TestBookListAdditional(unittest.TestCase):
    def setUp(self):
        self.book_list = BookList()
        self.book = Book("Book Title", "Author", 2000, "Publisher", 3, "2000-01-01")
        self.book_list.add_book(self.book)

    def test_remove_nonexistent_book(self):
        self.book_list.remove_book("Nonexistent Book")
        # Check that the existing book is still in the list
        self.assertIn(self.book.id, self.book_list.books)

class TestLoansAdditional(unittest.TestCase):
    def setUp(self):
        self.loans = Loans()
        self.book = Book("Test Book", "Author", 2000, "Publisher", 1, "2000-01-01")
        self.user = User("username", "First", "Last", 123, "Street", "12345", "user@example.com", "1990-01-01")

    def test_borrow_no_available_copies(self):
        self.loans.borrow_book("username", self.book)
        with self.assertRaises(Exception):
            self.loans.borrow_book("username", self.book)

    def test_return_book_not_borrowed(self):
        message = self.loans.return_book("username", "fake-id")
        self.assertIn("not found in user's borrowed books", message)

class TestFilterSelection(unittest.TestCase):
    def test_filter_selection_single(self):
        item = filter_selection(["item1"], "item1")
        self.assertEqual(item, "item1")

    def test_filter_selection_multiple(self):
        with patch('builtins.input', return_value="1"):
            item = filter_selection(["item1", "item2"], "item")
            self.assertEqual(item, "item1")

class TestMenu(unittest.TestCase):
    def setUp(self):
        self.book_list = BookList()
        self.user_list = UserList()
        self.loans = Loans()

    @patch('builtins.input', side_effect=["1", "5"])
    def test_books_menu(self, mock_input):
        books_menu = BooksMenu(self.book_list)
        books_menu.display()

    @patch('builtins.input', side_effect=["1", "username", "new@example.com", "5"])
    def test_users_menu(self, mock_input):
        users_menu = UsersMenu(self.user_list)
        users_menu.display()

class TestIntegration(unittest.TestCase):
    def setUp(self):
        self.book_list = BookList()
        self.user_list = UserList()
        self.book_loans = Loans()

        # Add sample data
        self.book = Book("Integration Test Book", "Author", 2020, "Publisher", 5, "2020-01-01")
        self.book_list.add_book(self.book)
        self.user = User("integrationuser", "First", "Last", 123, "Street", "12345", "user@example.com", "1990-01-01")
        self.user_list.add_user(self.user)

    @patch('builtins.input', side_effect=[
        '1',  # Borrow a Book
        'integrationuser',  # Username
        'Integration Test Book',  # Book Title
        '5'  # Exit
    ])
    def test_borrow_book_workflow(self, mock_input):
        loans_menu = LoansMenu(self.book_list, self.user_list, self.book_loans)
        loans_menu.display()

        # Check that the book has been borrowed
        self.assertEqual(self.book.num_available, 4)
        self.assertIn('integrationuser', self.book_loans.loans)
        self.assertEqual(len(self.book_loans.loans['integrationuser']), 1)

    @patch('builtins.input', side_effect=[
        '2',  # Return a Book
        'integrationuser',  # Username
        '1',  # Select first book
        '5'  # Exit
    ])
    def test_return_book_workflow(self, mock_input):
        # First, borrow a book
        self.book_loans.borrow_book('integrationuser', self.book)
        self.assertEqual(self.book.num_available, 4)

        loans_menu = LoansMenu(self.book_list, self.user_list, self.book_loans)
        loans_menu.display()

        # Check that the book has been returned
        self.assertEqual(self.book.num_available, 5)
        self.assertEqual(len(self.book_loans.loans['integrationuser']), 0)

class TestValidationFunctions(unittest.TestCase):
    def test_non_empty(self):
        self.assertTrue(non_empty("test"))
        self.assertFalse(non_empty(""))

    def test_positive_int(self):
        self.assertTrue(positive_int("5"))
        self.assertFalse(positive_int("0"))
        self.assertFalse(positive_int("-1"))
        self.assertFalse(positive_int("abc"))

    def test_non_negative_int(self):
        self.assertTrue(non_negative_int("0"))
        self.assertTrue(non_negative_int("5"))
        self.assertFalse(non_negative_int("-1"))
        self.assertFalse(non_negative_int("abc"))

    def test_valid_date(self):
        self.assertTrue(valid_date("2020-01-01"))
        self.assertFalse(valid_date("2020-13-01"))
        self.assertFalse(valid_date("invalid-date"))

    def test_valid_email(self):
        self.assertTrue(valid_email("test@example.com"))
        self.assertFalse(valid_email("invalid-email"))

class TestInitialization(unittest.TestCase):
    def test_init_library(self):
        book_list, user_list, loans = init_library()
        self.assertIsInstance(book_list, BookList)
        self.assertIsInstance(user_list, UserList)
        self.assertIsInstance(loans, Loans)
        self.assertGreater(book_list.get_total_books(), 0)
        self.assertGreater(user_list.get_total_users(), 0)

class TestGetInputFunction(unittest.TestCase):
    @patch('builtins.input', return_value='test')
    def test_get_input_non_empty(self, mock_input):
        result = get_input("Prompt:", non_empty, "Error")
        self.assertEqual(result, 'test')

    @patch('builtins.input', side_effect=['', 'test'])
    def test_get_input_retry(self, mock_input):
        result = get_input("Prompt:", non_empty, "Error")
        self.assertEqual(result, 'test')

    @patch('builtins.input', return_value='5')
    def test_get_input_positive_int(self, mock_input):
        result = get_input("Prompt:", positive_int, "Error")
        self.assertEqual(result, '5')

if __name__ == '__main__':
    unittest.main()
