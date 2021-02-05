from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr
from django.db.models import Max

from apps.base.models import EmblenBaseModel
from django.core.exceptions import NON_FIELD_ERRORS


class Sector(EmblenBaseModel):

    codigo = models.CharField(max_length=2)

    nombre = models.CharField(max_length=100)

    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Sectores"


class Dependencia(EmblenBaseModel):

    sector = models.ForeignKey(
        Sector,
        related_name="dependencias",
        on_delete=models.PROTECT
    )

    codigo = models.CharField(max_length=2)

    nombre = models.CharField(max_length=100)

    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Dependencias"


class Departamento(EmblenBaseModel):
    
    unidad_ejecutora = models.ForeignKey(
        "UnidadEjecutora",
        related_name="departamentos",
        on_delete=models.PROTECT,
    )

    codigo = models.CharField(max_length=14)

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Departamentos"


class Estado(EmblenBaseModel):
    
    codigo = models.CharField(max_length=10)

    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Estados"


class Municipio(EmblenBaseModel):

    estado = models.ForeignKey(
        Estado,
        related_name="municipios",
        on_delete=models.PROTECT
    )

    codigo = models.CharField(max_length=10)

    nombre = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Municipios"


class Parroquia(EmblenBaseModel):

    municipio = models.ForeignKey(
        Municipio,
        related_name="parroquias",
        on_delete=models.PROTECT
    )

    codigo = models.CharField(max_length=10)

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Parroquias"


class FuenteFinanciamiento(EmblenBaseModel):

    codigo = models.CharField(max_length=10)

    nombre = models.CharField(max_length=100)

    orden = models.IntegerField()

    externo = models.BooleanField(default=False)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Fuentes de Financiamientos"


class CentroCosto(EmblenBaseModel):

    NIVELES = {
        1: 1,
        2: 3
    }
    
    codigo = models.CharField(max_length=6,unique=True)

    nombre = models.CharField(max_length=100)

    nivel = models.IntegerField()

    def sin_ceros(self):
        """Retorna el codigo sin ceros a la derecha"""
        return self.codigo[0:self.NIVELES[self.nivel]]

    def siguientes(self):
        """Devuelve queryset de los centros de costo hijos del nivel siguiente"""
        
        debe_comenzar = self.sin_ceros() 
        siguiente_nivel = self.nivel + 1

        queryset = CentroCosto.objects.filter(
            nivel=siguiente_nivel,
            codigo__startswith=debe_comenzar,
        )

        return queryset

    class Meta:
        ordering = ('-creado',)
        verbose_name_plural = "Centros de Costos"

    def __str__(self):
        return self.codigo


class UnidadEjecutora(EmblenBaseModel):

    dependencia = models.ForeignKey(
        Dependencia,
        related_name="unidadejecutoras",
        on_delete=models.PROTECT
    )
    
    adscrito = models.ForeignKey(
        "UnidadEjecutora",
        related_name="unidadejecutoras",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
    )

    codigo = models.CharField(max_length=10)

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Unidades Ejecutoras"


class SectorDesarrollador(EmblenBaseModel):
    
    codigo = models.CharField(max_length=3)

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Sectores Desarrolladores"


class UnidadMedida(EmblenBaseModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)

    dimension = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Unidades de Medidas"


