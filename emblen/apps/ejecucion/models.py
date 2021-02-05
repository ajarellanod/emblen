from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr
from django.db.models import Max

from apps.base.models import EmblenBaseModel
from django.core.exceptions import NON_FIELD_ERRORS


from apps.usuarios.models import (
    User
)

from apps.formulacion.models import (
    Partida,
    PartidaAccionInterna
)

from apps.contabilidad.models import (
    Comprobante
)

from apps.compras.models import (
    Beneficiario,
    Compromiso
)

class TiposOrdenPago(EmblenBaseModel):
    """ se guardarán los Tipos de Ordenes de Pagos """
    #Directa Especial = todas comprometen y causan al ser generadas
    #Causados = Solo Causan y las orden de compra, servicio y materiales-suministros Compromenten
    #Fondo de Terceros = todas comprometen y causan al ser generadas

    codigo = models.CharField(max_length=3) #DE - CAU - FTR

    descripcion = models.CharField(max_length=100) #Directa Especial - Causados - Fondo de Terceros

    compromete = models.BooleanField(default=False)

    causa = models.BooleanField(default=True)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Tipos de Ordenes de Pagos"


class OrdenesPago(EmblenBaseModel):
    """ se guardarán las Ordenes de Pago creadas"""
    ELABORADA = 0
    VERIFICADA = 1
    ANULADA = 2
    PAGADA = 3
    REVERSADA = 4

    ESTATUS_ORDEN = (
        (ELABORADA, "Elaborada"),
        (VERIFICADA, "Verificada"),
        (ANULADA, "Anulada"),
        (PAGADA, "Pagada"),
        (REVERSADA, "Reversada")
    )

    anio = models.CharField(max_length=4) 

    orden_pago = models.IntegerField()
    #Por año se debe reiniciar
    
    tipo = models.ForeignKey(
        TiposOrdenPago,
        related_name="ordenes_pago",
        on_delete=models.PROTECT
    ) # Tipo de Orden de Pago
    
    descripcion = models.CharField(max_length=300) #Descripción Orden de Pago

    fecha = models.DateField() #fecha de creacion de orden de pago

    monto = models.DecimalField(max_digits=22,decimal_places=4) # Monto de la Orden sin sumar las deducciones

    saldo = models.DecimalField(max_digits=22,decimal_places=4) # Saldo pendiente por pagar del monto de la orden
    #cuando la orden este por pagar el monto debe ser el monto neto a pagar puede ser igual al campo *monto*
    #o un poco menos si hay retenciones que lo diminuyan un poco
    
    monto_deduciones = models.DecimalField(max_digits=22,decimal_places=4) # Monto de las deducciones ( IVA, RETENCIONES, ETC ) de la Orden
    
    saldo_deducciones = models.DecimalField(max_digits=22,decimal_places=4) #Saldo pendiente por pagar del monto de la orden

    beneficiario = models.ForeignKey(
        Beneficiario,
        related_name="ordenes_pago",
        on_delete=models.PROTECT
    )
    
    estatus = models.IntegerField(
        "Estatus Orden", 
        choices=ESTATUS_ORDEN,
        default=ELABORADA
    )

    comprobante = models.ForeignKey(
        Comprobante,
        related_name="ordenes_pago",
        on_delete=models.PROTECT
    )

    comprobante_reverso = models.ForeignKey(
        Comprobante,
        related_name="reverso_ordenes_pago",
        on_delete=models.PROTECT
    )

    compromiso = models.ForeignKey(
        Compromiso,
        related_name="ordenes_pago",
        on_delete=models.PROTECT
    ) # Se llena con el compromiso previamente creado que se crea en compras por una Orden Compra, Servicio o Suministro
    # Este campo es para las ordenes Tipo *CAUSADO*

    elaborador = models.ForeignKey(
        User,
        related_name="elaborador_ordenes_pago",
        on_delete=models.PROTECT
    )

    verificador = models.ForeignKey(
        User,
        related_name="verificador_ordenes_pago",
        on_delete=models.PROTECT
    )

    anulador = models.ForeignKey(
        User,
        related_name="anulador_ordenes_pago",
        on_delete=models.PROTECT
    )  

    reversor = models.ForeignKey(
        User,
        related_name="revisor_ordenes_pago",
        on_delete=models.PROTECT
    )    

    def __str__(self):
        return self.orden_pago

    class Meta:
        verbose_name_plural = "Detalles de Ordenes de Pago"


