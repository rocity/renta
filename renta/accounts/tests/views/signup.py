from django.urls import reverse

from rest_framework import status

from renta.tests.base import BaseRentaTestCase
from accounts.tests.factories import UserFactory

from faker import Faker


fake = Faker()


class SignupViewTestCase(BaseRentaTestCase):
    """
    SignUp View Tests
    """

    url = reverse('signup')

    def setUp(self):
        self.user = UserFactory(email=fake.email())
        self.admin = UserFactory(is_admin=True)

        self.update_data = {'name': 'hello'}

        self.valid_post_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': 'secretPassword',
            'confirm_password': 'secretPassword'
        }

        self.invalid_post_data = {
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
            'password': '',
            'confirm_password': ''
        }

        self.sign_in_as_user(self.user)

    def get_detail_url(self, id):
        return reverse('signup', kwargs={'id': id})

    def test_list_signup_view_by_anon_fails(self):
        self.client.credentials()

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_list_signup_view_by_auth_user_fails(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_list_signup_view_by_admin_fails(self):
        self.sign_in_as_user(self.admin)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_signup_view_by_anon_fails(self):
        self.client.credentials()

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_signup_view_by_auth_user_fails(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_signup_view_by_admin_fails(self):
        self.sign_in_as_user(self.admin)

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_signup_view_by_anon_fails(self):
        self.client.credentials()

        response = self.client.patch(self.url, self.update_data)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_signup_view_by_auth_user_fails(self):
        response = self.client.patch(self.url, self.update_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_signup_view_by_admin_fails(self):
        self.sign_in_as_user(self.admin)

        response = self.client.patch(self.url, self.update_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_signup_view_by_anon_with_valid_data_succeeds(self):
        self.client.credentials()

        response = self.client.post(self.url, self.valid_post_data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json().get('first_name'), self.valid_post_data.get('first_name'))
        self.assertEqual(response.json().get('last_name'), self.valid_post_data.get('last_name'))
        self.assertEqual(response.json().get('email'), self.valid_post_data.get('email'))

    def test_post_signup_view_by_anon_with_invalid_data_fails(self):
        self.client.credentials()

        response = self.client.post(self.url, self.invalid_post_data)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_post_signup_view_by_auth_user_with_valid_data_fails(self):
        response = self.client.post(self.url, self.valid_post_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_signup_view_by_auth_user_with_invalid_data_fails(self):
        response = self.client.post(self.url, self.valid_post_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_signup_view_by_admin_with_valid_data_fails(self):
        self.sign_in_as_user(self.admin)

        response = self.client.post(self.url, self.valid_post_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_post_signup_view_by_admin_with_invalid_data_fails(self):
        self.sign_in_as_user(self.admin)

        response = self.client.post(self.url, self.valid_post_data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_signup_view_by_anon_fails(self):
        self.client.credentials()

        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_delete_signup_view_by_auth_user_faisl(self):
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_signup_view_by_admin_fails(self):
        self.sign_in_as_user(self.admin)

        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
