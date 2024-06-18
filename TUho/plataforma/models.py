from django.db import models
from ckeditor.fields import RichTextField
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # Obtiene la extensión del archivo
    valid_extensions = ['.jpg', '.png',]
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Archivo no soportado'))
# Create your models here.

# Modelo de Noticias
class Noticias(models.Model):
    titulo = models.CharField(max_length=255)
    imagen_cabecera = models.ImageField(upload_to=f"Noticias/{datetime.now().date().strftime('%d-%m-%Y')}/", blank=True, null=True, validators=[validate_file_extension])
    resumen = models.CharField(max_length=250, null=True, blank=True)
    cuerpo = RichTextField()
    on_create = models.DateField(auto_now_add=True)
    on_modified = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.titulo} - {self.on_create}"
    class Meta:
        verbose_name="noticia"
        verbose_name_plural="noticias"
        
class ConfiguracionGeneral(models.Model):
    correo = models.EmailField()
    contraseña_correo = models.CharField(max_length=50)
    
    