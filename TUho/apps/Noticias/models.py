from django.db import models

# Create your models here.

# Modelo de Noticias
class Noticias(models.Model):
    titulo = models.CharField(max_length=255)
    cuerpo = models.TextField()
    on_create = models.DateField(auto_now_add=True)
    on_modified = models.DateField(auto_now=True)

    class Meta:
        verbose_name="noticia"
        verbose_name_plural="noticias"