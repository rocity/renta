from renta.tests.base import BaseRentaTestCase

from rest_framework import status

from listings.models import Listing
from listings.tests.factories import ListingFactory
from accounts.tests.factories import UserFactory

from faker import Faker


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

        self.listing_update_data = { 'title': fake.color_name() }

        self.sign_in_as_user(self.user)

    def test_list_listings_by_anon_succeeds(self):
        self.client.credentials()

        response = self.client.get(self.get_list_url())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_listings_by_auth_user_succeeds(self):
        response = self.client.get(self.get_list_url())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_listings_by_admin_succeeds(self):
        self.sign_in_as_user(self.admin)

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

        response = self.client.delete(self.get_detail_url(listing.id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_listing_by_admin_succeeds(self):
        self.sign_in_as_user(self.admin)

        response = self.client.delete(self.get_detail_url(self.listing_one.id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
