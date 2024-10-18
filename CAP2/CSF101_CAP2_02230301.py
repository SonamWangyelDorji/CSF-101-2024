#Reference
# https://medium.com/@soumiksarkar178/building-a-library-management-system-in-python-my-first-project-a-jee-students-way-to-learn-ai-2983785665c8
# https://stackoverflow.com/questions/18665873/filtering-a-list-based-on-a-list-of-booleans
# https://www.geeksforgeeks.org/python-filter-list-by-boolean-list/
# https://www.w3schools.com/python/python_classes.asp
# https://python.land/python-data-types/python-list
# https://k4y0x13.github.io/CSF101-Programming-Methodology/OOP/Worksheet2.html
# https://www.geeksforgeeks.org/call-a-class-method-from-another-class-in-python/
# https://www.youtube.com/watch?v=GDymNBT_o_g
# https://www.youtube.com/watch?v=MZZSMaEAC2g

#Initializing class Book to store title,author and availability status.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.availability_status = True

#Initializing class Library to create features to implement in a library management system.
class Library:
    def __init__(self):
        self.books = []
        #Initialized a dictionary so that admin keep track of books borrowed by the user.
        self.borrowed_book_log = {}
    
    #Function to add book
    def add_book(self,book):
        self.books.append(book)
        print(f"The book titled '{book.title}' by '{book.author}' has been added to the library.")
    
    #Function to view all the book in the library.
    def view_all_books(self):
        #If the list books is empty:
        if not self.books:
            print("There are no books in the library")
        #If the list is not empty:
        else:
            print("Books in the library: \n")
            for book in self.books:
                if book.availability_status == True:
                    #Instead of availability status as true or false, replaceing it with Available / Not available.
                    status = "Available"
                else:
                    status = "Not Available"
                print(f"Title: {book.title}, Author: {book.author}, Status: {status} ")
    
    #Function that shows books which are available in the library.
    def view_book(self):
        if not self.books : 
            print("No books in the library") 
        else:
            #Initilized a list to store books which are available.
            books_available = []
            for book in self.books:
                if book.availability_status == True:
                    books_available.append(book)
            for book in books_available:
                print(f"Title: '{book.title}' Author: '{book.author}' \n")
    
    #Function to lend the book to the user and change its status in the library.
    def borrow_book(self,user,book_title):
        for book in self.books:
            if book.title == book_title and book.availability_status == True:
                book.availability_status = False
                self.borrowed_book_log[book] = user #Keep track on who borrowed the book
                user.book_borrowed.append(book) # Add the book borrowed to the users list 'book_borrowed'
                print(f"The book titled '{book.title}' has been borrowed.")
                return book
        print(f"Sorry, the book titled '{book_title}' is not available.")
        return None
    
    #Function to receive the book from the user and change its availability status.
    def return_book(self,user,book_title):
        for book in self.books:
            if book.title == book_title and book.availability_status == False:
                book.availability_status = True
                del self.borrowed_book_log[book] # Remove the key-value pair from the borrowed log when returned
                user.book_borrowed.remove(book) # Remove the book from the user's 'book_borrowed' list
                print(f"The book titled '{book.title}' has been returned.")
                return book 
        print(f"The book titled {book_title} was not found in the library.")
        return None

#Initializing user class to store user details and to provide functions to the users menu.
class User:
    def __init__(self,name):
        self.name = name
        self.book_borrowed = []
    #Function that uses method from the library class to borrow the book
    def borrow(self, library, book_title):
        library.borrow_book(self,book_title)
    #Function that uses method from the library class to return the book
    def return_book(self, library, book_title): 
        for book in self.book_borrowed:
            if book.title == book_title:
                library.return_book(self,book_title)
                return (f"You have given the book '{book_title}' back to the library.")    
        return(f"You don't have '{book_title}' borrowed.")
    

#Initializing user class to store Admin details and to provide functions to the users menu.
class Admin(User):
    def __init__(self, name):
        super().__init__(name)
    # Function that uses method from the library to add books.
    def add_books_to_library(self,library,book):
        library.add_book(book)
    # Function to keep track of books borrowed from the library.
    def track_books_borrowed(self,library):
        if not library.borrowed_book_log:
            print("No books are borrowed by the students")
        else:
            print("Books borrowed by the students: \n")
            for book,user in library.borrowed_book_log.items():
                print(f"Title: {book.title} By '{book.author}' has been borrowed by: {user.name}")

    # Function to view all the books in the library regardless of its status(avail/not avail).
    def view_all_books(self,library):
        library.view_all_books()



def main():
    library = Library()
    admin = Admin("Admin")
    print("==== Welcome To Library Management System ====")

    while True:
        #Used strip method to remove any trailing white spaces and  converted the input into lowercase to prevent error.
        user_type= input("\n Are you an Admin or a User? (admin/user) or if you want to exit just enter 'exit': ").strip().lower()
        if user_type == "exit":
            print("Thank you for using our Library System")
            break

        elif user_type == "admin":
            password = input("Enter Admin password: ")

            if password == "Admin123":
                print("........ Acessing Admin ........\n")
                while True:
                    print(" Admin Menu: ")
                    print("1. View all books")
                    print("2. View available books")
                    print("3. Add a book")
                    print("4. View borrowed books with user details")
                    print("5. Exit")
                    #Used strip method to remove any trailing white spaces
                    option = input("Choose an option: ").strip()

                    if option == "1":
                        print("\n Book in the Library: ")
                        admin.view_all_books(library)
                    
                    elif option == "2":
                        print("\n Available books in the library: ")
                        library.view_book()
                    
                    elif option == "3":
                        title = input("Enter the book title: ")
                        author = input("Enter the author name: ")
                        # Adding book detail to the class 'Book'
                        added = Book(title,author)
                        # Adding the book in the library
                        admin.add_books_to_library(library,added)
                    
                    elif option == "4":
                        admin.track_books_borrowed(library)

                    elif option == "5":
                        print("Exiting Admin Menu")
                        break

        elif user_type == "user":
            user_name = input("Enter your name: ")
            user = User(user_name)
            while True:
                print("\n User Menu: ")
                print("1. View available books")
                print("2. Borrow a book")
                print("3. Return a book")
                print("4. View your borrowed books")
                print("5. Exit")
                #Used strip method to remove any trailing white spaces
                User_option = input("Choose an option: ").strip()

                if User_option == "1":
                    print("\n Available Books: ")
                    library.view_book()
                
                elif User_option == "2":
                    title_input = input("Enter the title of the book to borrow: ")
                    user.borrow(library,title_input)
                
                elif User_option == "3":
                    title_input = input("Enter the title of the book to return: ")
                    user.return_book(library,title_input)
                
                elif User_option == "4":
                    print(f"{user_name} Borrowed Books: ")
                    if not user.book_borrowed:
                        print(f"{user_name} have not borrowed any book.")
                    else:
                        for book in user.book_borrowed:
                            print(f"Title: {book.title}, Author: {book.author}")
                elif User_option == "5":
                    print("Exiting User Menu")
                    break

        
            

#Calling the main function 
if __name__ == "__main__":
    main()

            

        
        