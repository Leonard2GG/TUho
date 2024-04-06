from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from apps.Usuarios.models import Usuario
from apps.Noticias.models import Noticias

# Create your views here.


def Inicio(request):
    return render(request,"Plataforma/Inicio.html")

@login_required
def MisTramites(request):
    return render(request,"Plataforma/Mis Trámites.html")

@login_required
def InformacionPersonal(request):
    return render (request,"Plataforma/Informacion Personal.html")

@login_required
def AtencionPoblacion(request):
    if request.POST:
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
            from_email="smtp.gmail.com",
            recipient_list= ["kiri05062001@gmail.com"]
        )
        return render (request,"Plataforma/Atención a la Poblacion.html",{'response':'correcto', 'message':'Se ha enviado correctamente'})
    return render (request,"Plataforma/Atención a la Poblacion.html")

@login_required
def Administracion(request):
    context = {
        'usuarios': Usuario.objects.all()
    }
    return render (request,"Plataforma/Sitio Administrativo.html", context)

@login_required
def Tramites(request):
    return render (request,"Plataforma/Tramites.html")

@login_required
def Usuarios(request):
    context = {
        'usuarios': Usuario.objects.all()
    }
    return render (request,"Plataforma/Usuarios.html", context)


def NoticiasUsuario(request):
    noticias = Noticias.objects.all()
    return render(request,"Plataforma/Noticias Usuario.html", {'noticias':noticias})






