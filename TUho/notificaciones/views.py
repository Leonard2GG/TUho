from django.shortcuts import redirect, render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from usuarios.models import Usuario
from .models import Notificacion
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Bandeja de entrada
@login_required
def Bandeja(request:HttpRequest) -> HttpResponse:
    usuario = request.user
    notificaciones = Notificacion.objects.filter(para=usuario)
    
    #Paginación de notitifcaciones
    paginator = Paginator(notificaciones,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"Notificaciones/Bandeja.html", {'page_obj':page_obj})

#Bandeja Admin
def BandejaAdmin(request:HttpRequest) -> HttpResponse:
    usuario = request.user
    notificaciones = Notificacion.objects.filter(para=usuario)
    
    #Paginación de notitifcaciones 
    paginator = Paginator(notificaciones,10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"Notificaciones/Bandeja Admin.html", {'page_obj':page_obj})