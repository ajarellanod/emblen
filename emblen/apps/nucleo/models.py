from django.db import models


class Modulo(models.Model):
    """
    Modelo donde se registra todos los modulos disponibles en el sistema.
    """

    nombre = models.CharField("Nombre", max_length=50)

    descripcion = models.CharField("Descripción", max_length=200)

    def __str__(self):
        return self.nombre


class Opcion(models.Model):
    """
    Modelo donde se registra todos las opciones de cada modulo disponibles en el sistema.
    """

    nombre = models.CharField("Nombre", max_length=200)

    modulo = models.ForeignKey(
        Modulo,
        related_name="opciones",
        on_delete=models.CASCADE,
        verbose_name="Modulo",
    )