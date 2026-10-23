from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ActividadDeportivaForm, ActividadDeportiva

# Create your views here.

def agregar_actividad(request):
    if request.method == 'POST':
        form = ActividadDeportivaForm(request.POST)
        if form.is_valid():
            form.save()  # Guarda directamente en la base de datos SQLite.
            messages.success(request, 'La actividad deportiva se ha registrado con éxito!')
            return redirect('agregar_actividad')
        else:
            messages.error(request, 'Por favor, corrige los errores del formulario.')
    else:
        form = ActividadDeportivaForm()

    return render(request, 'reservas/agregar_actividad.html', {'form': form})


def lista_actividades(request):
    # Consulta todas las actividades deportivas registradas en la base de datos.
    actividades = ActividadDeportiva.objects.all()
    
    # Renderiza la plantilla enviando el listado de actividades.
    return render(request, 'reservas/lista_actividades.html', {'actividades': actividades})


def detalle_actividad(request, pk):
    # Obtiene la actividad por su ID o lanza un error 404 si no existe.
    actividad = get_object_or_404(ActividadDeportiva, pk=pk)
    
    # Renderiza la plantilla enviando los datos de la actividad.
    return render(request, 'reservas/detalle_actividad.html', {'actividad': actividad})