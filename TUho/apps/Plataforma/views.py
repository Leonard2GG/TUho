from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.

@login_required
def Inicio(request):
    return render(request,"Inicio.html")

@login_required
def MisTramites(request):
    return render(request,"Mis Trámites.html")

@login_required
def InformacionPersonal(request):

    return render (request,"Informacion Personal.html")

@login_required
def AtencionPoblacion(request):
    if request.POST:
        print(request.POST.keys())
        email = request.user.email
        nombre = request.user.first_name
        last_name = request.user.last_name
        address = request.user.direccion
        municipality = request.POST['municipality']
        subject = request.POST['subject']
        message = request.POST['message']
        #email
        send_mail(
            subject= subject,
            message=f"Email: {email}\nNombre: {nombre}\nApellidos: {last_name}\nDireccion: {address}\nMuniciopio: {municipality}\nMensaje: {message}",
            from_email="mailtrap@demomailtrap.com",
            recipient_list= ["kiri05062001@gmail.com"]
        )
    return render (request,"Atención a la Poblacion.html")

@login_required
def Administracion(request):
    return render (request,"Sitio Administrativo.html")

@login_required
def RolTramite(request):
    return render (request,"Base Roles Tramites.html")

@login_required
def RolUsuario(request):
    return render (request,"Base Roles Usuarios.html")









