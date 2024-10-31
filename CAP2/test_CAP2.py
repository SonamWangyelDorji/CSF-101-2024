import unittest

from CSF101_CAP2_02230301 import Library, Book, Admin, User

class TestingLibrarySystem(unittest.TestCase):
    # Method used to prepare the test fixture. 
    def setUp(self):
        self.library_system = Library()
        self.admin = Admin("ADMIN")
        self.user = User("USER_1")
        self.book = Book("Book","Author")
        

        # Add book in library by admin (Adding two books )
        self.admin.add_books_to_library(self.library_system, self.book)

    # Testing is user can successfully borrow a book and availability changes correctly
    def test_valid_book_borrowing(self):
        self.user.borrow(self.library_system, "Book")

        #Checking the books availability statust after borrow(unit testing to compare test value with false)
        self.assertFalse(self.book.availability_status)

        #Check if the borrowed book is in users "Borrowed_book list"
        self.assertIn(self.book, self.user.book_borrowed)


if __name__ == "__main__":
    unittest.main()