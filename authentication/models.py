from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class RegisteredUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    peran = models.CharField()
    nama = models.CharField()
    umur = models.IntegerField(default=None, null=True, blank=True)
    domisili = models.CharField()
    golongan_darah = models.CharField(default=None, null=True, blank=True)
    kondisi_ibu = models.CharField(default=None, null=True, blank=True)

class Bayi(models.Model):
    umur = models.IntegerField()
    jenis_kelamin = models.CharField()
    orang_tua = models.OneToOneField(RegisteredUser, on_delete=models.CASCADE)
