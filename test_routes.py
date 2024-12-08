import unittest
from app import app
import requests

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_books(self):
        response = self.app.get('/books')
        self.assertEqual(response.status_code, 200)

    # ... similar tests for other routes ...
