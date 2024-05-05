from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    avatar_url = models.CharField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
