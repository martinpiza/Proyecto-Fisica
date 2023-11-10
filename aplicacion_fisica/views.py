# aplicacion_fisica/views.py
from django.shortcuts import render
from .models import Articulo

def index(request):
    return render(request, 'aplicacion_fisica/index.html')

def movimiento_circular(request):
    articulos = Articulo.objects.filter(titulo__icontains='movimiento circular')
    return render(request, 'aplicacion_fisica/movimiento_circular.html', {'articulos': articulos})

def fuerza(request):
    articulos = Articulo.objects.filter(titulo__icontains='fuerza')
    return render(request, 'aplicacion_fisica/fuerza.html', {'articulos': articulos})

def leyes_newton(request):
    articulos = Articulo.objects.filter(titulo__icontains='leyes de newton')
    return render(request, 'aplicacion_fisica/leyes_newton.html', {'articulos': articulos})
