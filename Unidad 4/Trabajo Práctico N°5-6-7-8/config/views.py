from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from apps.reservas.models import ActividadDeportiva, Inscripcion

# Create your views here.

def index(request):
    return render(request, 'index.html')

def registrarse(request):
    return render(request, 'registrarse.html')

def inscribirse(request):
    actividades = ActividadDeportiva.objects.all() # Consulta todas las actividades en SQLite3.
    return render(request, 'inscribirse.html', {'actividades': actividades})

def mis_inscripciones(request):
    # 2. Obtener todas las inscripciones registrando las relaciones necesarias
    inscripciones = Inscripcion.objects.select_related('horario__actividad_deportiva').all()
    
    # 3. Enviar las inscripciones al contexto del template
    return render(request, 'mis_inscripciones.html', {'inscripciones': inscripciones})

def cancelar_inscripcion(request, pk):
    # Busca la inscripción o devuelve un error 404 si no existe
    inscripcion = get_object_or_404(Inscripcion, pk=pk)
    
    # Cambiamos el estado a 'CAN' (Cancelada)
    inscripcion.estado = 'CAN'
    inscripcion.save()
    
    messages.success(request, 'La inscripción ha sido cancelada correctamente.')
    return redirect('mis_inscripciones')