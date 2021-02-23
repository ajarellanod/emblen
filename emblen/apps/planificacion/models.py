from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr
from django.db.models import Max
from django.core.exceptions import NON_FIELD_ERRORS

from apps.base.models import EmblenBaseModel

from apps.formulacion.models import (
    PartidaAccionInterna
)


class TipoModificacion(EmblenBaseModel):
    
    codigo = models.CharField(max_length=2)

    nombre = models.CharField(max_length=100)

    descripcion = models.CharField(max_length=200)

    tipo_afectacion = models.CharField(max_length=2) #A = Aumenta -- D = disminuye 

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Modificaciones"


class Modificacion(EmblenBaseModel):
    """ 
    En este modelo se deben guardar los cambios/modificaciones (afectaciones)
    que se le vayan haciendo al presupuesto
    """
    anio = models.CharField(max_length=4)

    numero = models.CharField(max_length=10)

    partida_accioninterna = models.ForeignKey(
        PartidaAccionInterna,
        related_name="documentos",
        on_delete=models.PROTECT
    )

    tipo_documento = models.ForeignKey(
        TipoModificacion,
        related_name="documentos",
        on_delete=models.PROTECT
    )

    documento_referenciado = models.IntegerField() 
    #No se coloca como FK de la tabla compromiso porque puede ser otro tipo de documento
    #Como Nota de debito ND o otro que no crean un compromiso pero tiene un codigo de referencia

    fecha = models.DateField()
    
    monto = models.DecimalField(max_digits=22,decimal_places=4)

    saldo = models.DecimalField(max_digits=22,decimal_places=4)

    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Modificaciones"


class AcumuladosPresupuestario(EmblenBaseModel):
    """ 
    En este modelo se deben guardar los Acumulados de los cambios (afectaciones)
    que se le vayan haciendo al presupuesto POR MES
    """
    
    anio = models.CharField(max_length=4)

    mes = models.CharField(max_length=2)

    partida_accioninterna = models.ForeignKey(
        PartidaAccionInterna,
        related_name="acumuladospresupuestarios",
        on_delete=models.PROTECT
    )
    
    compromiso = models.DecimalField(max_digits=22,decimal_places=4)

    causado = models.DecimalField(max_digits=22,decimal_places=4)

    pago = models.DecimalField(max_digits=22,decimal_places=4)

    aumento = models.DecimalField(max_digits=22,decimal_places=4)

    disminucion = models.DecimalField(max_digits=22,decimal_places=4)

    por_comprometer = models.DecimalField(max_digits=22,decimal_places=4)

    por_causar = models.DecimalField(max_digits=22,decimal_places=4)

    por_pagar = models.DecimalField(max_digits=22,decimal_places=4)

    monto = models.DecimalField(max_digits=22,decimal_places=4)

    saldo = models.DecimalField(max_digits=22,decimal_places=4)

    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Acumulados Presupuestario"
        unique_together = (("partida_accioninterna", "mes", "anio"),)