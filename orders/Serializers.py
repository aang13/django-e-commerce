from rest_framework import serializers 
from orders.models import Orders


class OrdersSerializers(serializers.ModelSerializer):
    class Meta:
        model: Orders
        fields=('id','reference','customer','total','payment','status','date')