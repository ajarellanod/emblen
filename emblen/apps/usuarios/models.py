from django.db import models
from django.contrib.auth.models import User

from apps.base.models import TimeStampedModel


class Perfil(TimeStampedModel):
    """
    Modelo para agregar nuevos atributos a la clase principal User de Django.
    """

    usuario = models.OneToOneField(
        User, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.usuario.get_full_name()

    class Meta:
        verbose_name_plural = "Perfiles"