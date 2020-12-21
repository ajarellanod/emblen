from django.db import models
from django.contrib.auth.models import User

from apps.base.models import EmblenBaseModel


class Perfil(EmblenBaseModel):
    """
    Modelo para agregar nuevos atributos a la clase principal User de Django.
    """

    usuario = models.OneToOneField(
        User, on_delete=models.PROTECT
    )

    def __str__(self):
        return self.usuario.get_full_name()

    class Meta:
        verbose_name_plural = "Perfiles"