from django.shortcuts import render, HttpResponse

# Create your views here.

def get_registro_contagio(request): #Aqui se ingresará un contagio
    return render(request, "appWebCovidApp/ingresarContagio.html")
