
from django.urls import reverse
from django.contrib.auth.hashers import make_password

from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class BaseRentaTestCase(APITestCase):
    """
    Base Test Case complete with user login and client setup.
    """

    base_url_name = None
    url = None

    password_string = 'password'

    class setUp(self):
        self.client = APIClient()

        if self.base_url_name:
            # Set default url to "list"
            self.url = reverse(f'{self.base_url_name}-list')

    def sign_in_as_user(self, user, password=self.password_string):
        """
        Set user session into current test run.

        :param: user - The user instance
        :param: password - The user's password in plaintext
        """

        self.client.credentials()
        credentials = {'username': user.email, 'password': password}
        token = self.client.post(reverse('api_token_auth'), credentials, format='json')
        self.client.credentials(HTTP_AUTHORIZATION='Token {}'.format(token.json().get('token')))

    def get_detail_url(self, object_id, base_url_name=None):
        """
        Reverse the detail URL for the given URL name.

        :param: object_id - The object's ID
        :param: base_url_name - Base name of the URL to reverse.
        """

        if not self.base_url_name and not base_url_name:
            raise AttributeError('No base URL name provided.')

        if not base_url_name:
            base_url_name = self.base_url_name

        return reverse(f'{base_url_name}-detail', kwargs={'pk': object_id})

    def get_list_url(self, base_url_name=None):
        """
        Reverse the detail URL for the given URL name.

        :param: base_url_name - Base name of the URL to reverse.
        """

        if not self.base_url_name and not base_url_name:
            raise AttributeError('No base URL name provided.')

        if not base_url_name:
            base_url_name = self.base_url_name

        return reverse(f'{base_url_name}-list')
