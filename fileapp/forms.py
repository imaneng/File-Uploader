from django import forms
from django.db import models
from django.db.models import fields
from .models import File


class GetFileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ('title','duc','uploader','upload_date')