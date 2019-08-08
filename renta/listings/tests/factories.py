from django.core.files.base import ContentFile
from factory import DjangoModelFactory, SubFactory, LazyAttribute
from factory.django import ImageField

from listings.models import Listing, ListingImage
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


class ListingImageFactory(DjangoModelFactory):
    """
    Generates a ListingImage Instance

    Default Fields:
    - listing
    - image
    """
    class Meta:
        model = ListingImage

    listing = SubFactory(ListingFactory)
    image = LazyAttribute(
        lambda _: ContentFile(
            ImageField()._make_data(
                {'width': 1024, 'height': 768}
            ), 'example.jpg'
        )
    )
