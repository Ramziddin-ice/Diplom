from django.db import models
from file_storge.models import Storge_file,Mytext
# Create your models here.
class Shingle_model(models.Model):
    text_file1 = models.ForeignKey(Storge_file,related_name='first_text_file',on_delete=models.CASCADE)
    text_file2 = models.ForeignKey(Storge_file,related_name='second_text_file',on_delete=models.CASCADE)
    part = models.PositiveSmallIntegerField()
    as_like = models.CharField(max_length=250)


class Shingle_text_model(models.Model):
    text_1 = models.ForeignKey(Mytext,related_name='first_text',on_delete=models.CASCADE)
    text_2 = models.ForeignKey(Mytext,related_name='second_text',on_delete=models.CASCADE)
    part = models.PositiveSmallIntegerField()
    as_like = models.CharField(max_length=250)

class Textbase(models.Model):
    text_main=models.TextField(unique=True)