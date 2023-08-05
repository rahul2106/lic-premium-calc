from django.urls import path
from . import views

urlpatterns = [
    path('get_api_call', views.get_api_call, name='get_api_call'),
    path('calculate', views.calculate, name='calculate'),
]
