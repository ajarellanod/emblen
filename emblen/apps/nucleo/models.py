from django.db import models

from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr
from django.db.models import Max

from apps.base.models import EmblenBaseModel
from django.core.exceptions import NON_FIELD_ERRORS


class Publicacion(EmblenBaseModel):
    """ 
    Almanecena las Publicaciones de Ley
    """
    codigo = models.IntegerField()

    descripcion = models.CharField(max_length=100)

    anio = models.CharField(max_length=4)

    class Meta:
        verbose_name_plural = "Publicaciones"

    def __str__(self):
        return str(self.codigo)


class MovimientoGasto(EmblenBaseModel):
    """ se guardarán los Todos las modificaciones, compromisos, imputaciones y 
    afectaciones que se le hagan a las partidas de GASTOS (4) """

    MODIFICACION = 1    #planificacion.ModificacionGasto
    CONTRATO = 2        #compras.ContratoPartida
    ORDENPAGO = 3       #ejecucion.OrdenPago
    COMPROMISO = 4      #compras.Orden

    TIPO_MOVIMIENTO = (
        (MODIFICACION, "Modificacion"),
        (CONTRATO, "Contrato"),
        (ORDENPAGO, "Ordenpago"),
        (COMPROMISO, "Compromiso")
    )

    anio = models.CharField(max_length=4) #AÑO EN EJERCICIO

    periodo = models.CharField(max_length=2) #periodo

    partida = models.ForeignKey(
        "formulacion.PartidaAccionInterna",
        related_name="movimientos_gastos",
        on_delete=models.PROTECT
    )
    
    tipo_movimiento = models.IntegerField(
        choices=TIPO_MOVIMIENTO
    )

    monto = models.DecimalField(max_digits=22,decimal_places=4)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Movimientos de Gastos"
