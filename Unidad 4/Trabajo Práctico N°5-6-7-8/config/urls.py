"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

    path('registrarse/', views.registrarse, name='registrarse'),
        path('actividades/', views.lista_actividades, name='lista_actividades'),
        path('inscribirse/', views.inscribirse, name='inscribirse'),
        path('mis-inscripciones/', views.mis_inscripciones, name='mis_inscripciones'),
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from .views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('inscribirse/', views.inscribirse, name='inscribirse'),
    path('mis-inscripciones/', views.mis_inscripciones, name='mis_inscripciones'),
    # URLs de las Apps.
    path('', include('apps.reservas.urls')),
]