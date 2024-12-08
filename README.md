# library-management-system
Library Management System

Introduction

This is a simple Flask API for a Library Management System. It allows for CRUD operations on books and members, as well as searching for books by title or author.

Prerequisites

Python 3.x
Flask
SQLite3
Installation

Clone this repository:
Bash
git clone https://github.com/shreyashpanage/library-management-system.git
Use code with caution.

Install the required packages:
Bash
pip install flask
Use code with caution.

Running the Application

Create a SQLite database file named library.db.
Run the Flask app:
Bash
python app.py
Use code with caution.

API Endpoints

Books

GET /books: Retrieves a list of all books.
POST /books: Creates a new book.
GET /books/int:book_id: Retrieves a specific book.
PUT /books/int:book_id: Updates a specific book.
DELETE /books/int:book_id: Deletes a specific book.
GET /books/search: Searches for books by title or author.
Members

GET /members: Retrieves a list of all members.
POST /members: Creates a new member.
GET /members/int:member_id: Retrieves a specific member.
PUT /members/int:member_id: Updates a specific member.
DELETE /members/int:member_id: Deletes a specific member.
Design Choices

SQLite: A simple and lightweight database for this project.
Flask: A lightweight web framework for rapid API development.
Plain Python: No external libraries for core functionality to keep the project simple and focused.
Assumptions and Limitations

Basic Authentication: For simplicity, the API does not include robust authentication and authorization mechanisms.
Limited Error Handling: Error handling is basic and could be improved.
No Pagination: Pagination is not implemented.
No Data Validation: Input data is not validated, which could lead to unexpected behavior.
Future Improvements

Implement robust authentication and authorization.
Add error handling and validation.
Implement pagination.
Consider using a more powerful database like PostgreSQL or MySQL for larger-scale applications.
Explore using a framework like SQLAlchemy for database interactions.
Add unit tests to ensure code quality.
