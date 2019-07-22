from django.urls import reverse
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from renta.tests.base import BaseRentaTestCase
from accounts.tests.factories import UserFactory

from faker import Faker


fake = Faker()


class ProfileViewTestCase(BaseRentaTestCase):
    """
    Profile View Tests
    """

    base_url_name = 'profiles'

    def setUp(self):
        self.user = UserFactory(email=fake.email())
        self.admin = UserFactory(is_admin=True)

        self.profile_one = UserFactory()

        self.other_user = UserFactory(email=fake.email())

        self.sign_in_as_user(self.user)

    def test_list_profiles_by_anon_fails(self):
        self.client.credentials()

        response = self.client.get(self.get_list_url())

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_list_profiles_by_auth_user_succeeds(self):
        self.sign_in_as_user(self.other_user)

        response = self.client.get(self.get_list_url())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_profiles_by_admin_succeeds(self):
        self.sign_in_as_user(self.admin, password='password')

        response = self.client.get(self.get_list_url())

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_profile_by_anon_fails(self):
        self.client.credentials()

        response = self.client.get(self.get_detail_url(self.profile_one.id))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_profile_by_auth_user_succeeds(self):
        self.sign_in_as_user(self.other_user)

        response = self.client.get(self.get_detail_url(self.profile_one.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_profile_by_admin_succeeds(self):
        self.sign_in_as_user(self.admin)

        response = self.client.get(self.get_detail_url(self.profile_one.id))

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_profile_by_anon_fails(self):
        self.client.credentials()

        response = self.client.patch(self.get_detail_url(self.profile_one.id), {'first_name': 'Joe'})

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_profile_by_non_owner_auth_user_fails(self):
        self.sign_in_as_user(self.other_user)

        response = self.client.patch(self.get_detail_url(self.profile_one.id), {'first_name': 'Joe'})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_profile_by_owner_auth_user_succeeds(self):
        self.sign_in_as_user(self.profile_one)

        response = self.client.patch(self.get_detail_url(self.profile_one.id), {'first_name': 'Joe'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_profile_by_admin_succeeds(self):
        self.sign_in_as_user(self.admin)

        response = self.client.patch(self.get_detail_url(self.profile_one.id), {'first_name': 'Joe'})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_profile_by_anon_fails(self):
        self.client.credentials()

        response = self.client.delete(self.get_detail_url(self.profile_one.id))

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_profile_by_non_owner_auth_user_fails(self):
        self.sign_in_as_user(self.other_user)

        response = self.client.delete(self.get_detail_url(self.profile_one.id))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_profile_by_owner_auth_user_fails(self):
        self.sign_in_as_user(self.profile_one)

        response = self.client.delete(self.get_detail_url(self.profile_one.id))

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_profile_by_admin_succeeds(self):
        self.sign_in_as_user(self.admin)

        response = self.client.delete(self.get_detail_url(self.profile_one.id))

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_get_own_profile_by_anon_fails(self):
        pass

    def test_get_own_profile_by_non_owner_fails(self):
        pass

    def test_get_own_profile_by_owner_succeeds(self):
        pass

    def test_get_own_profile_by_admin_for_other_users_fail(self):
        pass
