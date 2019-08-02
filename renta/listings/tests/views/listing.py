from renta.tests.base import BaseRentaTestCase

from rest_framework import status

from listings.models import Listing
from listings.tests.factories import ListingFactory
from accounts.tests.factories import UserFactory

from faker import Faker

from io import BytesIO
from PIL import Image

fake = Faker()


class ListingViewTestCase(BaseRentaTestCase):
    """
    Listing View Tests
    """

    base_url_name = 'listings'

    def setUp(self):
        self.user = UserFactory(email=fake.email())
        self.admin = UserFactory(is_admin=True)

        self.listing_one = ListingFactory()

        self.listing_update_data = { 'title': fake.color_name(), 'images': [] }
        self.listing_valid_create_data = {
            'title': fake.color_name(),
            'description': fake.sentence(nb_words=10),
            'price': 555,
            'location': fake.address(),
            'location_coordinates': f'{fake.latitude()},{fake.longitude()}',
            'images': [self.create_test_image(), self.create_test_image(), ]
        }

        self.sign_in_as_user(self.user)

    def create_test_image(self):
        file = BytesIO()
        image = Image.new('RGBA', size=(50, 50), color=(155, 0, 0))
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_list_listings_by_anon_succeeds(self):
        self.client.credentials()

        response = self.client.get(self.get_list_url())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_listings_by_auth_user_succeeds(self):
        response = self.client.get(self.get_list_url())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_listings_by_admin_succeeds(self):
        self.sign_in_as_user(self.admin)

        response = self.client.get(self.get_list_url())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_listing_by_anon_succeeds(self):
        self.client.credentials()

        response = self.client.get(self.get_detail_url(self.listing_one.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_listing_by_auth_user_succeeds(self):
        response = self.client.get(self.get_detail_url(self.listing_one.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_listing_by_admin_succeeds(self):
        self.sign_in_as_user(self.admin)

        response = self.client.get(self.get_detail_url(self.listing_one.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_listing_by_anon_fails(self):
        self.client.credentials()
        listing = ListingFactory()

        response = self.client.patch(self.get_detail_url(listing.id), self.listing_update_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_listing_by_non_owner_auth_user_fails(self):
        listing = ListingFactory()
        another_user = UserFactory()
        self.sign_in_as_user(another_user)

        response = self.client.patch(self.get_detail_url(listing.id), self.listing_update_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_listing_by_owner_auth_user_succeeds(self):
        owner = UserFactory()
        listing = ListingFactory(user=owner)
        self.sign_in_as_user(owner)

        response = self.client.patch(self.get_detail_url(listing.id), self.listing_update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), self.listing_update_data.get('title'))

    def test_update_listing_by_admin_succeeds(self):
        listing = ListingFactory()
        self.sign_in_as_user(self.admin)

        response = self.client.patch(self.get_detail_url(listing.id), self.listing_update_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json().get('title'), self.listing_update_data.get('title'))

    def test_delete_listing_by_anon_fails(self):
        self.client.credentials()

        response = self.client.delete(self.get_detail_url(self.listing_one.id))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_listing_by_non_owner_auth_user_fails(self):
        another_user = UserFactory()
        self.sign_in_as_user(another_user)

        response = self.client.delete(self.get_detail_url(self.listing_one.id))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_listing_by_owner_auth_user_succeeds(self):
        owner = UserFactory()
        listing = ListingFactory(user=owner)
        self.sign_in_as_user(owner)

        response = self.client.delete(self.get_detail_url(listing.id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_listing_by_admin_succeeds(self):
        self.sign_in_as_user(self.admin)

        response = self.client.delete(self.get_detail_url(self.listing_one.id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_listing_by_anon_with_valid_data_fails(self):
        self.client.credentials()

        response = self.client.post(self.get_list_url(), self.listing_valid_create_data)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_listing_by_anon_with_invalid_data_fails(self):
        self.client.credentials()

        response = self.client.post(self.get_list_url(), {'title': 'Hello world.'})

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_listing_by_auth_user_with_valid_data_succeeds(self):
        user = UserFactory()

        self.sign_in_as_user(user)

        response = self.client.post(self.get_list_url(), self.listing_valid_create_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_listing_by_auth_user_with_invalid_data_fails(self):
        user = UserFactory()

        self.sign_in_as_user(user)

        response = self.client.post(self.get_list_url(), {'title': 'Hello?'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_listing_by_admin_with_valid_data_succeeds(self):
        self.sign_in_as_user(self.admin)

        response = self.client.post(self.get_list_url(), self.listing_valid_create_data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_listing_by_admin_with_invalid_data_fails(self):
        self.sign_in_as_user(self.admin)

        response = self.client.post(self.get_list_url(), {'title': 'Hello?'})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
