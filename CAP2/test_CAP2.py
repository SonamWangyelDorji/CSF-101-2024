# Reference 
# https://gist.github.com/mogproject/fc7c4e94ba505e95fa03
# https://kapeli.com/cheat_sheets/Python_unittest_Assertions.docset/Contents/Resources/Documents/index
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.setUp
# https://medium.com/@sachinsoni600517/unit-testing-in-python-a-comprehensive-guide-for-beginners-985eec71bb4d
# https://realpython.com/python-unittest/

import unittest

from CSF101_CAP2_02230301 import Library, Book, Admin, User

class TestingLibrarySystem(unittest.TestCase):
    # Method used to prepare the test fixture. 
    def setUp(self):
        self.library_system = Library()
        self.admin = Admin("ADMIN")
        self.user = User("USER_1")
        self.book = Book("Book","Author")
        # Add book in library
        self.admin.add_books_to_library(self.library_system, self.book)

    # Testing if user can successfully borrow a book and availability changes correctly
    def test_valid_book_borrowing(self):
        self.user.borrow(self.library_system, "Book")

        #Checking the books availability status after borrow(unit testing to compare test value with false)
        self.assertFalse(self.book.availability_status)

        #Check if the borrowed book is in users "Borrowed_book list"
        self.assertIn(self.book, self.user.book_borrowed)

    #Testing to borrow a book that has been already borrowed
    def test_invalid_book_borrowing(self):
        self.user.borrow(self.library_system, "Book")
        borrowing_same_book = self.user.borrow(self.library_system, "Book")

        # Verify borrowing attempt failure
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


    #TEST edge/boundry CASE: borrowing all books from library
    def test_borrow_all_books(self):
        #Add book for testing
        book1 = Book("Test_Book1","Author1")
        self.admin.add_books_to_library(self.library_system,book1)
        #Borrow all book from library
        self.user.borrow(self.library_system,"Test_Book1")
        self.user.borrow(self.library_system,"Book")

        #Check available book in library
        available_book = []
        for book in self.library_system.books:
            if book.availability_status == True:
                available_book.append(book)
    
        #Verify all books are borrowed
        self.assertEqual(len(available_book),0)

        #Check if all the mentioned borrowed books are in users "borrowed_book" list
        self.assertIn(self.book, self.user.book_borrowed)
        self.assertIn(book1, self.user.book_borrowed)
    
    #TEST edge/boundry CASE: returning books that were not borrowed
    def test_return_book_not_borrowed(self):
        returning_not_borrowed = self.user.return_book(self.library_system, "No books borrowed")

        #Check error message
        self.assertEqual(returning_not_borrowed, "You don't have 'No books borrowed' borrowed.")
    
    #TEST edge/boundry CASE: borrowing a book that does not exist
    def test_borrow_nonexistent_book(self):
        #Borrow a book that does not exist
        borrow_nonexistent = self.user.borrow(self.library_system, "Book that doesnt exist")
        #Verify error message
        self.assertIsNone(borrow_nonexistent)

    #TEST edge/boundry CASE: return book that does not exist
    def test_return_nonexistent_book(self):
        #return non_existent book
        return_nonexistent_book = self.user.return_book(self.library_system, "Return Book that doesnt exist")
        #Verify error message
        self.assertEqual(return_nonexistent_book, "You don't have 'Return Book that doesnt exist' borrowed.")


    #TEST edge/boundry CASE: validate if the book borrowed is kept tracked or not 
    def test_valid_tracking_of_books_borrowed(self):
        # Add book for testing 
        add_book_for_testing = Book("Harry Potter","J.K Rowling")
        self.admin.add_books_to_library(self.library_system, add_book_for_testing)
        # User borrows book
        self.user.borrow(self.library_system, "Harry Potter")
        #Check if the borrowed book is in users "Borrowed_book list"
        self.assertIn(add_book_for_testing, self.user.book_borrowed)
        #Check if the booked borrowed is tracked in the library's log
        self.assertIn(add_book_for_testing, self.library_system.borrowed_book_log)
    
    
if __name__ == "__main__":
    unittest.main()