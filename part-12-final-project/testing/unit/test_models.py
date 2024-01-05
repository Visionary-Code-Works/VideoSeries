
import unittest
from app.models import ExampleModel
from app import db

class TestModels(unittest.TestCase):
    def setUp(self):
        # Setup code before each test method
        db.create_all()

    def tearDown(self):
        # Cleanup code after each test method
        db.session.remove()
        db.drop_all()

    def test_example_model_creation(self):
        # Test for creating an example model
        model = ExampleModel(name='Test Model')
        db.session.add(model)
        db.session.commit()
        self.assertIsNotNone(model.id)
        self.assertEqual(model.name, 'Test Model')

if __name__ == '__main__':
    unittest.main()
