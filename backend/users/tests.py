from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User


class AuthTestCase(APITestCase):
    def test_user_registration_and_token(self):
        url = reverse('register')
        data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password': 'testpass123'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)

        token_url = reverse('token_obtain_pair')
        response = self.client.post(token_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertIn('access', response.data)
