from django.db import models
from authentication.models import RegisteredUser

# Create your models here.
class Donor(models.Model):
    user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    timestamp = models.DateField()
    tag = models.CharField()
