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
from usuarios import views 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views




urlpatterns = [
    path('Login/', views.Login, name="Login"),
    path('Registrar/', views.Registrar, name="Registrar"),
    path('CerrarSesion/',login_required(views.CerrarSesion), name="CerrarSesion"), 
    # Contraseña Olvidada
    path('verify/<token>', views.TokenValidationView , name="token_verify"),
    path('reset_password/', views.RestablecerContraseña.as_view() , name="password_reset"),
    path('reset_password_send/', views.RestablecerContraseñaConfirmado, name="password_reset_done"),
    path('reset/<uidb64>/<token>', views.CambiarContraseña.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', views.CambiarContraseñaConfirmado, name="password_reset_complete"),
     # Informacion Personal
    path('ActualizarInf/', login_required(views.ActualizarInf), name="ActualizarInf"),
]