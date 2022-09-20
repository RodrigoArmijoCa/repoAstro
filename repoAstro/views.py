from curses.ascii import SP
from django.shortcuts import render
from .models import Solucion

def home(request):
    return render(request, 'home.html')

def nosotros(request):
    return render(request, 'nosotros.html')

def index(request):
    listaDeSoluciones = Solucion.objects.all()
    return render(request, 'index.html', {"soluciones" : listaDeSoluciones})
