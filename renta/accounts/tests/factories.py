import factory

from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from faker import Faker


fake = Faker()

class UserFactory(factory.django.DjangoModelFactory):
    """
    User Factory
    Generates a User instance

    Default fields:
    - email
    - first_name
    - last_name
    - password (Defaults to 'password')
    """

    class Meta:
        model = get_user_model()

    email = factory.lazy_attribute(
        lambda o: f'{fake.first_name()}{fake.last_name()}@{fake.free_email_domain()}'.lower()
    )
    username = factory.lazy_attribute(lambda o: fake.user_name())
    first_name = factory.lazy_attribute(lambda o: fake.first_name())
    last_name = factory.lazy_attribute(lambda o: fake.last_name())
    password = make_password('password')
