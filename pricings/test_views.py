from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class TestCreatePricing(TestCase):
    PRICINGS_URL = '/api/pricings/'

    def setUp(self):
        admin_user_data = {'username': 'admin', 'password': '1234'}

        admin_user = User.objects.create_superuser(**admin_user_data)
        admin_token = Token.objects.get_or_create(user=admin_user)[0]

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {admin_token.key}')

    def test_should_not_create_pricing_with_invalid_data(self):
        invalid_data = {'a_coefficient': 50}
        expected_error = {
            'b_coefficient': ['This field is required.'],
        }

        response = self.client.post(self.PRICINGS_URL, invalid_data)

        self.assertEqual(response.data, expected_error)
        self.assertEqual(response.status_code, 400)

    def test_should_create_pricing(self):
        new_pricing_data = {
            'a_coefficient': 50,
            'b_coefficient': 100,
        }
        expected_response = {'id': 1, **new_pricing_data}

        response = self.client.post(self.PRICINGS_URL, new_pricing_data)

        self.assertEqual(response.data, expected_response)
        self.assertEqual(response.status_code, 201)
