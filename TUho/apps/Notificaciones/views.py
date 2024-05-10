from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from apps.Usuarios.models import Usuario

# Bandeja de entrada
def Bandeja(request:HttpRequest) -> HttpResponse:

    return render(request,"Notificaciones/Bandeja.html")