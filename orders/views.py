from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status

from orders.models import Orders
from orders.Serializers import OrdersSerializers
# Create your views here.

@csrf_exempt
def orders_list(request):
    if request.method == 'GET':
        orders= Orders.objects.all();
        orders_serializer=OrdersSerializers(orders,many=True)
        return JsonResponse(orders_serializer.data, safe=False)
    elif request.method =='POST' :
        orders_data=JSONParser().parse(request)
        orders_serializer=OrdersSerializers(data=orders_data)
        if orders_serializer.is_valid():
            orders_serializer.save()
            return JsonResponse(orders_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(orders_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method== 'DELETE':
        Orders.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT) 
