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

    #Testing to borrow a book that is alredy borrowed
    def test_invalid_book_borrowing(self):
        self.user.borrow(self.library_system, "Book")
        borrowing_same_book = self.user.borrow(self.library_system, "Book")

        # Verify borrowing attempt fails
        self.assertIsNone(borrowing_same_book)


    #Testing if user can sucessfully return book and availability status in library and users "borrowed_book" list does not contain the book
    def test_valid_book_returning(self):
        self.user.borrow(self.library_system, "Book")
        self.user.return_book(self.library_system, "Book")
        #Test if book has been returned
        self.assertTrue(self.book.availability_status)
        #Test if the users book_borrowed list is empty
        self.assertEqual(self.user.book_borrowed, [])
    
    #Returning a book that hasnt been borrowed
    def test_invalid_book_returning(self):
        returning_unborrowed_book = self.user.return_book(self.library_system,"Book")
        #Verify return attempt fail
        self.assertEqual(returning_unborrowed_book,"You don't have 'Book' borrowed.")

    #Ensuring Admin can add Book and is appeared in library
    def test_admin_adding_books(self):
        add_book_by_admin = Book("Added_Book","Author")
        self.admin.add_books_to_library(self.library_system, add_book_by_admin)

        #Verify the new book is in Library
        self.assertIn(add_book_by_admin, self.library_system.books)
        #Check availability status of new book
        self.assertTrue(add_book_by_admin.availability_status)

if __name__ == "__main__":
    unittest.main()