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
    Parroquia
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

    partida = models.ForeignKey(
        Partida,
        related_name="bancos",
        on_delete=models.PROTECT
    ) #Partida contable de las DEDUCCIONES Solamente las que inician con *2* 

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

    partida = models.ForeignKey(
        Partida,
        related_name="cuentas",
        on_delete=models.PROTECT
    ) #Partida contable de las DEDUCCIONES Solamente las que inician con *2* 

    saldo_ultima_conc = models.DecimalField(max_digits=22,decimal_places=4) 
    fecha_ultima_conc = models.DateField()

    saldo_conc_proceso = models.DecimalField(max_digits=22,decimal_places=4)
    fecha_conc_proceso = models.DateField()

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Cuentas Bancarias"