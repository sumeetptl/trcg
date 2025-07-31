from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Blog(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    image = models.ImageField(upload_to='blogs/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
