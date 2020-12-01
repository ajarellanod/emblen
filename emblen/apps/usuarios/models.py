from django.db import models
from django.contrib.auth.models import User

from apps.base.models import TimeStampedModel

from apps.nucleo.models import Modulo


class Perfil(TimeStampedModel):
    """
    Clase para agregar nuevos atributos a la clase principal User de Django.
    """

    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE
    )

    roles = models.ManyToManyField(
        "Rol",
        related_name="perfiles",
        verbose_name="Roles de Usuario",
    )

    def __str__(self):
        return self.usuario.username


class Rol(models.Model):
    """
    Clase para manejar los roles de cada usuario dentro del sistema.
    """
    
    nombre = models.CharField("Nombre", max_length=50)

    descripcion = models.CharField("Descripción", max_length=200)

    modulo = models.ForeignKey(
        Modulo,
        related_name="roles",
        on_delete=models.CASCADE,
        verbose_name="Modulos",
    )

    def __str__(self):
        return self.nombre