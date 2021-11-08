from django.urls import path
from appWebCovidApp import views

urlpatterns = [
    path('mapa-colombia', views.get_registro_contagio, name='Contagio'),
]