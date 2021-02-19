from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr
from django.db.models import Max

from apps.base.models import EmblenBaseModel
from django.core.exceptions import NON_FIELD_ERRORS

from apps.formulacion.models import (
    Publicacion
)

class CuentaContable(EmblenBaseModel):
    """ 
    Almanecena las partidas presupuestarias de Recursos y Egresos.
    """
    
    NIVELES = {
        1: 1,
        2: 3,
        3: 5,
        4: 7,
        5: 9,
        6: 12
    }
    
    cuenta = models.CharField(max_length=12,unique=True)

    descripcion = models.TextField(max_length=100)

    nivel = models.IntegerField()

    saldo = models.DecimalField(
        max_digits=22,
        decimal_places=2,
        null=True,
        blank=True
    )

    publicacion = models.ForeignKey(
        Publicacion,
        related_name="cuentas_contables",
        on_delete=models.PROTECT
    )

    def sin_ceros(self):
        """Retorna la cuenta sin ceros a la derecha"""
        return self.cuenta[0:self.NIVELES[self.nivel]]

    def siguientes(self):
        """Devuelve queryset de las partidas hijas del nivel siguiente"""
        
        debe_comenzar = self.sin_ceros() 
        siguiente_nivel = self.nivel + 1

        queryset = CuentaContable.objects.filter(
            nivel=siguiente_nivel,
            cuenta__startswith=debe_comenzar,
        )

        return queryset
        
    class Meta:
        ordering = ('-creado',)
        verbose_name_plural = "Cuentas Contables"

    def __str__(self):
        return self.cuenta


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