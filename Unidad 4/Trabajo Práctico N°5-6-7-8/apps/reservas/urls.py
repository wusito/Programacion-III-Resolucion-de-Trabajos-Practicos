from django.urls import path
from . import views

urlpatterns = [
    path('actividades/agregar/', views.agregar_actividad, name='agregar_actividad'),
    path('actividades/', views.lista_actividades, name='lista_actividades'),
    path('actividades/<int:pk>/', views.detalle_actividad, name='detalle_actividad'),
]