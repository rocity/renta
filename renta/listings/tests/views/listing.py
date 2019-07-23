from renta.tests.base import BaseRentaTestCase

from rest_framework import status


from faker import Faker


class ListingViewTestCase(BaseRentaTestCase):
    """
    Listing View Tests
    """

    base_url_name = 'listings'

    def setUp(self):
        self.user = UserFactory(email=fake.email())
        self.admin = UserFactory(is_admin=True)

        self.sign_in_as_user(self.user)

    def test_list_listings_by_anon_succeeds(self):
        pass

    def test_list_listings_by_auth_user_succeeds(self):
        pass

    def test_list_listings_by_admin_succeeds(self):
        pass

    def test_get_listing_by_anon_succeeds(self):
        pass

    def test_get_listing_by_auth_user_succeeds(self):
        pass

    def test_get_listing_by_admin_succeeds(self):
        pass

    def test_update_listing_by_anon_fails(self):
        pass

    def test_update_listing_by_non_owner_auth_user_fails(self):
        pass

    def test_update_listing_by_owner_auth_user_succeeds(self):
        pass

    def test_update_listing_by_admin_succeeds(self):
        pass

    def test_delete_listing_by_anon_fails(self):
        pass

    def test_delete_listing_by_non_owner_auth_user_fails(self):
        pass

    def test_delete_listing_by_owner_auth_user_succeeds(self):
        pass

    def test_delete_listing_by_admin_succeeds(self):
        pass
