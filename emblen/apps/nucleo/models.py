from django.db import models


class Modulo(models.Model):
    """
    Clase donde se registraran todos los modulos disponibles en el sistema.
    """

    nombre = models.CharField("Nombre", max_length=50)

    descripcion = models.CharField("Descripción", max_length=200)

    def __str__(self):
        return self.nombre