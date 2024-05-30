from django.shortcuts import redirect, render, HttpResponse, get_list_or_404
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from apps.Usuarios.models import Usuario
from .forms import CrearNoticiasForm,  CrearGrupoForm
from .models import Noticias
from django.contrib.auth.models import Group
from django.db.models import Count
from django.http import HttpRequest, HttpResponseRedirect
from django.utils.decorators import method_decorator
from .decorators import admin_required



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
def AtencionPoblacion(request:HttpRequest):
    if request.POST:
        email = request.user.email
        usuario = request.user.username
        municipality = request.POST['municipality']
        consulta = request.POST['consulta']
        subject = request.POST['subject']
        message = request.POST['message']
        #email
        admin_list = [i.email for i in Usuario.objects.filter(groups__name="Administración")]
        send_mail(
            recipient_list=admin_list,
            subject= subject,
            message=f"Email: {email}\nNombre del usuario: {usuario}\nMuniciopio: {municipality}\nTipo de consulta: {consulta}\nAsunto: {subject}\nMensaje: {message}",
            from_email="smtp.gmail.com",
        )
        return render (request,"Plataforma/Atención a la Poblacion.html",{'response':'correcto', 'message':'Se ha enviado correctamente'})
    return render (request,"Plataforma/Atención a la Poblacion.html")

# Administración
@login_required
@admin_required
def Administracion(request):
    context = {
        'usuarios': Usuario.objects.all()
    }
    return render (request,"Plataforma/Sitio Administrativo.html", context)

# Trámites
@login_required
@admin_required
def Tramites(request):
    return render (request,"Plataforma/Tramites.html")

# Usuarios
@login_required
@admin_required
def Usuarios(request):
    context = {
        'usuarios': Usuario.objects.all()
    }
    return render (request,"Plataforma/Usuarios.html", context)

# Eliminar Usuarios
@login_required
@admin_required
def EliminarUsuario(request,id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect("Usuarios")

# Cambiar Rol de Usuarios
@login_required
@admin_required
def CambiarRol(request, id):
    if request.method == 'POST':
        try:
            usuario = Usuario.objects.get(id=id)
        except Usuario.DoesNotExist:
            return render (request,"Plataforma/Atención a la Poblacion.html",{'response':'incorrecto', 'message':'Usuario no encontrado'})

        group_names = list(Group.objects.all().values_list('name', flat=True)) 
        selected_group = request.POST['role']

        if selected_group in group_names:
            try:
                group = Group.objects.get(name=selected_group)
            except Group.DoesNotExist:
                return render (request,"Plataforma/Atención a la Poblacion.html",{'response':'incorrecto', 'message':'Grupo no encontrado'})

            usuario.groups.clear()
            usuario.groups.add(group)
            return redirect('Usuarios')
        else:
           return render (request,"Plataforma/Atención a la Poblacion.html",{'response':'incorrecto', 'message':'Rol inválido'})
    else:
        group_names = list(Group.objects.all().values_list('name', flat=True))
        return render(request, "Plataforma/Cambiar Rol.html", {'group_names': group_names})

        
# Noticas del usuario
def NoticiasUsuario(request):
    noticias = Noticias.objects.all()
    return render(request,"Plataforma/Noticias Usuario.html", {'noticias':noticias})

# Visualizar Noticias
@login_required
@admin_required
def NoticiasView(request):
    noticias = Noticias.objects.all()
    return render(request,"Plataforma/Noticias.html", {'noticias':noticias})

# Crear Noticias
@login_required
@admin_required
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
@admin_required
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
@admin_required
def EliminarNoticia(request,id):
    noticia = Noticias.objects.get(id=id)
    noticia.delete()
    return redirect("Noticias")

# Instalar Modulos PDF
@login_required
@admin_required
def InstalarModulosPDF(request):
    return render(request,"Plataforma/Instalacion Modulo.html")

@login_required
@admin_required
def Graficos(request):
    return render(request,"Plataforma/Graficos.html")

@login_required
@admin_required
def Grupos(request):
    grupos = Group.objects.annotate(user_count=Count('user'))
    return render(request,"Plataforma/Grupos.html",{'grupos':grupos})

# Crear Grupo
@login_required
@admin_required
def CrearGrupo(request:HttpRequest):
    if request.POST:
        form = CrearGrupoForm(request.POST)
        if form.is_valid():
            nombre_grupo = form.cleaned_data['name']
            grupo, created = Group.objects.get_or_create(name=nombre_grupo)
            return redirect('Grupos')
    else:
        form = CrearGrupoForm()
    return render(request,'Plataforma/Crear Grupo.html',{'form':form})

# Editar Grupo
@login_required
@admin_required
def EditarGrupo(request, id):
    grupo = Group.objects.get(id=id)
    if request.POST:
        form = CrearGrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('Grupos')
    else:
        form = CrearGrupoForm(instance=grupo)
    return render(request,'Plataforma/Editar Grupo.html',{'form':form})

# Eliminar Grupo
@login_required
@admin_required
def EliminarGrupo(request, id):
    grupo = Group.objects.get(id=id)
    grupo.delete()
    return redirect("Grupos")