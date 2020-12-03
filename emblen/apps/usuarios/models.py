from django.db import models
from django.contrib.auth.models import User

from apps.base.models import TimeStampedModel

from apps.nucleo.models import Opcion


class Perfil(TimeStampedModel):
    """
    Modelo para agregar nuevos atributos a la clase principal User de Django.
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

    class Meta:
        verbose_name_plural = "Perfiles"


class Rol(models.Model):
    """
    Modelo para manejar los roles de cada usuario dentro del sistema.
    """
    
    nombre = models.CharField("Nombre", max_length=50)

    descripcion = models.CharField("Descripción", max_length=200)

    opciones = models.ManyToManyField(
        Opcion,
        related_name="roles",
        verbose_name="Opciones Disponibles",
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Roles"