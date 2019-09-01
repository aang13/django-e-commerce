from django.shortcuts import render 
from django.http import HttpResponse
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser 
from rest_framework import status

from users.models import Users
from users.Serializers import UsersSerializer
# Create your views here.

@csrf_exempt
def user_list(request):
    if request.method == 'GET':
        users= Users.objects.all();
        users_serializer=UsersSerializer(users,many=True)
        return JsonResponse(users_serializer.data, safe=False)
    elif request.method =='POST' :
        users_data=JSONParser().parse(request)
        users_serializer=UsersSerializer(data=users_data)
        if users_serializer.is_valid():
            users_serializer.save()
            return JsonResponse(users_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(users_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method== 'DELETE':
        Users.objects.all().delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)




