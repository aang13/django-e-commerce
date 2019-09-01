from django.db import models
from users.models import Users

# Create your models here.
class Products(models.Model):
    name=models.CharField(max_length=70, blank=False,default='')
    image=models.CharField(max_length=255)
    description=models.CharField(max_length=70)
    available_quantity=models.IntegerField()
    seller=models.ForeignKey(Users, on_delete=models.CASCADE)
    price=models.FloatField()
    selected_quantity=models.IntegerField()
    



