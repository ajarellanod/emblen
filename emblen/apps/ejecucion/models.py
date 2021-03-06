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
    FuenteFinanciamiento,
    Publicacion,
    Parroquia,
    PartidaAccionInterna
)


from apps.planificacion.models import (
    TipoModificacion,
)

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
        related_name="cuentas_contables_ejecucion",
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
        related_name="beneficiarios_ejecucion",
        on_delete=models.PROTECT
    )

    tipo_beneficiario = models.ForeignKey(
        TipoBeneficiario,
        related_name="beneficiarios_ejecucion",
        on_delete=models.PROTECT
    )
    
    #Datos de inscripcion
    numero_inscripcion = models.IntegerField() #Correlativo en nuestro sistema diferencia con id es que este codigo puede que lo necesiten ingresar manualmente por alguna razón

    fecha_inscripcion = models.DateField()

    usuario_inscripcion = models.ForeignKey(
        User,
        related_name="beneficiarios_ejecucion",
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
        related_name="cuenta_beneficiarios_ejecucion",
        on_delete=models.PROTECT
    ) #Id cuenta contable generada automáticamente apartir de las cuentas
    #20101020000000	PROVEEDORES - para Contratistas
        #Entonces la cuenta contable sería 201010200001 para el primer CONTRATISTA
    #20101010000000	Cuentas a pagar - para Proveedores
        #Entonces la cuenta contable sería 201010100002 para el primer PROVEEDOR

    cuenta_anticipo = models.ForeignKey(
        CuentaContable,
        related_name="anticipo_beneficiarios_ejecucion",
        on_delete=models.PROTECT
    ) #Id cuenta contable generada automáticamente apartir de la cuenta 10102070000000 (ANTICIPOS)
        # Entonces la cuenta anticipo sería 101020700001 para el primer CONTRATISTA
    #Sólo aplica para contratistas

    def __str__(self):
        # return  self.rif
        return '%s - %s' %(self.rif,self.razon_social) 

    class Meta:
        verbose_name_plural = "Beneficiarios"


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

    # compromiso = models.ForeignKey(
    #     "Compromiso",
    #     related_name="documentos_pagar_ejecucion",
    #     on_delete=models.PROTECT,
    #     null=True
    # )

    beneficiario = models.ForeignKey(
        Beneficiario,
        related_name="documentos_pagar_ejecucion",
        on_delete=models.PROTECT,
        null=True
    )


    def __str__(self):
        return self.numero

    class Meta:
        verbose_name_plural = "Documentos a Pagar"
        unique_together = (("numero", "anio", "beneficiario"),)


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

    beneficiario = models.ForeignKey(
        Beneficiario,
        related_name="ordenes_pago",
        on_delete=models.PROTECT,
        null=True
    )

    documento_pagar = models.ForeignKey(
        DocumentoPagar,
        related_name="ordenes_pago",
        on_delete=models.PROTECT,
        null=True
    )

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
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )

    anulador = models.ForeignKey(
        User,
        related_name="anulador_ordenes_pago",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )  

    reversor = models.ForeignKey(
        User,
        related_name="revisor_ordenes_pago",
        on_delete=models.PROTECT,
        null=True,
        blank=True
    )    

    contador = models.IntegerField(default=1)

    def __str__(self):
        return str(self.orden_pago)

    def gen_rest_attrs(self):
        """
        Genera Atributos Restante del Objeto en Instancia.
        >> ("orden_pago", "contador")
        """
       
        result = OrdenPago.objects.aggregate(Max('contador')).get("contador__max")
        
        if result:
            self.contador = result + 1
            
        self.codigo = self.contador

        self.saldo = self.monto 
        
        self.saldo_deducciones = self.monto_deduciones

    class Meta:
        verbose_name_plural = "Ordenes de Pago"



class Modificacion(EmblenBaseModel):
    """ 
    En este modelo se deben guardar los afectaciones
    que se le vayan haciendo al presupuesto
    """
    anio = models.CharField(max_length=4)

    numero = models.CharField(max_length=10)

    partida_accioninterna = models.ForeignKey(
        PartidaAccionInterna,
        related_name="modificaciones_ejecucion",
        on_delete=models.PROTECT
    )

    tipo_modificacion = models.ForeignKey(
        TipoModificacion,
        related_name="modificaciones_ejecucion",
        on_delete=models.PROTECT
    )

    documento_referenciado = models.IntegerField(null=True, blank=True) 
    
    monto = models.DecimalField(max_digits=22,decimal_places=2)

    saldo = models.DecimalField(max_digits=22,decimal_places=2, null=True, blank=True)

    descripcion = models.CharField(max_length=300)

    def __str__(self):
        return self.numero

    def gen_rest_attrs(self):
        
        self.saldo = self.monto

        self.tipo_modificacion = 1

        self.descripcion = 'dedss'

    def save(self, *args, **kwargs):
        super(Modificacion, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Modificaciones"


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
        related_name="asientos_contables_ejecucion",
        on_delete=models.PROTECT
    )

    cuenta_contable = models.ForeignKey(
        CuentaContable,
        related_name="asientos_contables_ejecucion",
        on_delete=models.PROTECT
    )

    partida = models.ForeignKey(
        PartidaAccionInterna,
        related_name="asientos_contables_ejecucion",
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
