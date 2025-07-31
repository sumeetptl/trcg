# users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('free', 'Free'),
        ('premium', 'Premium'),
        ('admin', 'Admin'),
    ]
    role = models.CharField(
        max_length=10, choices=ROLE_CHOICES, default='free')

    def __str__(self):
        return f"{self.username} ({self.role})"
