from rest_framework.test import APITestCase
from django.urls import reverse
from users.models import User
from rest_framework import status


class BlogTestCase(APITestCase):
    def setUp(self):
        self.admin = User.objects.create_user(
            username="admin", password="pass", role="admin")
        self.client.login(username="admin", password="pass")

    def test_admin_can_create_blog(self):
        self.client.force_authenticate(user=self.admin)
        response = self.client.post('/api/blogs/', {
            'title': 'Test Blog',
            'content': 'Sample content'
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
