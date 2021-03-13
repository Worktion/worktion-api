from datetime import timedelta
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import AccessToken

User = get_user_model()


class AuthenticationTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
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

    def test_token_login_bad_request(self):
        url = reverse('login_account')
        data = {
            "email": "test@a.com",
            "password": "12345678"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = {
            "email": "test@a.com",
            "password": "12345ddd678"
        }
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        data = {
            "email": "",
            "password": ""
        }
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_token_login(self):
        url = reverse('login_account')
        self.user.validate_email()
        data = {
            "email": "test@a.com",
            "password": "12345678"
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_token_refresh(self):
        url_login = reverse('login_account')
        url_refresh = reverse('refresh_token_account')
        self.user.validate_email()
        data = {
            "email": self.user.email,
            "password": '12345678',
        }
        response_login = self.client.post(url_login, data, format='json')
        data_refresh = {
            "refresh": response_login.data['refresh'],
        }
        response_refresh = self.client.post(url_refresh, data_refresh, format='json')
        self.assertEqual(response_refresh.status_code, status.HTTP_200_OK)

    def test_confirm_account_bad_request(self):
        client = APIClient()
        token = AccessToken.for_user(self.user)
        token.set_exp(lifetime=timedelta(milliseconds=3))
        client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + str(token)
        )
        response = client.post('/api/users/confirm-email/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_confirm_account_good_request(self):
        client = APIClient()
        token = AccessToken.for_user(self.user)
        token.set_exp(lifetime=timedelta(days=30))
        client.credentials(
            HTTP_AUTHORIZATION='Bearer ' + str(token)
        )
        response = client.post('/api/users/confirm-email/')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['email_verified'])


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
        self.assertEqual(response.status_code, status.HTTP_200_OK)
