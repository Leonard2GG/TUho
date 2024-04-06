from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from .forms import CrearNoticiasForm
from .models import Noticias


# Create your views here.
@login_required
def NoticiasView(request):
    noticias = Noticias.objects.all()
    return render(request,"Noticias/Noticias.html", {'noticias':noticias})

@login_required
def CrearNoticia(request):
    noticia = Noticias()
    form = CrearNoticiasForm()
    if request.POST:
        noticia.titulo = request.POST["titulo"]
        noticia.cuerpo = request.POST["cuerpo"]
        noticia.save()
        return redirect('Noticias')
    return render(request,"Noticias/Crear Noticia.html",{"noticias":form})

@login_required
def EditarNoticia(request,id):
    noticia = Noticias.objects.get(id=id)
    if request.POST:
        noticia.titulo = request.POST["titulo"]
        noticia.cuerpo = request.POST["cuerpo"]
        noticia.save()
        return redirect('Noticias')
        
    return render(request,"Noticias/Editar Noticia.html",{"noticias":noticia})

@login_required
def EliminarNoticia(request,id):
    noticia = Noticias.objects.get(id=id)
    noticia.delete()
    return redirect("Noticias")

