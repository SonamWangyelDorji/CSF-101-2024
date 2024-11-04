## Overview
This file provides documentation for the test cases created to validate the functionality of the Library Management System. It covers the resources used, the reasoning behind their selection, and design apporach for the test cases.

## 1. Resources Used
- Python UNITTEST Module: The main resource used for developing the test cases is the unittest module.
- Referred online resources mentioned in the code

## 2. Justification for Using These Resources 
- Unittest offers simplicity and compatibility as it is a reliable for smaller projects.

- Unittest allows for the creation of modular test cases, where each test method can focus on a specific functionality, making it easy to understand and extend.

- Unittest makes it straighforward to run the entire suite automatically, making this a scalable testing choice for ongoing project development. 

## 3. Test case Design and Structure 

- Each test case (e.g. test_valid_book_borrowing, test_invalid_book_borrowing ..) is designed to test a specific functionality of the Library Management System.

- Tests includes edge cases (e.g. returning books that were not borrowed, borrowing all books from library, borrowing non_existent book etc..)

- Each test uses assertion (e.g assertIn, assertEqual, assertFalse) to confirm that actual outcomes match expected outcome.

- To run the test, enter the code provided below 
    ` `bash 
    python -m unittest 