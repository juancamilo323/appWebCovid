from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request): #Aqui estará el mapa de calor y filtro de ver contagios
    return render(request, "appWebCovidApp/home.html")

def get_registro_contagio(request): #Aqui se ingresará un contagio
    return render(request, "appWebCovidApp/ingresarContagio.html")
