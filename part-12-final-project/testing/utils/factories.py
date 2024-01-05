# Factories for generating test data

from factory import Factory, Faker
from app.models import ExampleModel

class ExampleModelFactory(Factory):
    class Meta:
        model = ExampleModel

    name = Faker('name')

# Additional factories for other models can be added here
