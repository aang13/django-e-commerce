from django.db import models

# Create your models here.
class Users(models.Model):
    name=models.CharField(max_length=70, blank=False,default='')
    email=models.EmailField()
    password=models.CharField(max_length=30,blank=False)
    mobile=models.IntegerField()
    type=models.BooleanField()
