from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ActividadDeportivaForm

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