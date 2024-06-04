from .forms import InformacionPersonal
from .models import Usuario
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, password_validation
from django.contrib.auth.models import Group
from usuarios.models import Usuario
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm, ChangePasswordForm

# Create your views here.

# Nombre de los Grupos
def group_names(group:Group):
    return group.name

# Verificar si ese usuario pertenece a ese grupo
def verify_group(usuario, group_name):
    if group_name in map(  group_names , list(usuario.groups.all())):
        return True
    else:
        return False

# Login
def Login(request:HttpRequest):
    if request.user.is_authenticated:
        return redirect("Inicio")
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        try:
            user_to_auth = Usuario.objects.get(username=username)
        except Usuario.DoesNotExist:
            return render(request, "usuarios/Login.html", {'response': 'incorrecto', 'message': 'Fallo en la autentificación'})
        user = authenticate(request, username=user_to_auth.username, password=password)
        if user is not None:
            login(request, user)
            usuario = Usuario.objects.get(id=user.id)
            if verify_group(usuario, "Administración"):
                return redirect("Administracion")
            elif verify_group(usuario, "Usuario"):
                return redirect("Inicio")
            elif verify_group(usuario, "Administrador Trámites"):
                return redirect("Administracion")
            elif verify_group(usuario, "Supervisor"):
                return redirect("Administracion")
            return redirect("Inicio")
        else:
            return render(request, "usuarios/Login.html", {'response': 'incorrecto', 'message': 'Fallo en la autentificación'})
    return render(request, "usuarios/Login.html")

# Register
def Registrar(request:HttpRequest):
    if request.POST:
        if Usuario.objects.filter(username=request.POST['username']).exists():
            return render(request, "usuarios/Registrar.html", {'response': 'incorrecto', 'messages': ['El usuario ya existe']})

        usuario = Usuario()
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password and password2 and password != password2:
            return render(request, "usuarios/Registrar.html", {'response': 'incorrecto', 'messages': ['Las contraseñas deben coincidir']})

        usuario.username = username
        usuario.email = email
        usuario.set_password(password)

        try:
            validation = password_validation.validate_password(password, usuario)
            usuario.save()
            usuario.groups.add(Group.objects.get(name="Usuario"))
            usuario.save()
            return redirect("Login")
        except Exception as e:
            mensajes = []
            for err in e:
                mensajes.append(f"{err}")
            return render(request, "usuarios/Registrar.html", {'response': 'incorrecto', 'messages': mensajes})

    return render(request, "usuarios/Registrar.html")

# Restablecer Contraseña
class RestablecerContraseña(auth_views.PasswordResetView):
    template_name = "usuarios/Restablecer Contraseña.html"
    form_class = CustomPasswordResetForm

# Cambiar Contraseña
class CambiarContraseña(auth_views.PasswordResetConfirmView):
    form_class = ChangePasswordForm
    template_name = "usuarios/Cambiar Contraseña.html"

# Confirmacion del Restablecer Contraseña  
def RestablecerContraseñaConfirmado(request):
    return render(request,"usuarios/Restablecer Contraseña Confirmado.html")

# Confirmación del Cambiar Contraseña
def CambiarContraseñaConfirmado(request):
    return render(request,"usuarios/Cambiar Contraseña Confirmado.html")

# Cerrar Sesión
@login_required
def CerrarSesion(request:HttpRequest):
    logout(request)
    return redirect("Login")


# Actualizar Información
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
    return render(request,"usuarios/Actualizar Informacion Personal.html",{"form":form})
    





