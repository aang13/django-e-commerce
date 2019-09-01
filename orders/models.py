from django.db import models
from users.models import Users
from products.models import Products

# Create your models here.
class Orders(models.Model):
    reference=models.CharField(max_length=30)
    customer=models.ForeignKey(Users,on_delete=models.CASCADE)
    total=models.FloatField()
    payment=models.BooleanField()
    status=models.BooleanField()
    date=models.DateTimeField()


