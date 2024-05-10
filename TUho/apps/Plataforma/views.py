from django.shortcuts import redirect, render, HttpResponse, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from apps.Usuarios.models import Usuario
from .forms import CrearNoticiasForm
from apps.Plataforma.models import Noticias
from django.contrib.auth.models import Group
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

# Inicio
def Inicio(request):
    return render(request,"Plataforma/Inicio.html")

# Mis Tramites
@login_required
def MisTramites(request):
    return render(request,"Plataforma/Mis Trámites.html")

# Información Personal
@login_required
def InformacionPersonal(request):
    return render (request,"Plataforma/Informacion Personal.html")

# Atencion a la Población
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

# Administración
@login_required
def Administracion(request):
    context = {
        'usuarios': Usuario.objects.all()
    }
    return render (request,"Plataforma/Sitio Administrativo.html", context)

# Trámites
@login_required
def Tramites(request):
    return render (request,"Plataforma/Tramites.html")

# Usuarios
@login_required
def Usuarios(request):
    context = {
        'usuarios': Usuario.objects.all()
    }
    return render (request,"Plataforma/Usuarios.html", context)

# Eliminar Usuarios
@login_required
def EliminarUsuario(request,id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect("Usuarios")

# Cambiar Rol de Usuarios
@login_required
def CambiarRol(request, id):
    if request.method == 'POST':  
        usuario = Usuario.objects.get(id=id)
        group_names =['Administración','Supervisor', 'Usuario']
        selected_group = request.POST['role']
        if selected_group in group_names:
            group = Group.objects.get(name=selected_group)
            usuario.groups.clear()
            usuario.groups.add(group)
            return redirect('Usuarios')
    return render(request,"Plataforma/Cambiar Rol.html")
        
# Noticas del usuario
def NoticiasUsuario(request):
    noticias = Noticias.objects.all()
    return render(request,"Plataforma/Noticias Usuario.html", {'noticias':noticias})

# Visualizar Noticias
@login_required
def NoticiasView(request):
    noticias = Noticias.objects.all()
    return render(request,"Plataforma/Noticias.html", {'noticias':noticias})

# Crear Noticias
@login_required
def CrearNoticia(request):
    noticia = Noticias()
    form = CrearNoticiasForm()
    if request.POST:
        noticia.titulo = request.POST["titulo"]
        noticia.cuerpo = request.POST["cuerpo"]
        noticia.save()
        return redirect('Noticias')
    return render(request,"Plataforma/Crear Noticia.html",{"noticias":form})

# Editar Noticias
@login_required
def EditarNoticia(request,id):
    noticia = Noticias.objects.get(id=id)
    if request.POST:
        noticia.titulo = request.POST["titulo"]
        noticia.cuerpo = request.POST["cuerpo"]
        noticia.save()
        return redirect('Noticias')    
    return render(request,"Plataforma/Editar Noticia.html",{"noticias":noticia})

# Eliminar Noticias
@login_required
def EliminarNoticia(request,id):
    noticia = Noticias.objects.get(id=id)
    noticia.delete()
    return redirect("Noticias")

# Instalación de Módulos
@login_required
def InstalarModulos(request):
    return render(request,"Plataforma/Instalacion de Modulos.html")





