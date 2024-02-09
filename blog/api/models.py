from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    "Модель постов"
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=False)

    def __str__(self):
        return self.text

    class Meta:
        ordering = ["-created_at"]