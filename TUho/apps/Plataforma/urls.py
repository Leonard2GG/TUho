"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
"""
from django.urls import path
from apps.Plataforma import views

urlpatterns = [
    path('', views.Inicio, name="Inicio"),
    path('MisTramites/', views.MisTramites, name="MisTramites"),
    path('InfoPersonal/', views.InformacionPersonal, name="InfoPersonal"),
    path('AtencionPoblacion/', views.AtencionPoblacion, name="AtencionPoblacion"),
    path('Login/', views.Login, name="Login"),
    path('Registrar/', views.Registrar, name="Registrar"),
    path('Administracion/', views.Administracion, name="Administracion"),
    path('RolTramite/', views.RolTramite, name="RolTramite"),
    path('RolUsuario/', views.RolUsuario, name="RolUsuario"),
]