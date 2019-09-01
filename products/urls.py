from django.conf.urls import url 
from products import views

urlpatterns =[
    url(r'^products/$',views.products_list)
]