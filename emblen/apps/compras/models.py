from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr
from django.db.models import Max

from apps.base.models import EmblenBaseModel
from django.core.exceptions import NON_FIELD_ERRORS


from apps.formulacion.models import (
    Partida,
    Parroquia
)

from apps.tesoreria.models import (
    Banco,
    TipoCuenta
)


class TiposBeneficiario(EmblenBaseModel):
    """ se guardarán los Tipos de Beneficiarios """
        #Contratistas = CTT
        #Proveedores = PRV
        #Nomina = NMN
        #Arrendamiento = ARR
        #Donaciones = DON
        #Viaticos = VTC
        #Otras =  OTR como para servicios básicos

    abreviacion = models.CharField(max_length=3)

    descripcion = models.CharField(max_length=100)

    # tipo_orden_pago = models.ForeignKey(
    #     TiposOrdenPago,
    #     related_name="tipo_beneficiario",
    #     on_delete=models.PROTECT
    # )

    cuenta_contable = models.ForeignKey(
        Partida,
        related_name="tipos_beneficiarios",
        on_delete=models.PROTECT
    ) #Id cuenta contable generado automático EJ: cuenta dependiendo el tipo 2.01.01.01.01.001

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Tipos de Beneficiarios"


class Beneficiario(EmblenBaseModel):
    """ se guardarán los beneficiario creados"""
    
    rif = models.CharField(max_length=12)
    # Sólo iniciando con J-24297146-5 """

    razon_social = models.CharField(max_length=100) # Nombre del ente

    siglas = models.CharField(max_length=10) # Siglas del ente

    direccion= models.CharField(max_length=500) # Dirección del ente

    telefono = models.CharField(max_length=13) #Teléfono del ente ej: 0414-419-6314

    correo = models.EmailField(max_length=254)

    parroquia = models.ForeignKey(
        Parroquia,
        related_name="beneficiarios",
        on_delete=models.PROTECT
    )

    tipo_beneficiario = models.ForeignKey(
        TiposBeneficiario,
        related_name="beneficiarios",
        on_delete=models.PROTECT
    )
    
    #Datos de inscripcion
    numero_inscripcion = models.IntegerField() #Correlativo en nuestro sistema diferencia con id es que este codigo puede que lo necesiten ingresar manualmente por alguna razón

    fecha_inscripcion = models.DateField()

    usuario_inscripcion = models.ForeignKey(
        User,
        related_name="beneficiario",
        on_delete=models.PROTECT
    )

    #Datos de Registro del Ente
    numero_registro = models.CharField(max_length=12) # Creo que es un numero propio del contratista

    fecha_registro = models.DateField()

    capital = models.DecimalField(max_digits=22,decimal_places=4) #Solo aplica si es proveedor y contratista

    #Datos del representante del Ente
    representante = models.CharField(max_length=100) # Nombres y Apellidos #Solo aplica si es proveedor y contratista

    cedula_representante = models.CharField(max_length=12) # Sólo iniciando con J-24297146-5 #Solo aplica si es proveedor y contratista

    #Datos de beneficiario
    fecha_vigencia = models.DateField()

    cuenta_contable = models.ForeignKey(
        Partida,
        related_name="cuenta_beneficiarios",
        on_delete=models.PROTECT
    ) #Id cuenta contable generada automáticamente apartir de las cuentas
    #20101020000000	PROVEEDORES - para Contratistas
        #Entonces la cuenta contable sería 201010200001 para el primer CONTRATISTA
    #20101010000000	Cuentas a pagar - para Proveedores
        #Entonces la cuenta contable sería 201010100002 para el primer PROVEEDOR

    cuenta_anticipo = models.ForeignKey(
        Partida,
        related_name="anticipo_beneficiarios",
        on_delete=models.PROTECT
    ) #Id cuenta contable generada automáticamente apartir de la cuenta 10102070000000 (ANTICIPOS)
        # Entonces la cuenta anticipo sería 101020700001 para el primer CONTRATISTA
    #Sólo aplica para contratistas

    def __str__(self):
        return self.rif

    class Meta:
        verbose_name_plural = "Beneficiarios"


class CuentaBeneficiario(EmblenBaseModel):
    """
    Este modelo debería ir en otro Módulo,
    que debería ser donde se vayan a gestionar los proveedores
    """

    beneficiario = models.ForeignKey(
        Beneficiario,
        related_name="cuenta_beneficiarios",
        on_delete=models.PROTECT
    )

    banco = models.ForeignKey(
        Banco,
        related_name="cuenta_beneficiarios",
        on_delete=models.PROTECT
    )

    numero = models.CharField(max_length=20)

    tipo =  models.ForeignKey(
        TipoCuenta,
        related_name="cuenta_beneficiarios",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Cuentas Bancarias de Beneficiarios"


class Compromiso(EmblenBaseModel):
    """ se guardarán los contratos creados"""

    comprobante = models.CharField(max_length=6) # Ej: CS1710 = Contrato Servicio = CS - Año 2017 = 17- numero contrato 10
    
    fecha = models.DateField() #Fecha Creación del Compromiso/Contrato

    beneficiario = models.ForeignKey(
        Beneficiario,
        related_name="Compromiso",
        on_delete=models.PROTECT
    ) # id del contratista

    descripcion = models.CharField(max_length=300) #del compromiso

    monto = models.DecimalField(max_digits=22,decimal_places=4) #monto total del compromiso

    saldo = models.DecimalField(max_digits=22,decimal_places=4) #Monto que queda pendiente del compromiso

    monto_transito = models.DecimalField(max_digits=22,decimal_places=4) #Monto que queda en transito del compromiso

    cedula_responsable = models.CharField(max_length=12) # J-24297146-5 Cédula de quien está creando el contrato o del representante del contratista

    #Hay que crear la estructura para llevar el historial de cada ejecución dentro del sistema 
    # Por ejemplo aquí hay que saber cual usuario elabora, verifica, cuando lo hace. 

    def __str__(self):
        return self.comprobante

    class Meta:
        verbose_name_plural = "Compromisos"
