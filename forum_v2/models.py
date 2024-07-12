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

class Event(models.Model):
    user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    judul = models.CharField(max_length=300)
    detail = models.TextField()
    penyelenggara = models.CharField(max_length=300)
    lokasi = models.TextField()
    tanggal_mulai = models.DateField(null=True)
    tanggal_selesai = models.DateField(blank=True, null=True)
    waktu_mulai = models.TimeField(null=True)
    waktu_selesai = models.TimeField(blank=True, null=True)
    link_event = models.URLField(null=True, blank=True)
    nama_contact_person = models.CharField(max_length=50, null=True, blank=True)
    nomor_contact_person = models.CharField(max_length=20, null=True, blank=True)

class PesertaEvent(models.Model):
    peserta = models.CharField(max_length=50)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

