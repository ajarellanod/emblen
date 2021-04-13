from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr
from django.db.models import Max
from django.core.exceptions import NON_FIELD_ERRORS

from apps.base.models import EmblenBaseModel

from apps.formulacion.models import PartidaAccionInterna, IngresoPresupuestario

from apps.nucleo.models import MovimientoGasto


class TipoModificacion(EmblenBaseModel):
    
    DISMINUCION = 'D'
    AUMENTO = 'A'
    TRASPASO = 'T'
    
    TIPO_AFECTACION = (
        (DISMINUCION, 'Disminucion'),
        (AUMENTO, 'Aumento'),
        (TRASPASO, 'Traspaso'),
    )

    INGRESOS = 'I'
    GASTOS = 'G'

    TIPO_MODIFICACION = (
        (INGRESOS, 'Ingresos'),
        (GASTOS, 'Gastos'),
    )

    codigo = models.CharField(max_length=2)

    nombre = models.CharField(max_length=100)

    descripcion = models.CharField(max_length=200)
    
    afectacion = models.CharField(max_length=1, choices=TIPO_AFECTACION)
    
    tipo_modificacion = models.CharField(max_length=1, choices=TIPO_MODIFICACION)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Modificaciones"


class ModificacionIngreso(EmblenBaseModel):

    GACETA = 0
    ACTA = 1

    TIPO_DOCUMENTO = (
        (GACETA, "Gaceta"),
        (ACTA, "Acta"),
    ) #Acta de Junta Directiva

    ELABORADO = 0
    VERIFICADO = 1
    ANULADO = 2
    REVERSADO = 3

    ESTATUS_INGRESO = (
        (ELABORADO, "Elaborado"),
        (VERIFICADO, "Verificado"),
        (ANULADO, "Anulado"),  
        (REVERSADO, "Reversado"),  
    )

    anio = models.CharField(max_length=4)
    
    fecha = models.DateField()
    
    periodo = models.CharField(max_length=2)

    numero = models.IntegerField()

    tipo_modificacion = models.ForeignKey(
        TipoModificacion,
        related_name="modificaciones_ingresos",
        on_delete=models.PROTECT,
        null=True
    )

    tipo_documento = models.IntegerField(
        "Tipo de Documento del Ingreso", 
        choices=TIPO_DOCUMENTO,
    )

    numero_documento = models.CharField(max_length=10)

    fecha_documento = models.DateField()

    numero_decreto = models.CharField(max_length=10, null=True) #Si es una acta no lleva decreto

    descripcion = models.TextField(max_length=300)

    monto = models.DecimalField(max_digits=22,decimal_places=2)

    ingreso_presupuestario = models.ForeignKey(
        IngresoPresupuestario,
        related_name="modificaciones_ingresos",
        on_delete=models.PROTECT
    )

    estatus = models.IntegerField(
        "Estatus Modificacón de Ingreso", 
        choices=ESTATUS_INGRESO,
        default=ELABORADO
    )

    elaborador = models.ForeignKey(
        User,
        related_name="e_modificaciones_ingresos",
        on_delete=models.PROTECT,
        null=True
    )

    verificador = models.ForeignKey(
        User,
        related_name="v_modificaciones_ingresos",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    anulador = models.ForeignKey(
        User,
        related_name="a_modificaciones_ingresos",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    ) 

    reversor = models.ForeignKey(
        User,
        related_name="r_modificaciones_ingresos",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    ) 

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Modificaciones de Ingresos"


class ModificacionGasto(EmblenBaseModel):
    """ 
    En este modelo se deben guardar los afectaciones
    que se le vayan haciendo al presupuesto
    """
    ELABORADA = 0
    VERIFICADA = 1
    ANULADA = 2
    REVERSADA = 3

    ESTATUS_GASTO = (
        (ELABORADA, "Elaborada"),
        (VERIFICADA, "Verificada"),
        (ANULADA, "Anulada"), 
        (REVERSADA, "Reversada"), 
    )

    fecha = models.DateField()

    numero = models.IntegerField()

    tipo_modificacion = models.ForeignKey(
        TipoModificacion,
        related_name="modificaciones_gastos",
        on_delete=models.PROTECT
    )

    modificacion_ingreso = models.ForeignKey(
        ModificacionIngreso,
        related_name="modificaciones_gastos",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    movimiento_gasto = models.ForeignKey(
        MovimientoGasto,
        related_name="modificaciones_gastos",
        on_delete=models.PROTECT
    )

    descripcion = models.CharField(max_length=300)

    estatus = models.IntegerField(
        "Estatus Modificación de Gasto", 
        choices=ESTATUS_GASTO,
        default=ELABORADA
    )

    elaborador = models.ForeignKey(
        User,
        related_name="e_modificaciones_gastos",
        on_delete=models.PROTECT,
        null=True
    )

    verificador = models.ForeignKey(
        User,
        related_name="v_modificaciones_gastos",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    anulador = models.ForeignKey(
        User,
        related_name="a_modificaciones_gastos",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    ) 

    reversor = models.ForeignKey(
        User,
        related_name="r_modificaciones_gastos",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    ) 

    def __str__(self):
        return self.numero

    def _next_num(self):
        result = ModificacionGasto.objects.all().aggregate(Max('numero'))
        result = result["numero__max"]

        if result is not None:
            return result + 1
        return 1

    def gen_rest_attrs(self):
        self.saldo = self.monto
        self.numero = self._next_num()

    def afecta_partida(self):
        pai = self.partida_accioninterna
        tm = self.tipo_modificacion

        if tm.afectacion == tm.AUMENTO:
            pai.mto_actualizado += self.monto
        else:
            pai.mto_actualizado -= self.monto

        pai.save()

    class Meta:
        verbose_name_plural = "Modificaciones de Gastos"


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

