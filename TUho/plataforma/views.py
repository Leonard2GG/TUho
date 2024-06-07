from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from usuarios.models import Usuario
from .forms import CrearNoticiasForm,  CrearGrupoForm
from .models import Noticias
from django.contrib.auth.models import Group
from django.db.models import Count
from django.http import HttpRequest, HttpResponseRedirect
from django.utils.decorators import method_decorator
from .decorators import admin_required, pure_admin_required
from django.core.paginator import Paginator





# Create your views here.

# Inicio
def Inicio(request):
    return render(request,"plataforma/Inicio.html")

# Mis Tramites
@login_required
def MisTramites(request):
    return render(request,"plataforma/Mis Trámites.html")

# Información Personal
@login_required
def InformacionPersonal(request):
    return render (request,"plataforma/Informacion Personal.html")

# Atencion a la Población
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
        return render (request,"plataforma/Atención a la Poblacion.html",{'response':'correcto', 'message':'Se ha enviado correctamente'})
    return render (request,"plataforma/Atención a la Poblacion.html")

# Administración
@login_required
@admin_required
def Administracion(request:HttpRequest):
    context = {
        'usuarios': Usuario.objects.all()
    }
    if request.user.groups.filter(name='Administración').exists():
        return render (request,"plataforma/Sitio Administrativo.html", context)
    elif request.user.groups.filter(name='Administrador Trámites').exists():
        return render (request,"plataforma/Sitio Administrativo.html", context)
    return render (request,"plataforma/Sitio Administrativo.html", context)

# Trámites
@login_required
@admin_required
def Tramites(request):
    return render (request,"plataforma/Tramites.html")

# Usuarios
@login_required
@pure_admin_required
def Usuarios(request):
    context = {
        'usuarios': Usuario.objects.all()
    }
    return render (request,"plataforma/Usuarios.html", context)

# Eliminar Usuarios
@login_required
@pure_admin_required
def EliminarUsuario(request,id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect("Usuarios")

# Cambiar Rol de Usuarios
@login_required
@pure_admin_required
def CambiarRol(request, id):
    if request.method == 'POST':
        try:
            usuario = Usuario.objects.get(id=id)
        except Usuario.DoesNotExist:
            return render (request,"plataforma/Atención a la Poblacion.html",{'response':'incorrecto', 'message':'Usuario no encontrado'})

        group_names = list(Group.objects.all().values_list('name', flat=True)) 
        selected_group = request.POST['role']

        if selected_group in group_names:
            try:
                group = Group.objects.get(name=selected_group)
            except Group.DoesNotExist:
                return render (request,"plataforma/Atención a la Poblacion.html",{'response':'incorrecto', 'message':'Grupo no encontrado'})

            usuario.groups.clear()
            usuario.groups.add(group)
            return redirect('Usuarios')
        else:
           return render (request,"plataforma/Atención a la Poblacion.html",{'response':'incorrecto', 'message':'Rol inválido'})
    else:
        group_names = list(Group.objects.all().values_list('name', flat=True))
        return render(request, "plataforma/Cambiar Rol.html", {'group_names': group_names})

        
# Noticas del usuario
def NoticiasUsuario(request):
    noticias = list(Noticias.objects.all().order_by("on_modified"))[::-1]
    paginator = Paginator(noticias,5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request,"plataforma/Noticias Usuario.html", {'page_obj':page_obj})

# Visualizar Noticias
@login_required
@pure_admin_required
def NoticiasView(request):
    noticias = list(Noticias.objects.all().order_by("on_modified"))[::-1]
    paginator = Paginator(noticias,5)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    print(page_obj.paginator.count)
    return render(request,"plataforma/Noticias.html", {'page_obj':page_obj})

# Crear Noticias
@login_required
@pure_admin_required
def CrearNoticia(request):
    noticia = Noticias()
    form = CrearNoticiasForm()
    if request.POST:
        noticia.titulo = request.POST["titulo"]
        noticia.cuerpo = request.POST["cuerpo"]
        noticia.save()
        return redirect('Noticias')
    return render(request,"plataforma/Crear Noticia.html",{"noticias":form})

# Editar Noticias
@login_required
@pure_admin_required
def EditarNoticia(request,id):
    noticia = Noticias.objects.get(id=id)
    if request.POST:
        noticia.titulo = request.POST["titulo"]
        noticia.cuerpo = request.POST["cuerpo"]
        noticia.save()
        return redirect('Noticias')    
    return render(request,"plataforma/Editar Noticia.html",{"noticias":noticia})

# Eliminar Noticias
@login_required
@pure_admin_required
def EliminarNoticia(request,id):
    noticia = Noticias.objects.get(id=id)
    noticia.delete()
    return redirect("Noticias")

# Instalar Modulos PDF
@login_required
@pure_admin_required
def InstalarModulosPDF(request):
    return render(request,"plataforma/Instalacion Modulo.html")

@login_required
@admin_required
def Graficos(request):
    return render(request,"plataforma/Graficos.html")

@login_required
@pure_admin_required
def Grupos(request):
    grupos = Group.objects.annotate(user_count=Count('user'))
    return render(request,"plataforma/Grupos.html",{'grupos_query':grupos})

# Crear Grupo
@login_required
@pure_admin_required
def CrearGrupo(request:HttpRequest):
    if request.POST:
        form = CrearGrupoForm(request.POST)
        if form.is_valid():
            nombre_grupo = form.cleaned_data['name']
            grupo, created = Group.objects.get_or_create(name=nombre_grupo)
            return redirect('Grupos')
    else:
        form = CrearGrupoForm()
    return render(request,'plataforma/Crear Grupo.html',{'form':form})

# Editar Grupo
@login_required
@pure_admin_required
def EditarGrupo(request, id):
    grupo = Group.objects.get(id=id)
    if request.POST:
        form = CrearGrupoForm(request.POST, instance=grupo)
        if form.is_valid():
            form.save()
            return redirect('Grupos')
    else:
        form = CrearGrupoForm(instance=grupo)
    return render(request,'plataforma/Editar Grupo.html',{'form':form})

# Eliminar Grupo
@login_required
@pure_admin_required
def EliminarGrupo(request, id):
    grupo = Group.objects.get(id=id)
    grupo.delete()
    return redirect("Grupos")