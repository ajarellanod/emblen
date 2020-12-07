from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from apps.base.models import TimeStampedModel
from django.core.exceptions import NON_FIELD_ERRORS

class Partida(TimeStampedModel):
    """ Almanecena las partidas presupuestarias de Recursos y Egresos """
    
    cuenta = models.CharField(max_length=14,unique=True)

    descripcion = models.TextField()

    nivel = models.IntegerField()

    saldo = models.DecimalField(max_digits=22,decimal_places=4,null=True)

    estatus = models.BooleanField(default=True)


    class Meta:
        ordering = ('-creado',)


    def __str__(self):
        return self.descripcion