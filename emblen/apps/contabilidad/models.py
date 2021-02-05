from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr
from django.db.models import Max

from apps.base.models import EmblenBaseModel
from django.core.exceptions import NON_FIELD_ERRORS


class Comprobante(EmblenBaseModel):
    """ se guardarán todos los Comprobantes - es como una tabla resumen con comprobante y monto por mes"""
    mes = models.CharField(max_length=2)

    anio = models.CharField(max_length=4)
    
    codigo = models.IntegerField() # correlativos - unico por mes y año 

    descripcion = models.CharField(max_length=100)

    fecha = models.DateField()

    monto = models.DecimalField(max_digits=22,decimal_places=4)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Comprobantes"
        unique_together = (("mes", "anio", "codigo"),)