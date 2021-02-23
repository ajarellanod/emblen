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
    Departamento,
    FuenteFinanciamiento
)

# from apps.contabilidad.models import (
#     Comprobante
# )



class TipoOrdenPago(EmblenBaseModel):
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


class ClaseOrdenPago(EmblenBaseModel):
    """ se guardarán las Clases de Ordenes de Pagos """
    #PRESTACIÓN DE SERVICIOS

    descripcion = models.CharField(max_length=100) #PRESTACIÓN DE SERVICIOS

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Clases de Ordenes de Pagos"


class OrdenPago(EmblenBaseModel):
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
        TipoOrdenPago,
        related_name="ordenes_pago",
        on_delete=models.PROTECT
    ) # Tipo de Orden de Pago
    
    clase = models.ForeignKey(
        ClaseOrdenPago,
        related_name="ordenes_pago",
        on_delete=models.PROTECT
    ) # Clases de Orden de Pago

    unidad_origen = models.ForeignKey(
        Departamento,
        related_name="ordenes_pagos",
        on_delete=models.PROTECT
    )

    fuente_financiamiento = models.ForeignKey(
        FuenteFinanciamiento,
        related_name="ordenes_pagos",
        on_delete=models.PROTECT
    )

    # beneficiario = models.ForeignKey(
    #     Beneficiario,
    #     related_name="ordenes_pago",
    #     on_delete=models.PROTECT
    # )

    descripcion = models.CharField(max_length=300) #Descripción Orden de Pago

    fecha = models.DateField() #fecha de creacion de orden de pago

    monto = models.DecimalField(max_digits=22,decimal_places=4) # Monto Total de la Orden

    saldo = models.DecimalField(max_digits=22,decimal_places=4) # Saldo pendiente por pagar del monto de la orden
    #al beneficiario sería el monto sin deducciones
    
    monto_deduciones = models.DecimalField(max_digits=22,decimal_places=4) # Monto de las deducciones ( IVA, RETENCIONES, ETC ) de la Orden
    
    saldo_deducciones = models.DecimalField(max_digits=22,decimal_places=4) #Saldo pendiente real por pagar de las deducciones
   
    estatus = models.IntegerField(
        "Estatus Orden", 
        choices=ESTATUS_ORDEN,
        default=ELABORADA
    )

    # comprobante = models.ForeignKey(
    #     Comprobante,
    #     related_name="ordenes_pago",
    #     on_delete=models.PROTECT
    # )

    # comprobante_reverso = models.ForeignKey(
    #     Comprobante,
    #     related_name="reverso_ordenes_pago",
    #     on_delete=models.PROTECT
    # )

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

    contador = models.IntegerField(default=1)

    def __str__(self):
        return self.orden_pago

    def gen_rest_attrs(self):
        """
        Genera Atributos Restante del Objeto en Instancia.
        >> ("orden_pago", "contador")
        """
       
        result = OrdenPago.objects.aggregate(Max('contador')).get("contador__max")
        
        if result:
            self.contador = result + 1

        self.codigo = self.contador

    class Meta:
        verbose_name_plural = "Ordenes de Pago"