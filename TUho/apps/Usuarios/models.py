from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Usuario(AbstractUser):
    carnet = models.CharField(max_length=11);
    telefono = models.CharField(max_length = 8);
    direccion = models.TextField(max_length = 255);