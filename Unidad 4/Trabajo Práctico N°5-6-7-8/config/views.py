from django.shortcuts import render
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registrarse(request):
    return render(request, 'registrarse.html')

def inscribirse(request):
    return render(request, 'inscribirse.html')

def mis_inscripciones(request):
    return render(request, 'mis_inscripciones.html')