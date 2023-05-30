from django.db import models

# Create your models here.
import uuid

class Storge_file(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250)
    file = models.FileField(upload_to='documents/%Y/%m/%d')

class Mytext(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=250)
    text = models.TextField()