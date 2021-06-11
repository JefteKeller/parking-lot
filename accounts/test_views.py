from django.test import TestCase, client

from rest_framework.test import APIClient


class TestCreateAdminView(TestCase):
    ACCOUNTS_URL = '/api/accounts/'

    def setUp(self):
        self.client = APIClient()

        self.user_data = {
            'username': 'admin',
            'password': '1234',
            'is_superuser': True,
            'is_staff': True
        }

    def test_should_create_admin_user(self):

        expected_user = {'id': 1, **self.user_data}
        del expected_user['password']

        response = self.client.post(self.ACCOUNTS_URL, self.user_data)

        self.assertDictEqual(response.data, expected_user)
        self.assertEqual(response.status_code, 201)

    def test_should_not_create_duplicated_user(self):
        expected_error = {'message': 'User already exists'}

        self.client.post(self.ACCOUNTS_URL, self.user_data)

        response = self.client.post(self.ACCOUNTS_URL, self.user_data)

        self.assertDictEqual(response.data, expected_error)
        self.assertEqual(response.status_code, 409)
