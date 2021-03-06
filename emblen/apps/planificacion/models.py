from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr
from django.db.models import Max
from django.core.exceptions import NON_FIELD_ERRORS

from apps.base.models import EmblenBaseModel

from apps.formulacion.models import PartidaAccionInterna


class TipoModificacion(EmblenBaseModel):
    
    DISMINUCION = 'D'
    AUMENTO = 'A'
    
    TIPO_AFECTACION = (
        (DISMINUCION, 'Disminucion'),
        (AUMENTO, 'Aumento'),
    )
    
    codigo = models.CharField(max_length=2)

    nombre = models.CharField(max_length=100)

    descripcion = models.CharField(max_length=200)
    
    afectacion = models.CharField(max_length=1, choices=TIPO_AFECTACION)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Modificaciones"


class Modificacion(EmblenBaseModel):
    """ 
    En este modelo se deben guardar los afectaciones
    que se le vayan haciendo al presupuesto
    """
    anio = models.CharField(max_length=4)

    numero = models.IntegerField()

    partida_accioninterna = models.ForeignKey(
        PartidaAccionInterna,
        related_name="modificaciones",
        on_delete=models.PROTECT
    )

    tipo_modificacion = models.ForeignKey(
        TipoModificacion,
        related_name="modificaciones",
        on_delete=models.PROTECT
    )

    documento_referenciado = models.IntegerField(null=True, blank=True) 
    
    monto = models.DecimalField(max_digits=22,decimal_places=2)

    saldo = models.DecimalField(max_digits=22,decimal_places=2, null=True, blank=True)

    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.numero

    def _next_num(self):
        result = Modificacion.objects.all().aggregate(Max('numero'))
        result = result["numero__max"]

        if result is not None:
            return result + 1
        return 1

    def gen_rest_attrs(self):
        self.saldo = self.monto
        self.numero = self._next_num()

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
    
    class Meta:
        verbose_name_plural = "Acumulados Presupuestario"
        unique_together = (("partida_accioninterna", "mes", "anio"),)

