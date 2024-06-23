import uuid
from django.http import HttpRequest
from django.shortcuts import render, redirect
from usuarios.models import Usuario
from django.core.mail import send_mail, EmailMessage
from .models import AtencionPoblacion
from .forms import AtencionPoblacionForm
from plataforma.decorators import pure_admin_required
from django.contrib.auth.decorators import login_required
from django.contrib import messages
@login_required
@pure_admin_required

# Create your views here.
# Atencion a la Población
def AtencionPoblacionView(request:HttpRequest):
    form = AtencionPoblacionForm()
    if request.POST:
        try:
            atencionP = AtencionPoblacion()
            atencionP.usuario = request.user
            atencionP.nombre = request.POST["nombre"]
            atencionP.apellidos = request.POST["apellidos"]
            atencionP.email = request.POST["email"]
            atencionP.carnet = request.POST["carnet"]
            atencionP.telefono = request.POST["telefono"]
            atencionP.direccion = request.POST["direccion"]
            atencionP.municipality = request.POST['municipality']
            atencionP.consulta = request.POST['consulta']
            if request.FILES:
                atencionP.adjunto = request.FILES['adjunto']
            atencionP.asunto = request.POST['asunto']
            atencionP.mensaje = request.POST['mensaje']
            atencionP.token = str(uuid.uuid4())
            
            #email
            admin_list = [i.email for i in Usuario.objects.filter(groups__name="Administración")]
            mail = EmailMessage(
                atencionP.asunto, 
                f"Email: { atencionP.email}\nNombre del usuario: { atencionP.usuario}\nNombre del solicitante: { atencionP.nombre}\nApellidos del solicitante: { atencionP.apellidos}\nCarnet: { atencionP.carnet}\nTeléfono: { atencionP.telefono}\nDirección: { atencionP.direccion}\nMunicipio: {atencionP.municipality}\nTipo de consulta: {atencionP.consulta}\nAsunto: {atencionP.asunto}\nMensaje: {atencionP.mensaje}",
                "smtp.gmail.com",
                admin_list
            )
            if request.FILES:
                mail.attach(atencionP.adjunto.name, atencionP.adjunto.read(), request.FILES['adjunto'].content_type)

            mail.send()

            atencionP.save()
            return render(request, "AtencionPoblacion/Atención a la Poblacion.html", {'response': 'correcto', 'message': 'Se ha enviado su solicitud correctamente', 'form': form})
        except Exception as e:
            form_persist = AtencionPoblacionForm(request.POST)
            messages.error(request, "Algo salió mal con el envio del correo, por favor intentelo de nuevo")
            print(e)
            return render(request, "AtencionPoblacion/Atención a la Poblacion.html", {'form': form_persist})
    return render(request, "AtencionPoblacion/Atención a la Poblacion.html", {'form': form})

@login_required
@pure_admin_required
def VisualizarAtencionPoblacion(request, id):
    aPoblacion = AtencionPoblacion.objects.get(id=id)
    return render(request,'AtencionPoblacion/Visualizar Atención a la Poblacion.html',{'form':aPoblacion})