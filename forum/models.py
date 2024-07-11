from django.db import models

# Create your models here.
from authentication.models import RegisteredUser

class Post(models.Model):
    user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)