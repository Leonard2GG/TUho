from django.db import models
from usuarios.models import Usuario
from datetime import datetime
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from .choices import consulta_choice, municipality_choice

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # Obtiene la extensión del archivo
    valid_extensions = ['.pdf', '.doc', '.docx', '.jpg', '.png', '.xlsx']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Archivo no soportado'))

# Create your models here.
class AtencionPoblacion(models.Model):
    nombre = models.CharField(max_length=250);
    apellidos = models.CharField(max_length=250);
    email = models.EmailField();
    carnet = models.CharField(max_length=11);
    telefono = models.CharField(max_length = 8);
    direccion = models.CharField(max_length = 250);
    municipality = models.CharField(max_length=250, choices=municipality_choice)
    consulta = models.CharField(max_length=250, choices=consulta_choice)
    adjunto = models.FileField(upload_to=f"AtencionPoblacion/{datetime.now().date().strftime('%d-%m-%Y')}/", blank=True, null=True, validators=[validate_file_extension])
    asunto = models.CharField(max_length=250);
    mensaje = models.TextField()
    on_create = models.DateField(auto_now_add=True)
    on_modified = models.DateField(auto_now=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.nombre}{self.apellidos} - {self.asunto} - {self.on_create}"
    
    class Meta:
        verbose_name="atención a la población"
        verbose_name_plural="atención a la población"
