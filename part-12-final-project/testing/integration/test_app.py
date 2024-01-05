import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # Setup for testing the Flask application
        app.testing = True
        self.client = app.test_client()

    def test_home_page(self):
        # Test the home page route
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn('Welcome to the Web-Based Data Dashboard', response.data.decode())

    # Additional route tests can be added here

if __name__ == '__main__':
    unittest.main()
