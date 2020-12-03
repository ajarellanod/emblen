from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from apps.base.models import TimeStampedModel

class Partida(TimeStampedModel):
    """ Almanecena las partidas presupuestarias de Recursos y Egresos """
    
    cuenta = models.CharField(max_length=14)

    descripcion = models.TextField()

    nivel = models.IntegerField()

    saldo = models.DecimalField(max_digits=22,decimal_places=4)

    estatus = models.BooleanField()

    class Meta:
        ordering = ('-creado',)

    def __str__(self):
        return self.descripcion