from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from usuarios.models import Usuario
from .models import Notificacion
from django.contrib.auth.decorators import login_required

# Bandeja de entrada
@login_required
def Bandeja(request:HttpRequest) -> HttpResponse:
    print(request.user)
    usuario = request.user
    notificaciones = Notificacion.objects.filter(para=usuario)
    return render(request,"Notificaciones/Bandeja.html", {'notificaciones': notificaciones})

def BandejaUsuario(request:HttpRequest) -> HttpResponse:
    print(request.user)
    usuario = request.user
    notificaciones = Notificacion.objects.filter(para=usuario)
    return render(request,"Notificaciones/Bandeja Usuario.html", {'notificaciones': notificaciones})