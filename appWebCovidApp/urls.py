from django.urls import path
from appWebCovidApp import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('ingresarcontagio', views.get_registro_contagio, name='Contagio'),
]