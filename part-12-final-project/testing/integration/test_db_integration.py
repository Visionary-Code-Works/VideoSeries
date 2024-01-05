import unittest
from app import db
from app.models import ExampleModel

class TestDBIntegration(unittest.TestCase):
    def setUp(self):
        # Setup for database integration testing
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        db.create_all()

    def tearDown(self):
        # Cleanup after tests
        db.session.remove()
        db.drop_all()

    def test_model_insertion(self):
        # Test insertion of a model into the database
        model = ExampleModel(name='Test Model')
        db.session.add(model)
        db.session.commit()
        self.assertIsNotNone(model.id)

    # Additional database integration tests can be added here

if __name__ == '__main__':
    unittest.main()
