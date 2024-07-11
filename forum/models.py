from django.db import models

# Create your models here.
from authentication.models import RegisteredUser

class Post(models.Model):
    user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)

class Event(models.Model):
    user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    judul = models.CharField(max_length=300)
    detail = models.TextField()
    penyelenggara = models.CharField(max_length=300)
    lokasi = models.TextField()
    tanggal_waktu_mulai = models.DateTimeField(auto_now_add=True, blank=True)
    tanggal_waktu_selesai = models.DateTimeField(auto_now_add=True, blank=True)
    link_event = models.URLField(null=True, blank=True)
    nama_contact_person = models.CharField(max_length=50, null=True, blank=True)
    nomor_contact_person = models.CharField(max_length=20, null=True, blank=True)

class PesertaEvent(models.Model):
    peserta = models.CharField(max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