class Deduccion(EmblenBaseModel):
    """ Se guardarán las Deducciones de las Ordenes de Pago que tengan que tenerlas = ODP_CUENTAS"""
    #ESTA TABLA DEJALA PENDIENTE - DEJAME ANALIZAR SI ES NECESARIA PARA ALGO DIFERENTE QUE GUARDAR EL DETALLE DE LAS DEDUCCIONES
    # SI NO SE UTILIZA PARA OTRA COSA, NO ES NECESARIO PORQUE EN LA SIGUIENTE TABLA TENEMOS LA MISMA INFORMACION
    #NO LA TOMES EN CUENTA

    orden_pago = models.ForeignKey(
        OrdenesPago,
        related_name="deducciones",
        on_delete=models.PROTECT
    )

    partida = models.ForeignKey(
        Partida,
        related_name="deducciones",
        on_delete=models.PROTECT
    ) #Partida contable de las DEDUCCIONES Solamente las que inician con *2* 
    
    monto = models.DecimalField(max_digits=22,decimal_places=4) #monto a pagar de la deducción
    
    saldo = models.DecimalField(max_digits=22,decimal_places=4) #Monto pendiente por pagar de la deducción
    #el saldo queda en 0 posteriormente que en Tesorería realizan el pago

    # pago = models.ForeignKey(
    #     "Pago",
    #     related_name="deducciones",
    #     on_delete=models.PROTECT
    # )
    #Id del pago que haga referencia a la deuda

    def __str__(self):
        return self.orden_pago

    class Meta:
        verbose_name_plural = "Deducciones"


class DetallesOrdenesPago(EmblenBaseModel):
    """  Aquí va todo lo de la orden, partida a las cuales afecte (comienzan por 4)
    partidas contables (comienzan con 2) del beneficiario que va a recibir y las deducciones"""

    DEBITO = 'D'
    CREDITO = 'C'

    TIPO_AFECTACION = (
        (DEBITO, "Débito"),
        (CREDITO, "Crédito")
    )

    orden_pago = models.ForeignKey(
        OrdenesPago,
        related_name="detalles_ordenes_pagos",
        on_delete=models.PROTECT
    )

    partida = models.CharField(max_length=12)
    #cuenta contable de las DEDUCCIONES Solamente las que inician con *2* 
    # Partidas de Gastos 4 o Contables 2
    #Las 4 vienen de la formulación del año en ejecución -> PartidaAccionInterna
    #Allí usaremos la vista de mostrar Centro de Costo -> Acc Específicas -> Partidas de PartidaAccionInterna
    #Y obtener también montos que se tienen disponibles **
    #Contemplando también que solo tomaremos de la formulacion las partidas de gasto
    #Y las contables 2, para lo que vayan a pagar - ejemplo las retenciones, el codigo del beneficiario

    comprobante = models.ForeignKey(
        Comprobante,
        related_name="detalles_ordenes_pago",
        on_delete=models.PROTECT
    )

    tipo_afectacion = models.CharField(
        max_length=1,
        choices=TIPO_AFECTACION,
        default=DEBITO
    ) # D = Debido o C = Credito

    descripcion = models.CharField(max_length=12) 
    #Aquí es para guardar la descripción de la partida o cuenta a pesar de tenerlo en sus tablas pertinentes 
    #Si lo consideras no coloques la descripción ya que son las mismas descripciones de la partida o cuenta utilizada

    monto = models.DecimalField(max_digits=22,decimal_places=4) #Monto por la partida o cuenta
    
    saldo = models.DecimalField(max_digits=22,decimal_places=4) #Monto pendiente por pagar de la deducción
    #el saldo queda en 0 posteriormente que en Tesorería realizan el pago

    # pago = models.ForeignKey(
    #     "Pago",
    #     related_name="deducciones",
    #     on_delete=models.PROTECT
    # )
    #Id del pago que haga referencia a la partida en cuestión

    fecha = models.DateField()

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Detalles de Ordenes de Pago"