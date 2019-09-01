from rest_framework import serializers 
from products.models import Products

class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model:Products
        fields=('id','name','image','description','available_quantity','seller','price','selected_quantity')
        