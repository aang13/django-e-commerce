from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status


from products.models import Products
from products.Serializers import ProductsSerializers
# Create your views here.

@csrf_exempt
def products_list(request):
    if request.method == 'GET':
        products= Products.objects.all();
        products_serializer=ProductsSerializers(products,many=True)
        return JsonResponse(products_serializer.data, safe=False)
    elif request.method =='POST' :
        products_data=JSONParser().parse(request)
        products_serializer=ProductsSerializers(data=products_data)
        if products_serializer.is_valid():
            products_serializer.save()
            return JsonResponse(products_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(products_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method== 'DELETE':
        Products.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)   
