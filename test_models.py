import unittest
from models import Book, Member
import sqlite3

class TestModels(unittest.TestCase):
    def setUp(self):
        self.conn = sqlite3.connect(':memory:')
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE books (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author TEXT, publication_year INTEGER)")

    def tearDown(self):
        self.conn.close()

    def test_book_save_and_get(self):
        book = Book(None, "Test Book", "Test Author", 2023)
        book.save(self.conn)
        books = Book.get_all(self.conn)
        self.assertEqual(len(books), 1)
        self.assertEqual(books[0].title, "Test Book")

# ... similar tests for other model methods ...
