from factory import DjangoModelFactory, SubFactory

from listings.models import Listing
from random import randint
from accounts.tests.factories import UserFactory

from faker import Faker

fake = Faker()


class ListingFactory(DjangoModelFactory):
    """
    Generates a Listing Instance

    Default Fields:
    - user
    - title
    - description
    - price
    - location
    """

    class Meta:
        model = Listing

    user = SubFactory(UserFactory)
    title = fake.color_name()
    description = fake.sentence(nb_words=10)
    price = randint(1, 200)
    location = fake.address()
