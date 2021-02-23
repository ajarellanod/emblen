from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr
from django.db.models import Max

from apps.base.models import EmblenBaseModel
from django.core.exceptions import NON_FIELD_ERRORS

from apps.formulacion.models import (
    Publicacion,
    PartidaAccionInterna
)

from apps.ejecucion.models import (
    OrdenPago
)

# from apps.tesoreria.models import (
#     Pago
# )


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
    periodo = models.CharField(max_length=2)

    anio = models.CharField(max_length=4)
    
    codigo = models.IntegerField() # correlativos - unico por periodo y año 

    descripcion = models.CharField(max_length=100)

    fecha = models.DateField()

    monto = models.DecimalField(max_digits=22,decimal_places=4) #Monto total de lo que sea ya se orden de pago o ingresos

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Comprobantes"
        unique_together = (("periodo", "anio", "codigo"),)


class AsientoContable(EmblenBaseModel):
    """  Aquí va todo lo de la orden, partida a las cuales afecte (comienzan por 4)
    cuentas contables (comienzan con 2) del beneficiario que va a recibir (que es la contraparte de la partidas de gasto)
     y las deducciones (que son las contrapartes de partida de gasto de Impuesto al valor agregado)"""

    DEBITO = 'D'
    CREDITO = 'C'

    TIPO_AFECTACION = (
        (DEBITO, "Débito"),
        (CREDITO, "Crédito")
    )

    orden_pago = models.ForeignKey(
        OrdenPago,
        related_name="asientos_contables",
        on_delete=models.PROTECT
    )

    cuenta_contable = models.ForeignKey(
        CuentaContable,
        related_name="asientos_contables",
        on_delete=models.PROTECT
    )

    partida = models.ForeignKey(
        PartidaAccionInterna,
        related_name="asientos_contables",
        on_delete=models.PROTECT
    )

    #cuenta contable de las DEDUCCIONES Solamente las que inician con *2* 
    # Partidas de Gastos 4 o Contables 2
    #Las 4 vienen de la formulación del año en ejecución -> PartidaAccionInterna
    #Allí usaremos la vista de mostrar Centro de Costo -> Acc Específicas -> Partidas de PartidaAccionInterna
    #Y obtener también montos que se tienen disponibles **
    #Contemplando también que solo tomaremos de la formulacion las partidas de gasto
    #Y las contables 2, para lo que vayan a pagar - ejemplo las retenciones, el codigo del beneficiario

    tipo_afectacion = models.CharField(
        max_length=1,
        choices=TIPO_AFECTACION,
        default=DEBITO
    ) # D = Debido o C = Credito

    monto = models.DecimalField(max_digits=22,decimal_places=4) #Monto por la partida o cuenta
    
    saldo = models.DecimalField(max_digits=22,decimal_places=4) #Monto pendiente por pagar de la deducción
    #el saldo queda en 0 posteriormente que en Tesorería realizan el pago

    # pago = models.ForeignKey(
    #     Pago,
    #     related_name="asientos_contables",
    #     on_delete=models.PROTECT,
    #     null=True
    # )# Id del pago

    fecha = models.DateField()

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Asientos Contables"