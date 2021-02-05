from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr
from django.db.models import Max

from apps.base.models import EmblenBaseModel
from django.core.exceptions import NON_FIELD_ERRORS

from apps.formulacion.models import (
    Programa,
    Partida,
    Parroquia,
    PartidaAccionInterna
)

from apps.compras.models import (
    Beneficiario
)


class TiposDocumento(EmblenBaseModel):
    
    codigo = models.CharField(max_length=2)

    nombre = models.CharField(max_length=100)

    descripcion = models.CharField(max_length=200)

    tipo_afectacion = models.CharField(max_length=2) #A = Aumenta -- D = disminuye 

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Documentos"


class Documento(EmblenBaseModel):

    anio = models.CharField(max_length=4)

    numero = models.CharField(max_length=10)

    partida_accioninterna = models.ForeignKey(
        PartidaAccionInterna,
        related_name="documentos",
        on_delete=models.PROTECT
    )

    tipo_documento = models.ForeignKey(
        TiposDocumento,
        related_name="documentos",
        on_delete=models.PROTECT
    )

    fecha = models.DateField()

    beneficiario = models.ForeignKey(
        Beneficiario,
        related_name="documentos",
        on_delete=models.PROTECT
    )

    monto = models.DecimalField(max_digits=22,decimal_places=4)

    saldo = models.DecimalField(max_digits=22,decimal_places=4)

    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Documentos"


class AcumuladosPresupuestario(EmblenBaseModel):
    """ 
    En este modelo se deben guardar los acumulados de los cambios
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