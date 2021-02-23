from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr
from django.db.models import Max

from apps.base.models import EmblenBaseModel
from django.core.exceptions import NON_FIELD_ERRORS


from apps.formulacion.models import (
    Parroquia,
    PartidaAccionInterna
)

from apps.tesoreria.models import (
    Banco,
    TipoCuenta
)

from apps.contabilidad.models import (
    CuentaContable
)


class TipoBeneficiario(EmblenBaseModel):
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
        CuentaContable,
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
        TipoBeneficiario,
        related_name="beneficiarios",
        on_delete=models.PROTECT
    )
    
    #Datos de inscripcion
    numero_inscripcion = models.IntegerField() #Correlativo en nuestro sistema diferencia con id es que este codigo puede que lo necesiten ingresar manualmente por alguna razón

    fecha_inscripcion = models.DateField()

    usuario_inscripcion = models.ForeignKey(
        User,
        related_name="beneficiarios",
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
        CuentaContable,
        related_name="cuenta_beneficiarios",
        on_delete=models.PROTECT
    ) #Id cuenta contable generada automáticamente apartir de las cuentas
    #20101020000000	PROVEEDORES - para Contratistas
        #Entonces la cuenta contable sería 201010200001 para el primer CONTRATISTA
    #20101010000000	Cuentas a pagar - para Proveedores
        #Entonces la cuenta contable sería 201010100002 para el primer PROVEEDOR

    cuenta_anticipo = models.ForeignKey(
        CuentaContable,
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


class TipoDocumento(EmblenBaseModel):
    
    codigo = models.CharField(max_length=4)

    nombre = models.CharField(max_length=100)
    # 1 debe ser FACTURA codigo FACT

    descripcion = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Documentos"


class DocumentoPagar(EmblenBaseModel):
    """Documentos a Pagar """

    CREDITO = 1
    CONTADO = 2
    EFECTIVO = 3

    FORMA_PAGO = (
        (CREDITO, "Crédito"),
        (CONTADO, "Contado"),
        (EFECTIVO, "Efectivo")
    )

    anio = models.CharField(max_length=4)
        
    tipo_documento = models.ForeignKey(
        TipoDocumento,
        related_name="documentos_pagar",
        on_delete=models.PROTECT
    )

    numero = models.CharField(max_length=10)

    numero_control = models.CharField(max_length=10)

    fecha = models.DateField()

    monto_imponible = models.DecimalField(max_digits=22,decimal_places=4)

    monto_iva = models.DecimalField(max_digits=22,decimal_places=4)

    monto = models.DecimalField(max_digits=22,decimal_places=4)

    descripcion = models.CharField(max_length=100)

    forma_pago = models.IntegerField(
        choices=FORMA_PAGO,
        default=CREDITO
    )

    compromiso = models.ForeignKey(
        "Compromiso",
        related_name="documentos_pagar",
        on_delete=models.PROTECT,
        null=True
    )

    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Documentos a Pagar"


class DetalleDocumentoPagar(EmblenBaseModel):
    """Detalles de Documentos a Pagar """
     
    documento_pagar = models.ForeignKey(
        DocumentoPagar,
        related_name="detalles_documentos_pagar",
        on_delete=models.PROTECT
    )

    item = models.IntegerField()

    denominacion = models.CharField(max_length=300)

    cantidad = models.IntegerField()

    precio_unitario = models.DecimalField(max_digits=22,decimal_places=4)

    total= models.DecimalField(max_digits=22,decimal_places=4) #multiplicacion de cantidad * precio_unitario

    contador = models.IntegerField(default=1)

    def __str__(self):
        return self.documento_pagar

    def gen_rest_attrs(self):
        """
        Genera Atributos Restante del Objeto en Instancia.
        >> ("item", "contador")
        """

        result = DetalleDocumentoPagar.objects.filter(
            documento_pagar=self.documento_pagar
        ).aggregate(Max('contador')).get("contador__max")

        if result:
            self.contador = result + 1

        self.item = self.contador

    class Meta:
        verbose_name_plural = "Detalles de Documentos a Pagar"


class TipoContrato(EmblenBaseModel):
    """ se guardarán los Tipos de contratos """
        #Servicios = CSE
        #Materiales y Suministros = CMS
        #Obras = COB

    codigo = models.CharField(max_length=3)

    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Tipos de Contratos"


class Contrato(EmblenBaseModel):
    """ se guardarán los contratos(-obras-, -servicios- y -materiales y suministros-) creados
    Nota: cuando el contrato es CSE o CMS son Contratos Marco porque los beneficiarios serán varios
    Para ellos se creará una tabla donde se lleve la relacion Contratos-Beneficiarios (VALIDAR que SOLO sean contratistas)
    Para los contratos de COB sólo debe haber un beneficiario
    Los COB Suelen tener Anticipos que es una orden de pago (otorgando una parte por adelantado al contratista)
    Los COB se cancelan en totalidad con VALUACIONES de 1 a N valuaciones (que sería ordenes de pago de valuaciones)

    Importante= cuando se crea un contrato marco se esta haciendo un pre-compromiso apartando toda la disponibilidad
    de una partida completa para ese contrato, por ende, debe haber un solo contrato marco por ejercicio para una
    partida presupuestaria.

    partida 402-0-0-1 |
    partida 402-0-0-2 | | pretenecen al contrato Nº 1
    partida 402-0-0-3 |

    partida 402-0-0-4 |
    partida 402-0-0-5 | | pretenecen al contrato Nº 2
    partida 402-0-0-6 |

    partida 402-0-0-1 |
    partida 402-0-0-7 | | pretenecen al contrato Nº 3 || Esto no es posible ya que tanto la partida que termina en 1 y 4
    partida 402-0-0-4 |    pertenecen a otro contrato marco


    """
    anio = models.CharField(max_length=4)

    codigo = models.CharField(max_length=6) # correlativo POR TIPO de contrato - Reinicia por año

    tipo_contrato = models.ForeignKey(
        TipoContrato,
        related_name="contratos",
        on_delete=models.PROTECT
    )

    fecha = models.DateField() #Fecha Creación del Contrato

    descripcion = models.CharField(max_length=300) #del compromiso

    monto = models.DecimalField(max_digits=22,decimal_places=4) #monto total del compromiso

    saldo = models.DecimalField(max_digits=22,decimal_places=4) #Monto que queda pendiente del compromiso

    monto_transito = models.DecimalField(max_digits=22,decimal_places=4) #Monto que queda en transito del compromiso

    cedula_responsable = models.CharField(max_length=12) # J-24297146-5 Cédula de quien está creando el contrato o del representante del contratista

    nombre_responsable = models.CharField(max_length=100)

    addendum = models.ForeignKey(
        "Contrato",
        related_name="contratos",
        on_delete=models.PROTECT,
        null = True,
        blank=True,
    ) #Sólo se llena si es un addemdum ya que tendría que referenciar al contrato al que va a incrementar

    #Hay que crear la estructura para llevar el historial de cada ejecución dentro del sistema 
    # Por ejemplo aquí hay que saber cual usuario elabora, verifica, cuando lo hace. 

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Contratos"


class BeneficiarioContrato(EmblenBaseModel):
    """Beneficiarios de Contratos """
     
    contrato = models.ForeignKey(
        Contrato,
        related_name="beneficiarios_contratos",
        on_delete=models.PROTECT
    )

    beneficiario = models.ForeignKey(
        Beneficiario,
        related_name="beneficiarios_contratos",
        on_delete=models.PROTECT
    )
    # Si es un contrato de Obra = COB solo debe haber un contratista si no es multi beneficiario

    def __str__(self):
        return self.contrato

    class Meta:
        verbose_name_plural = "Beneficiarios de Contratos"


class PartidaContrato(EmblenBaseModel):
    """Partidas de Contratos """

    #Pueden existir 2 diferentes contratos, con las mismas partidas y en el mismo año
    #Pero sólo si uno de ellos es un ADDENDUM ya que un addendum estáría incrementando un Contrato
    #Pero si no es un addemdum no pueden haber 2 con las mismas partidas
    
    anio = models.CharField(max_length=4)

    contrato = models.ForeignKey(
        Contrato,
        related_name="partidas_contratos",
        on_delete=models.PROTECT
    )

    partida_accioninterna = models.ForeignKey(
        PartidaAccionInterna,
        related_name="partidas_contratos",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.contrato

    class Meta:
        verbose_name_plural = "Beneficiarios de Contratos"
        unique_together = (("partida_accioninterna", "anio"),)

 
class TipoCompromiso(EmblenBaseModel):
    """ se guardarán los Tipos de contratos """
    #Orden de Compra = COC
    #Orden de Servicio = COS
    #Orden de Pago Directa Especial = CDE

    codigo = models.CharField(max_length=3)

    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.descripcion

    class Meta:
        verbose_name_plural = "Tipos de Compromisos"


class Compromiso(EmblenBaseModel):
    """ se guardarán los compromisos o llmadas ordenes de (compras, servicios y de Pago *Directa Especial*)  creados"""

    anio = models.CharField(max_length=4)

    codigo = models.CharField(max_length=6) # correlativo POR TIPO de compromiso - Reinicia por año

    tipo_compromiso = models.ForeignKey(
        TipoCompromiso,
        related_name="compromisos",
        on_delete=models.PROTECT
    )

    fecha = models.DateField() #Fecha Creación del Compromiso

    beneficiario = models.ForeignKey(
        Beneficiario,
        related_name="compromisos",
        on_delete=models.PROTECT
    ) # id del beneficiario sacamos aqui tambien al resposable

    descripcion = models.CharField(max_length=300) #del compromiso

    monto = models.DecimalField(max_digits=22,decimal_places=4) #monto total del compromiso

    saldo = models.DecimalField(max_digits=22,decimal_places=4) #Monto que queda pendiente del compromiso

    monto_transito = models.DecimalField(max_digits=22,decimal_places=4) #Monto que queda en transito del compromiso

    #Hay que crear la estructura para llevar el historial de cada ejecución dentro del sistema 
    # Por ejemplo aquí hay que saber cual usuario elabora, verifica, cuando lo hace. 

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Compromisos"
