from django.db import models

# Create your models here.
from authentication.models import RegisteredUser

class Discussion(models.Model):
    user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True)

class Comment(models.Model):
    post = models.ForeignKey(Discussion, related_name="comment", on_delete=models.CASCADE)
    user_commenting = models.ForeignKey(RegisteredUser,on_delete =models.CASCADE) 
    body = models.TextField()
    date_added =models.DateTimeField(auto_now_add=True)