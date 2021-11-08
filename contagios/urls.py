from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('<departamento_id>', views.Departamento_id , name="departamento_id")
]