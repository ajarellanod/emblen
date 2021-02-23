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
    Parroquia
)

from apps.contabilidad.models import (
    CuentaContable
)

from apps.ejecucion.models import (
    OrdenPago
)

class Banco(EmblenBaseModel):
    """Este modelo debería ir en otro Módulo, que debería ser donde se vayan a gestionar los Bancos - Tesorería"""
    
    codigo = models.CharField(max_length=3)

    nombre_corto = models.CharField(max_length=20) #Ej: Banesco

    nombre_completo = models.CharField(max_length=100) #Ej: Banesco Banco Universal, C.A.

    rif = models.CharField(max_length=12) #Ej: J-24297146-5

    direccion = models.CharField(max_length=500)

    codigo_postal = models.CharField(max_length=5)

    parroquia = models.ForeignKey(
        Parroquia,
        related_name="bancos",
        on_delete=models.PROTECT
    )

    cuenta_contable = models.ForeignKey(
        CuentaContable,
        related_name="bancos",
        on_delete=models.PROTECT
    ) #Cuenta contable de las DEDUCCIONES Solamente las que inician con *2* 

    persona_contacto = models.CharField(max_length=100)

    telefono_contacto = models.CharField(max_length=13) #ej: 0414-419-6314

    correo = models.EmailField(max_length=254)

    fax = models.CharField(max_length=12) #ej: 0243-2632021

    condicion = models.BooleanField(default=True) #True = si tienen cuentas para pagos en este banco, False = si solo hay proveedores con cuentas en este banco

    def __str__(self):
        return self.nombre_corto

    class Meta:
        verbose_name_plural = "Bancos"


class TipoCuenta(EmblenBaseModel):
    """Este modelo debería ir en otro Módulo, que debería ser donde se vayan a gestionar las Cuentas Bancarias - Tesorería"""
    
    codigo = models.CharField(max_length=2)

    descripcion = models.CharField(max_length=20)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Tipos de Cuentas Bancarias"


class Cuenta(EmblenBaseModel):
    """Este modelo debería ir en otro Módulo, que debería ser donde se vayan a gestionar las Cuentas Bancarias - Tesorería"""
    
    banco = models.ForeignKey(
        Banco,
        related_name="cuentas",
        on_delete=models.PROTECT
    )

    numero = models.CharField(max_length=20)

    tipo =  models.ForeignKey(
        TipoCuenta,
        related_name="cuentas",
        on_delete=models.PROTECT
    )

    direccion = models.CharField(max_length=500)

    codigo_postal = models.CharField(max_length=5)

    telefono = models.CharField(max_length=13) #ej: 0414-419-6314

    correo = models.EmailField(max_length=254)

    repr_legal = models.CharField(max_length=100)

    rif_repr_legal = models.CharField(max_length=12)

    parroquia = models.ForeignKey(
        Parroquia,
        related_name="cuentas",
        on_delete=models.PROTECT
    )

    cuenta_contable = models.ForeignKey(
        CuentaContable,
        related_name="cuentas",
        on_delete=models.PROTECT
    ) #Cuenta contable de las DEDUCCIONES Solamente las que inician con *2* 

    saldo_ultima_conc = models.DecimalField(max_digits=22,decimal_places=4) 
    fecha_ultima_conc = models.DateField()

    saldo_conc_proceso = models.DecimalField(max_digits=22,decimal_places=4)
    fecha_conc_proceso = models.DateField()

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Cuentas Bancarias"


class TipoImpuesto(EmblenBaseModel):
    """ Se guardarán los Tipos de Impuestos"""

    cuenta_contable = models.ForeignKey(
        CuentaContable,
        related_name="tipos_impuestos",
        on_delete=models.PROTECT
    ) #Cuenta Contable de las DEDUCCIONES Solamente las que inician con *2* 

    porcentaje = models.DecimalField(max_digits=22,decimal_places=4)

    descripcion = models.CharField(max_length=300)
    
    indicador_iva = models.BooleanField(default=False)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Tipos de Impuestos"


class Pago(EmblenBaseModel):
    """ Se guardarán los Pagos realizados"""

    cuenta_contable = models.ForeignKey(
        CuentaContable,
        related_name="pagos",
        on_delete=models.PROTECT
    ) #Cuenta Contable de las DEDUCCIONES Solamente las que inician con *2* 

    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Pagos"


class RetencionDeduccion(EmblenBaseModel):
    """ Se guardarán las Deducciones a Pagar de las ordenes de pago que tengan que tenerlas = ODP_CUENTAS"""
    #ESTA TABLA DEJALA PENDIENTE - DEJAME ANALIZAR SI ES NECESARIA PARA ALGO DIFERENTE QUE GUARDAR EL DETALLE DE LAS DEDUCCIONES
    # SI NO SE UTILIZA PARA OTRA COSA, NO ES NECESARIO PORQUE EN LA SIGUIENTE TABLA TENEMOS LA MISMA INFORMACION
    #NO LA TOMES EN CUENTA
    #NO ES TAN NECESARIA HASTA EL MOMENTO, PODEMOS DADOP EL CASO QUE SE NECESITE PARA ALGO MÁS SE PUEDE CREAR UNA VISTA
    #CON LA CONSULTA REQUERIDA DE LA TABLA DE DETALLES DE ORDENES DE PAGO 

    orden_pago = models.ForeignKey(
        OrdenPago,
        related_name="retenciones_deducciones",
        on_delete=models.PROTECT
    )

    tipo_impuesto = models.ForeignKey(
        TipoImpuesto,
        related_name="retenciones_deducciones",
        on_delete=models.PROTECT
    ) #Cuenta Contable de las DEDUCCIONES Solamente las que inician con *2* 
    
    monto = models.DecimalField(max_digits=22,decimal_places=4) #monto a pagar de la deducción
    
    saldo = models.DecimalField(max_digits=22,decimal_places=4) #Monto pendiente por pagar de la deducción
    #el saldo queda en 0 posteriormente que en Tesorería realizan el pago

    pago = models.ForeignKey(
        Pago,
        related_name="retenciones_deducciones",
        on_delete=models.PROTECT,
        null = True
    )
    #Id del pago que haga referencia a la deuda

    def __str__(self):
        return self.orden_pago

    class Meta:
        verbose_name_plural = "Retenciones y Deducciones"

