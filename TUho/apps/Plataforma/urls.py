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
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('',(views.Inicio), name="Inicio"),
    path('MisTramites/',login_required (views.MisTramites), name="MisTramites"),
    path('InfoPersonal/',login_required (views.InformacionPersonal), name="InfoPersonal"),
    path('AtencionPoblacion/',login_required (views.AtencionPoblacion), name="AtencionPoblacion"),
    path('Administracion/',login_required (views.Administracion), name="Administracion"),
    path('Tramites/',login_required (views.Tramites), name="Tramites"),
    path('Usuarios/',login_required (views.Usuarios), name="Usuarios"),
    path('EliminarUsuario/<int:id>/',login_required (views.EliminarUsuario), name="EliminarUsuario"),
    path('CambiarRol/<int:id>/',login_required (views.CambiarRol), name="CambiarRol"),
    path('NoticiasUsuario/', views.NoticiasUsuario, name="NoticiasUsuario"),
    path('InstalarModulosPDF/',login_required (views.InstalarModulosPDF), name="InstalarModulosPDF"),
    
    #Noticias
    path('Noticias/',login_required (views.NoticiasView), name="Noticias"),
    path('CrearNoticia/',login_required (views.CrearNoticia), name="CrearNoticia"),
    path('EditarNoticia/<int:id>/',login_required (views.EditarNoticia), name="EditarNoticia"),
    path('EliminarNoticia/<int:id>/',login_required (views.EliminarNoticia), name="EliminarNoticia"),
]