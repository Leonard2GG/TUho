from django.shortcuts import render, HttpResponse

# Create your views here.

def Inicio(request):
    return render(request,"Inicio.html")

def MisTramites(request):
    return render(request,"Mis Trámites.html")

def InformacionPersonal(request):
    return render (request,"Informacion Personal.html")

def AtencionPoblacion(request):
    return render (request,"Atención a la Poblacion.html")

def Login(request):
    return render (request,"Login.html")

def Registrar(request):
    return render (request,"Registrar.html")

def Administracion(request):
    return render (request,"Sitio Administrativo.html")

def RolTramite(request):
    return render (request,"Base Roles Tramites.html")

def RolUsuario(request):
    return render (request,"Base Roles Usuarios.html")









