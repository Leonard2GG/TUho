from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout, password_validation
from django.contrib.auth.models import Group
from apps.Usuarios.models import Usuario
from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import CustomPasswordResetForm, ChangePasswordForm

# Create your views here.

def group_names(group:Group):
    return group.name

def verify_group(usuario, group_name):
    if group_name in map(  group_names , list(usuario.groups.all())):
        return True
    else:
        return False

def Login(request:HttpRequest):
    if request.user.is_authenticated:
        return redirect("Inicio")
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user_to_auth = Usuario.objects.get(username=username)
        user = authenticate(request, username=user_to_auth.username, password=password)
        if user is not None:
            login(request, user)
            usuario = Usuario.objects.get(id=user.id)
            if verify_group(usuario, "Administración"):
                return redirect("Administracion")
            elif verify_group(usuario, "Usuario"):
                return redirect("Inicio")
            elif verify_group(usuario, "Supervisor"):
                return redirect("Administracion")
            return redirect("Inicio")

        else:
            return render(request,"Autenticacion/Login.html",{'response':'incorrecto', 'message':'Fallo en la autentificación'})
    return render (request,"Autenticacion/Login.html")

def Registrar(request:HttpRequest):
    if request.POST:
        usuario = Usuario()
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']
        if password and password2 and password != password2:
            return render(request,"Autenticacion/Registrar.html",{'response':'incorrecto', 'messages':['Las contraseñas deben coincidir']})

        usuario.username = username
        usuario.email = email
        usuario.set_password(password)
        
        try:
            validation = password_validation.validate_password(password, usuario)
            usuario.save()
            usuario.groups.add(Group.objects.get(name = "Usuario"))
            usuario.save()
            return redirect("Login")
        except Exception as e:
            mensajes = []
            for err in e:
                mensajes.append(f"{err}")
            return render(request,"Autenticacion/Registrar.html",{'response':'incorrecto', 'messages':mensajes})
           
    return render (request,"Autenticacion/Registrar.html")

class RestablecerContraseña(auth_views.PasswordResetView):
    template_name = "Autenticacion/Restablecer Contraseña.html"
    form_class = CustomPasswordResetForm

class CambiarContraseña(auth_views.PasswordResetConfirmView):
    form_class = ChangePasswordForm
    template_name = "Autenticacion/Cambiar Contraseña.html"
   
def RestablecerContraseñaConfirmado(request):
    return render(request,"Autenticacion/Restablecer Contraseña Confirmado.html")

def CambiarContraseñaConfirmado(request):
    return render(request,"Autenticacion/Cambiar Contraseña Confirmado.html")

@login_required
def CerrarSesion(request:HttpRequest):
    logout(request)
    return redirect("Login")
