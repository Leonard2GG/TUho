from typing import Any
from django.core.management.base import BaseCommand
from usuarios.models import Usuario
from plataforma.models import ConfiguracionGeneral

from django.contrib.auth.models import Group

GRUPOS = ["Administración", "Usuario", "Supervisor","Administrador Trámites"]

class Command(BaseCommand):

    help = "Genera el estado Inicial"

    def handle(self, *args: Any, **options: Any):

        for g in GRUPOS:
            if not Group.objects.filter(name=g):
                Group.objects.create(name=g)
                print(f"{g} Creado con éxito")

        if not Usuario.objects.filter(is_superuser=True):
            try:
                usuario = Usuario()
                usuario.username = "admin"
                usuario.set_password("admin")
                usuario.is_staff = True
                usuario.is_superuser = True
                usuario.save()
                usuario.groups.add(Group.objects.get(name="Administración"))
                usuario.save()
                print("Admin creado con exito")
            except Exception as e:
                print(e)
        conf_inicial = ConfiguracionGeneral()
        conf_inicial.correo = "incial@gmail.com"
        conf_inicial.contraseña_correo = "contraseña"
        
        self.stdout.write("Completado")

