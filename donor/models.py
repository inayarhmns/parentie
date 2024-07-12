from django.db import models
from authentication.models import RegisteredUser

# Create your models here.
class Donor(models.Model):
    user = models.ForeignKey(RegisteredUser, on_delete=models.CASCADE)
    timestamp = models.DateField()
    tag = models.CharField()
    document = models.FileField(upload_to='donor_documents/', default=None, null=True, blank=True)
    selesai = models.BooleanField(default=0, null=True, blank=True)

    def mark_as_done(self):
        self.selesai = True
        self.save()