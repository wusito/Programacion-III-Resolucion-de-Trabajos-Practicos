from django.urls import path
from . import views

urlpatterns = [
    path('actividades/agregar/', views.agregar_actividad, name='agregar_actividad'),
]