class TipoBeneficiario(EmblenBaseModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Beneficiarios"


class PeriodoActualizacion(EmblenBaseModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Periodos de Actualizacion"
 

class CondicionPrograma(EmblenBaseModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)  #Formulado - Banco de Proyectos

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Condiciones de los Programas"


class Programa(EmblenBaseModel):

    FEMENINO = 0
    MASCULINO = 1
    NO_DEFINIDO = 2

    SEXO_BENEFICIARIO = (
        (FEMENINO, "Femenino"),
        (MASCULINO, "Masculino"),
        (NO_DEFINIDO, "No Definido")
    )
    
    NIVEL = (
        (1, "Proyecto"),
        (2, "Acción Centralizada")
    )

    periodo_actualizacion = models.ForeignKey(
        PeriodoActualizacion,
        related_name="programas",
        on_delete=models.PROTECT
    )

    # Información Básica =====================================

    anio = models.CharField(max_length=4)

    codigo = models.CharField(max_length=11)

    nivel = models.IntegerField(choices=NIVEL)

    detalle = models.TextField()

    condicion = models.ForeignKey(
        CondicionPrograma,
        related_name="programas",
        on_delete=models.PROTECT
    )

    estado = models.CharField(max_length=3, default="INI") #INI

    sector_desarrollador = models.ForeignKey(
        SectorDesarrollador,
        related_name="programas",
        on_delete=models.PROTECT
    )

    plan_inversion_social = models.BooleanField(default=False)

    inicio = models.DateField()

    fin = models.DateField()

    responsable = models.ForeignKey(
        Departamento,
        related_name="programas",
        on_delete=models.PROTECT
    )

    # Ubicación ==============================================

    extension_territorial = models.BooleanField(default=True)

    parroquia = models.ForeignKey(
        Parroquia,
        related_name="programas",
        on_delete=models.PROTECT
    )

    # Objetivos ============================================
    
    desarrollo_sostenible = models.TextField()

    estrategico = models.TextField()

    problematica = models.TextField()

    especifico = models.TextField()

    resumen = models.TextField()   

    # Resultado Esperados ==================================

    bien_servicio = models.TextField()

    unidad_medida = models.ForeignKey(
        UnidadMedida,
        related_name="programas",
        on_delete=models.PROTECT
    )

    indicador_situacion = models.TextField()

    indicador_fuente = models.TextField()

    indicador_formula = models.TextField()

    indicador_objetivo = models.TextField()

    # Distribución Meta Física Trimestral ===================

    trimestre_1 = models.DecimalField(max_digits=22,decimal_places=2)
    trimestre_2 = models.DecimalField(max_digits=22,decimal_places=2)
    trimestre_3 = models.DecimalField(max_digits=22,decimal_places=2)
    trimestre_4 = models.DecimalField(max_digits=22,decimal_places=2)
    
    # Beneficiarios ==========================================

    tipo_beneficiario = models.ForeignKey(
        TipoBeneficiario,
        related_name="programas",
        on_delete=models.PROTECT
    )

    sexo_beneficiario = models.IntegerField(
        "Sexo del Beneficiario", 
        choices=SEXO_BENEFICIARIO,
        default=NO_DEFINIDO
    )
    
    # Empleos Generados =======================================

    directo_masculino = models.IntegerField()

    directo_femenino = models.IntegerField()
    
    indirecto_masculino = models.IntegerField()
    
    indirecto_femenino = models.IntegerField()

    # Porcentaje Avance ========================================

    ejecucion_fisica = models.FloatField()

    ejecucion_financiera = models.FloatField()

    # Fields de Ayuda =========================

    duracion = models.DurationField()

    contador = models.IntegerField(default=1)


    def gen_codigo(self):
        """Genera el codigo del Programa en instancia"""
        
        # Consulta donde se busca la dependencia
        dependencia = self.responsable.unidad_ejecutora.dependencia
        
        # Extraccion del codigo en cada modelo y nivel
        cod_sector = dependencia.sector.codigo
        cod_dependencia = dependencia.codigo
        cod_tipo = f"0{self.nivel}"
        cod_contador = "{:02}".format(self.contador)

        self.codigo = f"{cod_sector}{cod_dependencia}{cod_tipo}{cod_contador}"


    def gen_rest_attrs(self):
        """
        Genera Atributos Restante del Objeto en Instancia.
        >> ("codigo", "anio", "estado", "contador", "duracion")
        """

        self.anio = self.inicio.year
        self.duracion = self.fin - self.inicio

        # Obtiene el contador mayor de ese año y ese tipo de Programa 
        result = Programa.objects.filter(
            nivel=self.nivel, anio=self.anio
        ).aggregate(Max('contador')).get("contador__max")

        if result:
            self.contador = result + 1

        # Genera el codigo del Programa
        self.gen_codigo()


    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Programas"
        unique_together = (("anio", "nivel", "contador"),)


class LineaPlan(EmblenBaseModel):
    
    codigo = models.CharField(max_length=2)

    descripcion = models.TextField()

    tipo = models.CharField(max_length=1) #N = Nacional - E = Estadal 

    def __str__(self):
        return self.codigo

    class Meta:
        verbose_name_plural = "Lineas del Plan"


class LineaPrograma(EmblenBaseModel):
    
    codigo = models.CharField(max_length=4)

    auxiliar = models.IntegerField(default=1)

    programa = models.ForeignKey(
        Programa,
        related_name="lineas_programas",
        on_delete=models.PROTECT
    )

    historico = models.ForeignKey(
        LineaPlan,
        related_name="lineas_programas",
        on_delete=models.PROTECT
    )

    nacional = models.TextField()
    
    estrategico = models.TextField()
    
    general = models.TextField()

    def __str__(self):
        return self.codigo

    def gen_rest_attrs(self):
        """
        Genera Atributos Restante del Objeto en Instancia.
        >> ("codigo", "auxiliar")
        """

        result = LineaPrograma.objects.filter(
            programa=self.programa
        ).aggregate(Max('auxiliar')).get("auxiliar__max")

        if result:
            self.auxiliar = result + 1

        self.codigo = "{:04}".format(self.auxiliar)

    class Meta:
        verbose_name_plural = "Lineas del Programa"


class PlanDesarrollo(EmblenBaseModel):
    
    codigo = models.CharField(max_length=4)

    auxiliar = models.IntegerField(default=1)

    programa = models.ForeignKey(
        Programa,
        related_name="plan_desarrollos",
        on_delete=models.PROTECT
    )

    dimension = models.ForeignKey(
        LineaPlan,
        related_name="plan_desarrollos",
        on_delete=models.PROTECT
    )

    plan_metas = models.TextField()
    
    metas = models.TextField()
    
    solucion = models.TextField()

    def __str__(self):
        return self.codigo

    def gen_rest_attrs(self):
        """
        Genera Atributos Restante del Objeto en Instancia.
        >> ("codigo", "auxiliar")
        """

        result = PlanDesarrollo.objects.filter(
            programa=self.programa
        ).aggregate(Max('auxiliar')).get("auxiliar__max")

        if result:
            self.auxiliar = result + 1

        self.codigo = "{:04}".format(self.auxiliar)

    class Meta:
        verbose_name_plural = "Planes de Desarrollo"


class AreaInversion(EmblenBaseModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Areas de Inversion"


class CategoriaAreaInversion(EmblenBaseModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)

    area_inversion = models.ForeignKey(
        AreaInversion,
        related_name="categoria_area_inversion",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Categorias de las Areas de Inversion"


class EstatusFinanciamientoExterno(EmblenBaseModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Estatus de Financiamientos Externos"


class TipoAreaInversion(EmblenBaseModel):
    
    codigo = models.CharField(max_length=7)

    nombre = models.CharField(max_length=100)

    categoria = models.ForeignKey(
        CategoriaAreaInversion,
        related_name="tipo_area_inversion",
        on_delete=models.PROTECT
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Areas de Inversion"
        

class AccionEspecifica(EmblenBaseModel):

    FEMENINO = 0
    MASCULINO = 1
    NO_DEFINIDO = 2

    SEXO_BENEFICIARIO = (
        (FEMENINO, "Femenino"),
        (MASCULINO, "Masculino"),
        (NO_DEFINIDO, "No Definido")
    )
    
    programa = models.ForeignKey(
        Programa,
        related_name="acciones_especificas",
        on_delete=models.PROTECT
    )

   # Información Básica

    codigo = models.CharField(max_length=11)

    condicion = models.ForeignKey(
        CondicionPrograma,
        related_name="acciones_especificas",
        on_delete=models.PROTECT
    )

    descripcion = models.TextField()

    detallada = models.TextField()

    especifico = models.TextField()

    inicio = models.DateField()

    fin = models.DateField()

    impacto_social = models.TextField()

    articulacion = models.TextField()

    vinculacion = models.BooleanField(default=True)

    financiamiento_externo = models.BooleanField(default=True)

    bien_servicio = models.TextField()

    # Beneficiarios

    tipo_beneficiario = models.ForeignKey(
        TipoBeneficiario,
        related_name="acciones_especificas",
        on_delete=models.PROTECT
    )

    sexo_beneficiario = models.IntegerField(
        "Sexo del Beneficiario", 
        choices=SEXO_BENEFICIARIO,
        default=NO_DEFINIDO
    )


    # Empleos Generados

    directo_masculino = models.IntegerField()

    directo_femenino = models.IntegerField()
    
    indirecto_masculino = models.IntegerField()
    
    indirecto_femenino = models.IntegerField()

    # Responsables

    responsable = models.ForeignKey(
        Departamento,
        related_name="acciones_especificas",
        on_delete=models.PROTECT
    ) 

    # Metas Físicas

    extension_territorial = models.BooleanField(default=True)

    parroquia = models.ForeignKey(
        Parroquia,
        related_name="acciones_especificas",
        on_delete=models.PROTECT
    )

    sector = models.ForeignKey(
        SectorDesarrollador,
        related_name="acciones_especificas",
        on_delete=models.PROTECT
    )

    plazo_ejecucion = models.IntegerField()

    unidad_medida = models.ForeignKey(
        UnidadMedida,
        related_name="acciones_especificas",
        on_delete=models.PROTECT
    )

    centro_costo = models.ForeignKey(
        CentroCosto,
        related_name="acciones_especificas",
        on_delete=models.PROTECT
    )

    # Distribución Física Trimestral
    trimestre_1 = models.DecimalField(max_digits=22,decimal_places=2)
    trimestre_2 = models.DecimalField(max_digits=22,decimal_places=2)
    trimestre_3 = models.DecimalField(max_digits=22,decimal_places=2)
    trimestre_4 = models.DecimalField(max_digits=22,decimal_places=2)

    # Fuente Financimiento Externo

    estatus_financiamiento_externo = models.ForeignKey(
        EstatusFinanciamientoExterno,
        related_name="acciones_especificas",
        on_delete=models.PROTECT
    )

    tipo_area_inversion = models.ForeignKey(
        TipoAreaInversion,
        related_name="acciones_especificas",
        on_delete=models.PROTECT
    )

    fase = models.CharField(max_length=100)

    # Porcentaje Avance

    fecha_aprobacion_f_e = models.DateField()

    inicio_ejecucion_fisica_f_e = models.DateField()
 
    ejecucion_fisica = models.FloatField()

    ejecucion_financiera = models.FloatField()

    ejecutado_anio_anterior = models.DecimalField(max_digits=22,decimal_places=2)
    
    estimado_anio_siguiente = models.DecimalField(max_digits=22,decimal_places=2)

    estimado_anio_ejercicio = models.DecimalField(max_digits=22,decimal_places=2)
    
    # Fields de Ayuda =========================

    duracion = models.DurationField()

    contador = models.IntegerField(default=1)

    def __str__(self):
        return self.codigo
    
    def gen_rest_attrs(self):
        """
        Genera Atributos Restante del Objeto en Instancia.
        >> ("codigo", "contador", "duracion")
        """

        self.duracion = self.fin - self.inicio
        
        result = AccionEspecifica.objects.filter(
            programa=self.programa
        ).aggregate(Max('contador')).get("contador__max")
        
        if result:
            self.contador = result + 1

        self.codigo = self.programa.codigo + "{:02}".format(self.contador)

    class Meta:
        verbose_name_plural = "Acciones Especificas"


class Partida(EmblenBaseModel):
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

    saldo = models.DecimalField(max_digits=22,decimal_places=2,null=True)

    publicacion = models.CharField(max_length=3)

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
        verbose_name_plural = "Partidas"

    def __str__(self):
        return self.cuenta
       

class Estimacion(EmblenBaseModel):

    accion_especifica = models.ForeignKey(
        AccionEspecifica,
        related_name="estimaciones",
        on_delete=models.PROTECT
    )
    
    # Sólo partidas Nivel 2
    partida = models.ForeignKey(
        Partida,
        related_name="estimaciones",
        on_delete=models.PROTECT
    )

    monto = models.DecimalField(max_digits=22,decimal_places=2)
    
    anio = models.CharField(max_length=4)

    class Meta:
        verbose_name_plural = "Estimaciones por Partidas"
        unique_together = (("accion_especifica", "partida", "anio"),)

    def __str__(self):
        return f"{self.accion_especifica} - {self.partida}"
        
    def save(self, *args, **kwargs):
        if self.partida.nivel > 1:
            super(Estimacion, self).save(*args, **kwargs)
        else:
            raise ValueError("La Partida no puede ser de nivel 1")


class TipoGasto(EmblenBaseModel):

    codigo = models.CharField(max_length=2)

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Gastos"


class TipoOrganismo(EmblenBaseModel):

    codigo = models.CharField(max_length=2)

    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Tipos de Organismos"
        

class AccionInterna(EmblenBaseModel):

    NIVELES = (
        (1, "Nivel 1"), # 1000000, 2000000
        (2, "Nivel 2"), # 1070000, 2070000
        (3, "Nivel 3")  # 2070001, 2110001
    )

    codigo = models.CharField(max_length=7)
    
    descripcion = models.TextField()

    accion_especifica = models.ForeignKey(
        AccionEspecifica,
        related_name="acciones_internas",
        on_delete=models.PROTECT
    )

    tipo_gasto = models.ForeignKey(
        TipoGasto,
        related_name="acciones_internas",
        on_delete=models.PROTECT
    )

    nivel = models.IntegerField(choices=NIVELES)

    fuente_financiamiento = models.ForeignKey(
        FuenteFinanciamiento,
        related_name="acciones_internas",
        on_delete=models.PROTECT
    )

    auxiliar = models.IntegerField(default=1)

    transferencia = models.BooleanField(default=False)

    tipo_organismo = models.ForeignKey(
        TipoOrganismo,
        related_name="acciones_internas",
        on_delete=models.PROTECT
    )

    def gen_rest_attrs(self):
        """
        Genera Atributos Restante del Objeto en Instancia.
        >> ("codigo", "auxiliar", "nivel")
        """
        result = AccionInterna.objects.filter(
            accion_especifica=self.accion_especifica
        ).aggregate(Max('auxiliar')).get("auxiliar__max")
        
        if result:
            self.auxiliar = result + 1

        cod_tipo = self.tipo_gasto.codigo
        cod_aux = "{:04}".format(self.auxiliar)
        cod_sector = self.accion_especifica\
                        .programa\
                        .responsable\
                        .unidad_ejecutora\
                        .dependencia\
                        .sector.codigo

        self.codigo = f"{cod_tipo}{cod_sector}{cod_aux}"
        self.nivel = 3

    class Meta:
        verbose_name_plural = "Acciones Internas"


class PartidaAccionInterna(EmblenBaseModel):

    accion_interna = models.ForeignKey(
        AccionInterna,
        related_name="partida_accioninternas",
        on_delete=models.PROTECT
    )

    partida = models.ForeignKey(
        Partida,
        related_name="partida_accioninternas",
        on_delete=models.PROTECT
    )

    anio = models.CharField(max_length=4)

    mto_original = models.DecimalField(max_digits=22,decimal_places=2)

    mto_actualizado = models.DecimalField(max_digits=22,decimal_places=2)

    class Meta:
        verbose_name_plural = "Cuentas - Acciones Internas"
        unique_together = (("accion_interna", "partida", "anio"),)