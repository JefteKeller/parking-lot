from django.test import TestCase
from django.contrib.auth.models import User

from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token


class TestCreateListLevelView(TestCase):
    LEVELS_URL = '/api/levels/'

    def setUp(self):
        admin_user_data = {'username': 'admin', 'password': '1234'}

        admin_user = User.objects.create_superuser(**admin_user_data)
        admin_token = Token.objects.get_or_create(user=admin_user)[0]

        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {admin_token.key}')

        self.level_data_01 = {
            'name': 'floor 1',
            'fill_priority': 1,
            'motorcycle_spaces': 10,
            'car_spaces': 10
        }
        self.level_data_02 = {
            'name': 'floor 2',
            'fill_priority': 2,
            'motorcycle_spaces': 20,
            'car_spaces': 20
        }
        self.expected_level_data_response_01 = {
            'id': 1,
            'name': 'floor 1',
            'fill_priority': 1,
            'available_spaces': {
                'available_motorcycle_spaces': 10,
                'available_car_spaces': 10
            }
        }
        self.expected_level_data_response_02 = {
            'id': 2,
            'name': 'floor 2',
            'fill_priority': 2,
            'available_spaces': {
                'available_motorcycle_spaces': 20,
                'available_car_spaces': 20
            }
        }

    def test_should_list_levels(self):
        response_empty_list = self.client.get(self.LEVELS_URL)

        self.assertEqual(response_empty_list.data, [])
        self.assertEqual(response_empty_list.status_code, 200)

        expected_level_list = [
            self.expected_level_data_response_01,
            self.expected_level_data_response_02
        ]

        self.client.post(self.LEVELS_URL, self.level_data_01)
        self.client.post(self.LEVELS_URL, self.level_data_02)

        response_filled_list = self.client.get(self.LEVELS_URL)

        self.assertEqual(response_filled_list.data, expected_level_list)
        self.assertEqual(len(response_filled_list.data), 2)

    def test_should_not_create_level_with_invalid_data(self):
        invalid_data = {'name': 'floor 1', "fill_priority": 1}
        expected_error = {
            'motorcycle_spaces': ['This field is required.'],
            'car_spaces': ['This field is required.']
        }
        response = self.client.post(self.LEVELS_URL, invalid_data)

        self.assertDictEqual(response.data, expected_error)
        self.assertEqual(response.status_code, 400)

    def test_should_create_level(self):
        response = self.client.post(self.LEVELS_URL, self.level_data_01)

        self.assertDictEqual(response.data,
                             self.expected_level_data_response_01)
        self.assertEqual(response.status_code, 201)
