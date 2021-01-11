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
    CtasCCostoAInt
    )


class CodigoContable(EmblenBaseModel):
    """Este modelo debería ir en otro Módulo, que debería ser donde se vayan a gestionar los Códigos Contables - Contabilidad"""
    codigo = models.CharField(max_length=3)

    tipo = models.CharField(max_length=20)

    """Aquí faltan muchos campos que aún no sé cuales vamos a colocar esto se estructurará posteriormente"""

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Códigos Contables"    


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
        related_name="Bancos",
        on_delete=models.PROTECT
    )

    codigo_contable = models.ForeignKey(
        CodigoContable,
        related_name="Bancos",
        on_delete=models.PROTECT
    )

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


class Proveedor(EmblenBaseModel):
    """Este modelo debería ir en otro Módulo, que debería ser donde se vayan a gestionar los Proveedores"""
    
    nombre = models.CharField(max_length=100)

    siglas = models.CharField(max_length=20)

    rif = models.CharField(max_length=12) #Ej: J-24297146-5

    direccion = models.CharField(max_length=500)

    codigo_postal = models.CharField(max_length=5)

    telefono = models.CharField(max_length=13) #ej: 0414-419-6314

    correo = models.EmailField(max_length=254)

    repr_legal = models.CharField(max_length=100)

    rif_repr_legal = models.CharField(max_length=12)

    parroquia = models.ForeignKey(
        Parroquia,
        related_name="proveedores",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "proveedores"
        

class CuentaProveedor(EmblenBaseModel):
    """Este modelo debería ir en otro Módulo, que debería ser donde se vayan a gestionar los proveedores"""

    """Id del proveedor"""
    proveedor = models.ForeignKey(
        Proveedor,
        related_name="cuentaproveedores",
        on_delete=models.PROTECT
    )

    banco = models.ForeignKey(
        Banco,
        related_name="cuentaproveedores",
        on_delete=models.PROTECT
    )

    numero = models.CharField(max_length=20)

    tipo =  models.ForeignKey(
        TipoCuenta,
        related_name="cuentaproveedores",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Cuentas Bancarias de proveedores"


class TiposDocumento(EmblenBaseModel):
    
    codigo = models.CharField(max_length=2)

    nombre = models.CharField(max_length=100)

    descripcion = models.CharField(max_length=200)

    tipo_afectacion = models.CharField(max_length=2)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Documentos"


class Documento(EmblenBaseModel):

    anio = models.CharField(max_length=4)

    numero = models.CharField(max_length=10)

    # programa = models.ForeignKey(
    #     Programa,
    #     related_name="documentos",
    #     on_delete=models.PROTECT
    # )

    # partida = models.ForeignKey(
    #     Partida,
    #     related_name="documentos",
    #     on_delete=models.PROTECT
    # )

    cta_ccosto_accint = models.ForeignKey(
        CtasCCostoAInt,
        related_name="documentos",
        on_delete=models.PROTECT
    )

    tipo_documento = models.ForeignKey(
        TiposDocumento,
        related_name="documentos",
        on_delete=models.PROTECT
    )

    fecha = models.DateField()

    proveedor = models.ForeignKey(
        Proveedor,
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
    
    """ En este modelo se deben guardar los acumulados de los cambios que se le vayan haciendo al presupuesto POR MES"""
    
    anio = models.CharField(max_length=4)

    mes = models.CharField(max_length=2)

    cta_ccosto_accint = models.ForeignKey(
        CtasCCostoAInt,
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
        unique_together = (("cta_ccosto_accint", "mes", "anio"),)