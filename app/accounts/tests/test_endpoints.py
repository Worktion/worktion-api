from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class AuthenticationTestCase(APITestCase):
    def setUp(self):
        User.objects.create_user(
            'test@a.com',
            '12345678',
            'test',
            'test',
            'test'
        )

    def test_registration_account(self):
        url = reverse('registration_account')
        data = {
            "first_name": "test",
            "last_name": "test",
            "username": "test2",
            "email": "test2@a.com",
            "password": "12345678"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(User.objects.get(username='test2').email, 'test2@a.com')

    def test_token_login(self):
        url = reverse('token_obtain_pair')
        data = {
            "email": "test@a.com",
            "password": "12345678"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_token_refresh(self):
        url = reverse('token_obtain_pair')
        reverse('token_refresh')
        data = {
            "email": "test@a.com",
            "password": "12345678"
        }
        response = self.client.post(url, data, format='json')
        data = {
            "refresh": response.data['refresh'],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AccountTestCase(APITestCase):
    def setUp(self):
        User.objects.create_user(
            'test@a.com',
            '12345678',
            'test',
            'test',
            'test'
        )
        url = reverse('token_obtain_pair')
        data = {
            "email": "test@a.com",
            "password": "12345678"
        }
        response = self.client.post(url, data, format='json')
        self.token = response.data['access']

    def test_account_detail_get(self):
        client = APIClient()
        client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = client.get('/api/users/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_account_detail_put(self):
        client = APIClient()
        client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + self.token
        )
        data = {
            "username": "new",
        }
        response = client.patch('/api/users/1/', data, format='json')
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
