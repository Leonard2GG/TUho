from .forms import InformacionPersonal
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render


# Create your views here.


@login_required
def ActualizarInf(request:HttpRequest):
    if request.POST:
        usuario = Usuario.objects.get(id=request.user.id)
        usuario.first_name = request.POST['first_name']
        usuario.last_name = request.POST['last_name']
        usuario.carnet = request.POST['carnet']
        usuario.email = request.POST['email']
        usuario.telefono = request.POST['telefono']
        usuario.direccion = request.POST['direccion']
        usuario.save()
        return redirect("InfoPersonal")
    
    form = InformacionPersonal()
    return render(request,"Usuario/Actualizar Informacion Personal.html",{"form":form})
    







