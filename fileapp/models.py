from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone





class File (models.Model):
    duc = models.FileField(null=True, blank=True, upload_to='myfile')
    title = models.CharField(max_length=100)
    uploader = models.OneToOneField(User , on_delete=models.CASCADE)
    upload_date = models.DateTimeField(default = timezone.now)

    def __str__(self) -> str:
        return self.title

