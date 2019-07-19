from django.urls import reverse
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from accounts.tests.factories import UserFactory

from faker import Faker


fake = Faker()


class ProfileViewTestCase(APITestCase):
    """
    Profile View Tests
    """

    def setUp(self):
        self.user = UserFactory(email=fake.email(), password=make_password('password'))

        self.client = APIClient()
        self.sign_in_as_user(self.user.email, 'password')

    def sign_in_as_user(self, user, password):
        self.client.credentials()
        credentials = {'username': user.email, 'password': password}
        token = self.client.post(reverse('api_token_auth'), credentials, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(token.json().get('token')))

    def test_list_profiles_by_anon_fails(self):
        pass

    def test_list_profiles_by_auth_user_succeeds(self):
        pass

    def test_list_profiles_by_admin_succeeds(self):
        pass

    def test_get_profile_by_anon_fails(self):
        pass

    def test_get_profile_by_auth_user_succeeds(self):
        pass

    def test_get_profile_by_admin_succeeds(self):
        pass

    def test_update_profile_by_anon_fails(self):
        pass

    def test_update_profile_by_non_owner_auth_user_fails(self):
        pass

    def test_update_profile_by_owner_auth_user_succeeds(self):
        pass

    def test_update_profile_by_admin_succeeds(self):
        pass

    def test_delete_profile_by_anon_fails(self):
        pass

    def test_delete_profile_by_auth_user_fails(self):
        pass

    def test_delete_profile_by_admin_succeeds(self):
        pass
