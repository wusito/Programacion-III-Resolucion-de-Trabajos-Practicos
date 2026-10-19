from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('actividades/', views.lista_actividades, name='lista_actividades'),
    path('inscribirse/', views.inscribirse, name='inscribirse'),
    path('mis-inscripciones/', views.mis_inscripciones, name='mis_inscripciones'),
    path('actividades/agregar/', views.agregar_actividad, name='agregar_actividad'),
    path('actividades/', views.lista_actividades, name='lista_actividades'),
    path('actividades/<int:pk>/', views.detalle_actividad, name='detalle_actividad'),
]