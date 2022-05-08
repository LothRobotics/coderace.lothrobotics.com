from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('str:lobby_name', views.lobby, name='lobby')
]
