from django.conf import settings
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.core.mail import send_mail
from usuarios.models import Usuario
from usuarios.forms import InformacionPersonalForm
from atencion_poblacion.models import AtencionPoblacion
from .forms import CrearNoticiasForm, ConfiguracionEmail
from .models import Noticias, ConfiguracionGeneral
from django.contrib.auth.models import Group, Permission
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

# Administración
@login_required
@admin_required
def Administracion(request:HttpRequest):
    context = {
        'usuarios': Usuario.objects.all(),
        'APoblacion': AtencionPoblacion.objects.all(),
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
    APoblacion = AtencionPoblacion.objects.all()
    return render (request,"plataforma/Tramites.html",{"APoblacion":APoblacion})

@login_required
@admin_required
def EliminarTramite(request,id):
    aPoblacion = AtencionPoblacion.objects.get(id=id)
    aPoblacion.delete()
    return redirect("Tramites")


# Usuarios
@login_required
@pure_admin_required
def Usuarios(request):
    context = {
        'usuarios': Usuario.objects.all()
    }
    return render (request,"plataforma/Usuarios.html", context)

@login_required
@pure_admin_required
def InformacionUsuario(request,id):
    usuario = Usuario.objects.get(id=id)
    if request.POST:
        form = InformacionPersonal(request.POST,instance=usuario)
        usuario.first_name = request.POST['first_name']
        usuario.last_name = request.POST['last_name']
        usuario.carnet = request.POST['carnet']
        usuario.email = request.POST['email']
        usuario.telefono = request.POST['telefono']
        usuario.direccion = request.POST['direccion']
        usuario.save()
        return redirect("Usuarios")
    form = InformacionPersonalForm(instance=usuario)
    return render(request,"plataforma/Informacion Usuario.html",{"form":form})

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
    return render(request,"plataforma/Noticias.html", {'page_obj':page_obj})

# Visualizar Noticia Admin
def VisualizarNoticiasAdmin(request,id):
    noticia = Noticias.objects.get(id=id)
    return render(request,"plataforma/Visualizar NoticiaA.html", {'noticia':noticia})

# Visualizar Noticia Admin
def VisualizarNoticiasUsuario(request,id):
    noticia = Noticias.objects.get(id=id)
    return render(request,"plataforma/Visualizar NoticiaU.html", {'noticia':noticia})

# Crear Noticias
@login_required
@pure_admin_required
def CrearNoticia(request):
    form = CrearNoticiasForm()
    if request.POST:
        noticia = Noticias()
        noticia.titulo = request.POST["titulo"]
        noticia.imagen_cabecera = request.FILES["imagen_cabecera"]
        noticia.resumen = request.POST["resumen"]
        noticia.cuerpo = request.POST["cuerpo"]
        noticia.save()
        return redirect('Noticias')
    return render(request,"plataforma/Crear Noticia.html",{"form":form})

# Editar Noticias
@login_required
@pure_admin_required
def EditarNoticia(request,id):
    noticia = Noticias.objects.get(id=id)
    if request.POST:
        noticia.titulo = request.POST["titulo"]
        noticia.imagen_cabecera = request.FILES["imagen_cabecera"]
        noticia.resumen = request.POST["resumen"]
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
@pure_admin_required
def Grupos(request):
    grupos = Group.objects.annotate(user_count=Count('user'))
    return render(request,"plataforma/Grupos.html",{'grupos_query':grupos})

# Crear Grupo
@login_required
@pure_admin_required
def CrearGrupo(request:HttpRequest):
    if request.POST:
        nombre_grupo = request.POST['nombre_grupo']
        grupo = Group()
        grupo.name=nombre_grupo
        grupo.save()
        permisos_seleccioandos = request.POST.getlist('permisos[]')
        for permiso_id in permisos_seleccioandos:
            permiso = Permission.objects.get(id=permiso_id)
            grupo.permissions.add(permiso)
        grupo.save()
        return redirect ('Grupos')
    else:
        permisos = Permission.objects.all()
        context = {'permisos':permisos}
        return render(request,'plataforma/Crear Grupo.html', context)

# Editar Grupo
@login_required
@pure_admin_required
def EditarGrupo(request, id):
    grupo = Group.objects.get(id=id)
    permisos = Permission.objects.all()
    permisos_list = []
    for i in permisos:
        if i in grupo.permissions.all():
            permisos_list.append([True,i])
        else:
            permisos_list.append([False,i])
    if request.POST:
        grupo.name = request.POST['nombre_grupo']
        permisos_seleccioandos = request.POST.getlist('permisos[]')
        grupo.permissions.clear()
        for permiso_id in permisos_seleccioandos:
            permiso = Permission.objects.get(id=permiso_id)
            grupo.permissions.add(permiso)
        grupo.save()
        return redirect ('Grupos')
        
    else:
        
        context = {
            'permisos':permisos_list,
            'grupo': grupo,
            }
        return render(request,'plataforma/Editar Grupo.html', context)

# Eliminar Grupo
@login_required
@pure_admin_required
def EliminarGrupo(request, id):
    grupo = Group.objects.get(id=id)
    grupo.delete()
    return redirect("Grupos")

def ConfiguracionCorreo(request):
    if request.POST():
        conf_global = ConfiguracionGeneral.objects.all().first()
        conf_global.correo = request.POST["correo"]
        conf_global.contraseña_correo = request.POST["contraseña_correo"]
        conf_global.save()
        settings.configure(
                EMAIL_HOST_USER = conf_global.correo,
                EMAIL_HOST_PASSWORD = conf_global.contraseña_correo,  
            ) 
        return redirect("Administracion")
    form = ConfiguracionEmail()
    return render(request, "Cambio de Email_settings.html", {"form":form})