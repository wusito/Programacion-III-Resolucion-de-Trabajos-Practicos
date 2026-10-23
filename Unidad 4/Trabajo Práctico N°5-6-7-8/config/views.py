from django.shortcuts import render
from django.contrib import messages
from apps.reservas.models import ActividadDeportiva

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registrarse(request):
    return render(request, 'registrarse.html')

def inscribirse(request):
    actividades = ActividadDeportiva.objects.all() # Consulta todas las actividades en SQLite3.
    return render(request, 'inscribirse.html', {'actividades': actividades})

def mis_inscripciones(request):
    return render(request, 'mis_inscripciones.html')