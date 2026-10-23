from django.contrib import admin
from .models import ActividadDeportiva, Horario, Inscripcion

# Register your models here.

# 1. Personalización para Actividad Deportiva
@admin.register(ActividadDeportiva)
class ActividadDeportivaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'lugar', 'cupo')  # Columnas visibles en la lista
    search_fields = ('nombre', 'lugar')          # Campos habilitados para la barra de búsqueda

# 2. Personalización para Horario
@admin.register(Horario)
class HorarioAdmin(admin.ModelAdmin):
    list_display = ('actividad_deportiva', 'dia', 'hora_inicio', 'hora_fin')
    search_fields = ('actividad_deportiva__nombre', 'dia') # Permite buscar por el nombre de la actividad relacionada

# 3. Personalización para Inscripción
@admin.register(Inscripcion)
class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('apellido', 'nombre', 'dni', 'estado', 'fecha_inscripcion')
    search_fields = ('apellido', 'nombre', 'dni', 'email')
    list_filter = ('estado', 'nivel_deportivo') # Extra útil: filtros laterales