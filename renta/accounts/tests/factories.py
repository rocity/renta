import factory

from django.contrib.auth import get_user_model

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
    """

    class Meta:
        model = get_user_model()

    email = factory.lazy_attribute(
        lambda o: f'{fake.first_name()}{fake.last_name()}@{fake.free_email_domain()}'.lower()
    )
    first_name = factory.lazy_attribute(lambda o: fake.first_name())
    last_name = factory.lazy_attribute(lambda o: fake.last_name())
