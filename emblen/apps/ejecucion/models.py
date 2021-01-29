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
    PartidaAccionInterna
)

class CodigoContable(EmblenBaseModel):
    """Este modelo debería ir en otro Módulo, que debería ser donde se vayan a gestionar los Códigos Contables - Contabilidad"""
    """ 
    Almanecena las cuentas contables - partidas contables.
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

    saldo = models.DecimalField(max_digits=22,decimal_places=2,null=True)

    saldo_anterior = models.DecimalField(max_digits=22,decimal_places=2,null=True)

    def sin_ceros(self):
        """Retorna la cuenta sin ceros a la derecha"""
        return self.cuenta[0:self.NIVELES[self.nivel]]

    def siguientes(self):
        """Devuelve queryset de las partidas hijas del nivel siguiente"""
        
        debe_comenzar = self.sin_ceros() 
        siguiente_nivel = self.nivel + 1

        queryset = Partida.objects.filter(
            nivel=siguiente_nivel,
            cuenta__startswith=debe_comenzar,
        )

        return queryset
        
    class Meta:
        ordering = ('-creado',)
        verbose_name_plural = "Códigos Contables"

    def __str__(self):
        return self.cuenta


class Contratista(EmblenBaseModel):
     """ se guardarán los contratistas creados"""

    FIJO = 0
    EVENTUAL = 1

    TIPO_CONTRATISTA = (
        (FIJO, "Fijo"),
        (EVENTUAL, "Eventual")
    )

    rif = models.CharField(max_length=12) # Sólo iniciando con J-24297146-5

    razon_social = models.CharField(max_length=100) # Nombre del ente

    siglas = models.CharField(max_length=10) # Siglas del ente

    direccion= models.CharField(max_length=500) # Dirección del ente

    telefono = models.CharField(max_length=13) #Teléfono del ente ej: 0414-419-6314
    
    parroquia = models.ForeignKey(
        Parroquia,
        related_name="Contratistas",
        on_delete=models.PROTECT
    )
    
    #Datos de inscripcion
    numero_inscripcion = models.IntegerField() #Correlativo en nuestro sistema diferencia con id es que este codigo puede que lo necesiten ingresar manualmente por alguna razón

    fecha_inscripcion = models.DateField()

    usuario_inscripcion = models.ForeignKey(
        Usuario,
        related_name="Contratistas",
        on_delete=models.PROTECT
    )

    #Datos de Registro del Ente
    numero_registro = models.CharField(max_length=12) # Creo que es un numero propio del contratista

    fecha_registro = models.DateField()

    capital = models.DecimalField(max_digits=22,decimal_places=4)

    #Datos del representante del Ente
    representante = models.CharField(max_length=100) # Nombres y Apellidos

    cedula_representante = models.CharField(max_length=12) # Sólo iniciando con J-24297146-5

    #Datos de contratista
    fecha_vigencia = models.DateField()
    
    sexo_beneficiario = models.IntegerField(
        "Tipo de Contratista", 
        choices=TIPO_CONTRATISTA,
        default=FIJO
    ) #Si es eventual no se crea un codigo contable si es fijo automaticamente se debe crear uno

    codigo_contable = models.ForeignKey(
        CodigoContable,
        related_name="Contratistas",
        on_delete=models.PROTECT
    ) #Id codigo contable generado automatico EJ 20171020018000

    codigo_anticipo = models.ForeignKey(
        CodigoContable,
        related_name="Contratistas",
        on_delete=models.PROTECT
    ) #Id codigo contable para anticipos generado automatico EJ 20171020018000 en la misma tabla de codigo_contable

    def __str__(self):
        return self.rif

    class Meta:
        verbose_name_plural = "Contratistas"


class Compromiso(EmblenBaseModel):
    """ se guardarán los contratos creados"""

    comprobante = models.CharField(max_length=6) # Ej: CS1710 = Contrato Servicio = CS - Año 2017 = 17- numero contrato 10
    
    fecha = models.DateField() #Fecha Creación del Compromiso/Contrato

    contratista = models.ForeignKey(
        Contratista,
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


class TiposOrdenesPago(EmblenBaseModel):
    """ se guardarán los Tipos de Ordenes de Pagos"""
    #DE = Directa Especial
    #NP = nomina de pago 
    codigo = models.CharField(max_length=5)

    descripcion = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Ordenes de Pagos"


class Comprobante(EmblenBaseModel):
    """ se guardarán todos los Comprobantes - es como una tabal resumen con combante y monto por mes"""

    codigo = models.CharField(max_length=9) #año + mes + 5 digitos correlativos = 17010001 = año 2017, mes enero 10, el primer comprbante del mes 

    descripcion = models.CharField(max_length=100)

    fecha = models.DateField()

    monto = models.DecimalField(max_digits=22,decimal_places=4)

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Comprobantes"


class OrdenesPago(EmblenBaseModel):
    """ se guardarán las Ordenes de Pago creadas"""
    ELABORADA = 0
    VERIFICADA = 1
    ANULADA = 2
    PAGADA = 3

    ESTATUS_ORDEN = (
        (ELABORADA, "Elaborada")
        (VERIFICADA, "Verificada"),
        (ANULADA, "Anulada"),
        (PAGADA, "Pagada")
    )

    CONTRATISTA = 0
    PROVEEDOR = 1
    OTRO = 2
    DONACION = 3
    VIATICO = 4

    TIPO_BENEFICIARIO = (
        (CONTRATISTA, "Contratistas"),
        (PROVEEDOR, "Proveedores"),
        (OTRO, "Otros"),
        (DONACION, "Donaciones"),
        (VIATICO, "Viáticos")
    )
    
    numero = models.CharField(max_length=12) #Año 17 + correlativo = Numero de orden = 17001 y por año se reinicia

    tipo = models.ForeignKey(
        TiposOrdenesPago,
        related_name="ordenes_pago",
        on_delete=models.PROTECT
    ) # Tipo de Orden de Pago
    
    descripcion = models.CharField(max_length=300) #Descripción Orden de Pago

    fecha = models.DateField() #fecha de creacion de orden de pago

    monto = models.DecimalField(max_digits=22,decimal_places=4) # Monto de la Orden sin sumar las deducciones

    saldo = models.DecimalField(max_digits=22,decimal_places=4) # Saldo pendiente por pagar del monto de la orden = ejemplo cargaron una sola partida con la mitad del monto total, quedaría la mitas de saldo pendiente
    
    monto_deduciones = models.DecimalField(max_digits=22,decimal_places=4) # Monto de las deducciones ( IVA, RETENCIONES, ETC ) de la Orden
    
    saldo_deducciones = models.DecimalField(max_digits=22,decimal_places=4) #si quedan restantes del monto_deducciones (para eso restantes son los saldos = Saldos Restantes)

    tipo_beneficiario = models.IntegerField(
        "Tipo Beneficiario", 
        choices=TIPO_BENEFICIARIO,
        default=CONTRATISTA
    )

    beneficiario = models.IntegerField() # Traer todo del beneficiario puede ser un contratista, proveedor, donaciones, viaticos, otros
        #Aquí no sé como haríamos porque contratista, proveedor, donaciones, viaticos, otros, estarían en tablas diferentes
        #Pero aquí debemos guardar el Id del mismo sea cual sea de ellos
    
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
        related_name="ordenes_pago",
        on_delete=models.PROTECT
    )

    codigo_compromiso = models.ForeignKey(
        Compromiso,
        related_name="ordenes_pago",
        on_delete=models.PROTECT
    ) # Sólo si tiene un compromiso previo depende del tipo de orden de Pago

    elaborador = models.ForeignKey(
        Usuario,
        related_name="ordenes_pago",
        on_delete=models.PROTECT
    )

    verificador = models.ForeignKey(
        Usuario,
        related_name="ordenes_pago",
        on_delete=models.PROTECT
    )

    anulador = models.ForeignKey(
        Usuario,
        related_name="ordenes_pago",
        on_delete=models.PROTECT
    )    

class Deduccion(EmblenBaseModel):
    """ Se guardarán las Deducciones de las Ordenes de Pago que tengan que tenerlas = ODP_CUENTAS"""

    orden_pago = models.ForeignKey(
        OrdenesPago,
        related_name="deduccion",
        on_delete=models.PROTECT
    )

    codigo_contable = models.ForeignKey(
        CodigoContable,
        related_name="deduccion",
        on_delete=models.PROTECT
    ) # es una partida que inicia con 2 que son contables
    
    monto = models.DecimalField(max_digits=22,decimal_places=4) #monto a pagar de la deducción
    
    saldo = # Es el monto total que tienen para la deducción

    #general mente monto y saldo son iguales a menos que el monto sea menor a lo que van a pagar


class DetallesOrdenesPago(EmblenBaseModel):
    """  Aquí va todo lo de la orden, partida a las cuales afecte, codigo contable 
    del beneficiario que va a recibir y las deducciones"""

    DEBITO = D
    CREDITO = C

    TIPO_AFECTACION = (
        (DEBITO, "Debito")
        (CREDITO, "Crédito")
    )
    
    orden_pago = models.ForeignKey(
        OrdenesPago,
        related_name="detalles_ordenes_pago",
        on_delete=models.PROTECT
    )

    comprobante = models.ForeignKey(
        Comprobante,
        related_name="detalles_ordenes_pago",
        on_delete=models.PROTECT
    )
    
    cuenta = models.CharField(max_length=12) # partida o cuenta de gastos 4 - ingresos 3 - Contables 1
    #estas vienden de la formulación del año en ejecución 
    #Es decir podemos colocar una tabla con las acciones especificas de un lado y al seleccionar una 
    #se muestren las partidas relacionadas con esa acción especifica de la tabla PartidaAccionInterna para tener los 
    #montos que se tienen disponibles

    tipo_afectacion = models.CharField(max_length=1,
        "Tipo Afectación", 
        choices=TIPO_AFECTACION,
        default=DEBITO
    ) # D = Debido o C = Credito

    descripcion = models.CharField(max_length=12) #Aquí es para guardar la descripción de la partida o cuenta a pesar de tenerlo en sus tablas pertinentes 
    #Si lo consideras no coloques la descripción ya que son las mismas descripciones de la partida o cuenta utilizada

    monto = models.DecimalField(max_digits=22,decimal_places=4) #Monto por la partida o cuenta

    fecha = models.DateField()