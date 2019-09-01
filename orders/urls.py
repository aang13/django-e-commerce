from django.conf.urls import url 
from orders import views

urlpatterns =[
    url(r'^orders/$',views.orders_list)
]
