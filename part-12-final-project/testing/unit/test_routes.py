
import unittest
from app import app

class TestRoutes(unittest.TestCase):
    def setUp(self):
        # Setup code before each test method
        app.testing = True
        self.client = app.test_client()

    def test_index_route(self):
        # Test for the index route
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to the Web-Based Data Dashboard', response.data.decode())

if __name__ == '__main__':
    unittest.main()
