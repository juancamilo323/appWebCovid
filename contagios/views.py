from django.shortcuts import render
from contagios.models import Colombia, Departamento

# Create your views here.

def home(request): #Aqui estará el mapa de calor y filtro de ver contagios
    colombia = Colombia.objects.all()
    departamento = Departamento.objects.all()
    return render(request, "contagios/home.html", {"colombia": colombia, "departamento": departamento})

def Departamento_id(request, departamento_id):
    colombia = Colombia.objects.all()
    departamento = Departamento.objects.all()
    nombre = departamento_id
    departamento_id = Colombia.objects.filter(departamento_id = departamento_id)
    return render(request, "contagios/departamentos.html", {"colombia": colombia, "departamento": departamento, "departamento_id": departamento_id, "nombre": nombre})
