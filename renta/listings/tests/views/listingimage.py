
from rest_framework import status

from renta.tests.base import BaseRentaTestCase

from listings.models import Listing, ListingImage
from listings.tests.factories import ListingFactory, ListingImageFactory
from accounts.tests.factories import UserFactory

from faker import Faker

fake = Faker()


class ListingImageViewTestCase(BaseRentaTestCase):
    """
    ListingImage Tests
    """

    base_url_name = 'listingimages'

    def setUp(self):
        self.user = UserFactory(email=fake.email())
        self.other_user = UserFactory(email=fake.email())
        self.admin = UserFactory(is_admin=True)

        self.listing_one = ListingFactory(user=self.user)
        self.listing_image_one = ListingImageFactory()

        self.valid_listing_image_update_data = {
            'image': self.create_test_image()
        }

        self.valid_listing_image_create_data = {
            'listing': self.listing_one.id,
            'image': self.create_test_image()
        }

        self.sign_in_as_user(self.user)

    def test_list_listing_image_by_anon_fails(self):
        self.client.credentials()

        response = self.client.get(self.get_list_url())

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_listing_image_by_auth_user_fails(self):
        self.sign_in_as_user(self.other_user)

        response = self.client.get(self.get_list_url())

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_listing_image_by_admin_succeeds(self):
        self.sign_in_as_user(self.admin)

        response = self.client.get(self.get_list_url())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_listing_image_by_anon_fails(self):
        self.client.credentials()

        response = self.client.get(self.get_detail_url(self.listing_image_one.id))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_listing_image_by_auth_user_fails(self):
        self.sign_in_as_user(self.other_user)

        response = self.client.get(self.get_detail_url(self.listing_image_one.id))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_listing_image_by_admin_succeeds(self):
        self.sign_in_as_user(self.admin)

        response = self.client.get(self.get_detail_url(self.listing_image_one.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_listing_image_by_anon_fails(self):
        self.sign_in_as_user(self.other_user)

        response = self.client.patch(
            self.get_detail_url(self.listing_image_one.id),
            self.valid_listing_image_update_data
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_listing_image_by_auth_user_on_owned_listing_succeeds(self):
        owned_listing = ListingFactory(user=self.user)
        owned_image = ListingImageFactory(listing=owned_listing)

        response = self.client.patch(
            self.get_detail_url(owned_image.id),
            self.valid_listing_image_update_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_listing_image_by_auth_user_on_not_owned_listing_fails(self):
        self.sign_in_as_user(self.other_user)

        response = self.client.patch(
            self.get_detail_url(self.listing_image_one),
            self.valid_listing_image_update_data
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_listing_image_by_admin_succeeds(self):
        self.sign_in_as_user(self.admin)

        response = self.client.patch(
            self.get_detail_url(self.listing_image_one),
            self.valid_listing_image_update_data
        )

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_listing_image_by_anon_fails(self):
        self.client.credentials()

        response = self.client.post(
            self.get_list_url(),
            self.valid_listing_image_create_data
        )

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_listing_image_by_auth_user_on_owned_listing_succeeds(self):
        response = self.client.post(
            self.get_list_url(),
            self.valid_listing_image_create_data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_listing_image_by_auth_user_on_not_owned_listing_fails(self):
        self.sign_in_as_user(self.other_user)

        response = self.client.post(
            self.get_list_url(),
            self.valid_listing_image_create_data
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_listing_image_by_admin_succeeds(self):
        self.sign_in_as_user(self.admin)

        response = self.client.post(
            self.get_list_url(),
            self.valid_listing_image_create_data
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
