from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr

from apps.base.models import TimeStampedModel
from django.core.exceptions import NON_FIELD_ERRORS


class Sector(TimeStampedModel):

    codigo = models.CharField(max_length=14)

    nombre = models.CharField(max_length=100)

    descripcion = models.TextField()

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Sectores"


class Dependencia(TimeStampedModel):

    sector = models.ForeignKey(
        Sector,
        related_name="dependencias",
        on_delete=models.CASCADE
    )

    codigo = models.CharField(max_length=14)

    nombre = models.CharField(max_length=100)

    descripcion = models.TextField()

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Dependencias"


class Departamento(TimeStampedModel):

    dependencia = models.ForeignKey(
        Dependencia,
        related_name="departamentos",
        on_delete=models.CASCADE
    )

    codigo = models.CharField(max_length=14)

    nombre = models.CharField(max_length=100)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Departamentos"


class Estado(TimeStampedModel):
    
    codigo = models.CharField(max_length=10)

    nombre = models.CharField(max_length=100)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Estados"


class Municipio(TimeStampedModel):

    estado = models.ForeignKey(
        Estado,
        related_name="municipios",
        on_delete=models.CASCADE
    )

    codigo = models.CharField(max_length=10)

    nombre = models.CharField(max_length=100)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Municipios"


class Parroquia(TimeStampedModel):

    municipio = models.ForeignKey(
        Municipio,
        related_name="parroquias",
        on_delete=models.CASCADE
    )

    codigo = models.CharField(max_length=10)

    nombre = models.CharField(max_length=100)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Parroquias"


class FuenteFinanciamiento(TimeStampedModel):

    codigo = models.CharField(max_length=10)

    nombre = models.CharField(max_length=100)

    orden = models.IntegerField()

    externo=models.BooleanField(default=False)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Fuentes de Financiamientos"


class CentroCosto(TimeStampedModel):

    codigo = models.CharField(max_length=10)

    nombre = models.CharField(max_length=100)

    nivel = models.IntegerField()

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Centros de Costos"


class UnidadEjecutora(TimeStampedModel):

    dependencia = models.ForeignKey(
        Dependencia,
        related_name="unidadejecutoras",
        on_delete=models.CASCADE
    )

    codigo = models.CharField(max_length=10)

    nombre = models.CharField(max_length=100)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Unidades Ejecutoras"


class SectorDesarrollador(TimeStampedModel):
    
    codigo = models.CharField(max_length=3)

    nombre = models.CharField(max_length=100)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Sectores Desarrolladores"


class UnidadMedida(TimeStampedModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)

    dimension = models.IntegerField()

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Unidades de Medidas"


class TipoBeneficiario(TimeStampedModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Tipos de Beneficiarios"


class PeriodoActualizacion(TimeStampedModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Periodos de Actualizacion"


class CondicionPrograma(TimeStampedModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)  #Formulado - Banco de Proyectos

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Condiciones de los Programas"


class Programa(TimeStampedModel):

    dependencia = models.ForeignKey(
        Dependencia,
        related_name="programas",
        on_delete=models.CASCADE
    )

    periodo_actualizacion = models.ForeignKey(
        PeriodoActualizacion,
        related_name="programas",
        on_delete=models.CASCADE
    )

    # Información Básica

    anio = models.CharField(max_length=4)

    codigo = models.CharField(max_length=11)

    nivel = models.IntegerField() #3 o 4

    detallada = models.TextField()

    condicion = models.ForeignKey(
        CondicionPrograma,
        related_name="programas",
        on_delete=models.CASCADE
    )

    estado = models.CharField(max_length=3) #INI -

    sector_desarrollador = models.ForeignKey(
        SectorDesarrollador,
        related_name="programas",
        on_delete=models.CASCADE
    )

    plan_inversion_social = models.BooleanField(default=False)

    inicio = models.DateTimeField()

    fin = models.DateTimeField()

    # =======================================================

    # Responsables
    
    ente_responsable = models.ForeignKey(
        UnidadEjecutora,
        related_name="programas",
        on_delete=models.CASCADE
    )

    adscrito = models.ForeignKey(
        UnidadEjecutora,
        related_name="programas",
        on_delete=models.CASCADE
    )    

    responsable = models.ForeignKey(
        Departamento,
        related_name="programas",
        on_delete=models.CASCADE
    ) 

    # =======================================================

    # Ubicación

    extension_territorial = models.BooleanField(default=True)

    parroquia = models.ForeignKey(
        Parroquia,
        related_name="programas",
        on_delete=models.CASCADE
    )

    # =======================================================
    
    # Objetivos

    desarrollo_sostenible = models.TextField()

    estrategico = models.TextField()

    problematica = models.TextField()

    especifico = models.TextField()

    resumen = models.TextField()   

    # =======================================================

    # Resultado Esperados -> AQUI QUEDÉ

    bien_servicio = models.TextField()

    unidad_medida = models.ForeignKey(
        UnidadMedida,
        related_name="programas",
        on_delete=models.CASCADE
    )

    indicador_situacion = models.TextField()

    indicador_fuente = models.TextField()

    indicador_formula = models.TextField()

    indicador_objetivo = models.TextField()

    # =======================================================

    # Distribución Meta Física Trimestral
    trimestre_1 = models.DecimalField(max_digits=22,decimal_places=4)
    trimestre_2 = models.DecimalField(max_digits=22,decimal_places=4)
    trimestre_3 = models.DecimalField(max_digits=22,decimal_places=4)
    trimestre_4 = models.DecimalField(max_digits=22,decimal_places=4)
    
    # =======================================================

    # Beneficiarios

    tipo_beneficiario = models.ForeignKey(
        TipoBeneficiario,
        related_name="programas",
        on_delete=models.CASCADE
    )

    distincion_genero = models.BooleanField(default=True)

    beneficiario_masculino = models.IntegerField()

    beneficiario_femenino = models.IntegerField()
    

    # =======================================================

    # Empleos Generados

    directo_masculino = models.IntegerField()

    directo_femenino = models.IntegerField()
    
    indirecto_masculino = models.IntegerField()
    
    indirecto_femenino = models.IntegerField()

    # =======================================================

    # Porcentaje Avance

    ejecucion_fisica = models.DecimalField(max_digits=22,decimal_places=4)

    ejecucion_financiera = models.DecimalField(max_digits=22,decimal_places=4)

    # =======================================================

    class Meta:
        verbose_name_plural = "Programas"


class LineaPlan(TimeStampedModel):
    
    codigo = models.CharField(max_length=5)

    descripcion = models.TextField()

    tipo = models.CharField(max_length=1) #N = Nacional - E = Estadal 

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Lineas del Plan"


class LineaPrograma(TimeStampedModel):
    
    codigo = models.CharField(max_length=5)

    programa = models.ForeignKey(
        Programa,
        related_name="lineas_programas",
        on_delete=models.CASCADE
    )

    historico = models.ForeignKey(
        LineaPlan,
        related_name="lineas_programas",
        on_delete=models.CASCADE
    )

    nacional = models.TextField()
    
    estrategico = models.TextField()
    
    general = models.TextField()

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Lineas del Programa"


class PlanDesarrollo(TimeStampedModel):
    
    codigo = models.CharField(max_length=5)

    programa = models.ForeignKey(
        Programa,
        related_name="plan_desarrollos",
        on_delete=models.CASCADE
    )

    dimension = models.ForeignKey(
        LineaPlan,
        related_name="plan_desarrollos",
        on_delete=models.CASCADE
    )

    plan_metas = models.TextField()
    
    metas = models.TextField()
    
    solucion = models.TextField()

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Planes de Desarrollo"


class AreaInversion(TimeStampedModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Areas de Inversion"


class CategoriaAreaInversion(TimeStampedModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)

    area_inversion = models.ForeignKey(
        AreaInversion,
        related_name="categoria_area_inversion",
        on_delete=models.CASCADE
    )

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Categorias de las Areas de Inversion"


class EstatusFinanciamientoExterno(TimeStampedModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Estatus de Financiamientos Externos"


class TipoAreaInversion(TimeStampedModel):
    
    codigo = models.CharField(max_length=5)

    nombre = models.CharField(max_length=100)

    categoria = models.ForeignKey(
        CategoriaAreaInversion,
        related_name="tipo_area_inversion",
        on_delete=models.CASCADE
    )

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Tipos de Areas de Inversion"
        

class AccionEspecifica(TimeStampedModel):

    programa = models.ForeignKey(
        Programa,
        related_name="acciones_especificas",
        on_delete=models.CASCADE
    )

   # Información Básica

    codigo = models.CharField(max_length=11)

    condicion = models.CharField(max_length=20) #Formulado - Banco de Proyectos

    descripcion = models.TextField()

    detallada = models.TextField()

    especifico = models.TextField()

    # sectordesarrollador = models.ForeignKey(
    #     SectorDesarrollador,
    #     related_name="sectordesarrollador_accion_especificas",
    #     on_delete=models.CASCADE
    # )

    inicio = models.DateTimeField()

    fin = models.DateTimeField()

    impacto_social = models.TextField()

    articulacion = models.TextField()

    vinculacion = models.BooleanField(default=True)

    financiamiento_externo = models.BooleanField(default=False)

    bien_servicio = models.TextField()
    
    # =======================================================

    # Beneficiarios

    tipo_beneficiario = models.ForeignKey(
        TipoBeneficiario,
        related_name="acciones_especificas",
        on_delete=models.CASCADE
    )

    distincion_genero = models.BooleanField(default=True)

    beneficiario_masculino = models.IntegerField()

    beneficiario_femenino = models.IntegerField()
    
    # =======================================================

    # Empleos Generados

    directo_masculino = models.IntegerField()

    directo_femenino = models.IntegerField()
    
    indirecto_masculino = models.IntegerField()
    
    indirecto_femenino = models.IntegerField()

    # =======================================================

    # Responsables
    
    # enteresponsable = models.ForeignKey(
    #     UnidadEjecutora,
    #     related_name="enteresponsable_accion_especificas",
    #     on_delete=models.CASCADE
    # )

    # adscrito = models.ForeignKey(
    #     UnidadEjecutora,
    #     related_name="adscrito_accion_especificas",
    #     on_delete=models.CASCADE
    # )    

    responsable = models.ForeignKey(
        Departamento,
        related_name="acciones_especificas",
        on_delete=models.CASCADE
    ) 

    # =======================================================

    # Metas Físicas

    extension_territorial = models.BooleanField(default=True)

    parroquia = models.ForeignKey(
        Parroquia,
        related_name="acciones_especificas",
        on_delete=models.CASCADE
    )

    sector = models.ForeignKey(
        SectorDesarrollador,
        related_name="acciones_especificas",
        on_delete=models.CASCADE
    )

    plazo_ejecucion = models.IntegerField()

    unidad_medida = models.ForeignKey(
        UnidadMedida,
        related_name="acciones_especificas",
        on_delete=models.CASCADE
    )

    # =======================================================

    # Distribución Física Trimestral
    trimestre_1 = models.DecimalField(max_digits=22,decimal_places=4)
    trimestre_2 = models.DecimalField(max_digits=22,decimal_places=4)
    trimestre_3 = models.DecimalField(max_digits=22,decimal_places=4)
    trimestre_4 = models.DecimalField(max_digits=22,decimal_places=4)

    # =======================================================

    # Estimacion Financiera por partida

    estimado_401 = models.DecimalField(max_digits=22,decimal_places=4)
    estimado_402 = models.DecimalField(max_digits=22,decimal_places=4)
    estimado_403 = models.DecimalField(max_digits=22,decimal_places=4)
    estimado_404 = models.DecimalField(max_digits=22,decimal_places=4)
    estimado_405 = models.DecimalField(max_digits=22,decimal_places=4)
    estimado_407 = models.DecimalField(max_digits=22,decimal_places=4)
    estimado_408 = models.DecimalField(max_digits=22,decimal_places=4)
    estimado_411 = models.DecimalField(max_digits=22,decimal_places=4)
    estimado_498 = models.DecimalField(max_digits=22,decimal_places=4)

    # =======================================================

    # Fuente Financimiento Externo

    estatus_financiamiento_externo = models.ForeignKey(
        EstatusFinanciamientoExterno,
        related_name="acciones_especificas",
        on_delete=models.CASCADE
    )

    # areainversion = models.ForeignKey(
    #     AreaInversion,
    #     related_name="areainversion_acciones_especificas",
    #     on_delete=models.CASCADE
    # )

    # catareainv = models.ForeignKey(
    #     CategoriaAreaInversion,
    #     related_name="catareainv_acciones_especificas",
    #     on_delete=models.CASCADE
    # )

    tipo_area_inversion = models.ForeignKey(
        TipoAreaInversion,
        related_name="acciones_especificas",
        on_delete=models.CASCADE
    )

    fase = models.CharField(max_length=100)

    # =======================================================

    # Porcentaje Avance

    fecha_aprobacion_f_e = models.DateTimeField()

    inicio_ejecucion_fisica_f_e = models.DateTimeField()
 
    ejecucion_fisica = models.DecimalField(max_digits=22,decimal_places=4)

    ejecucion_financiera = models.DecimalField(max_digits=22,decimal_places=4)

    ejecutado_anio_anterior = models.DecimalField(max_digits=22,decimal_places=4)
    
    estimado_anio_siguiente = models.DecimalField(max_digits=22,decimal_places=4)

    estimado_anio_ejercicio = models.DecimalField(max_digits=22,decimal_places=4)

    # =======================================================

    class Meta:
        verbose_name_plural = "Acciones Especificas"


class Partida(TimeStampedModel):
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

    descripcion = models.TextField()

    nivel = models.IntegerField()

    saldo = models.DecimalField(max_digits=22,decimal_places=4,null=True)

    estatus = models.BooleanField(default=True)

    def sin_ceros(self):
        """Retorna la cuenta sin ceros a la derecha"""
        return self.cuenta[0:self.NIVELES[self.nivel]]

    def siguientes(self):
        """Devuelve queryset de las partidas hijas del nivel siguiente"""
        debe_comenzar = self.sin_ceros() 
        siguiente_nivel = self.nivel + 1

        return Partida.objects.filter(
            nivel=siguiente_nivel, 
            cuenta__startswith=debe_comenzar
        )
        
    class Meta:
        ordering = ('-creado',),
        verbose_name_plural = "Programas"

    def __str__(self):
        return self.cuenta
       

class Estimacion(TimeStampedModel):

    accion_especifica = models.ForeignKey(
        AccionEspecifica,
        related_name="estimaciones",
        on_delete=models.CASCADE
    )
    
    # Sólo partidas Nivel 2

    partida = models.ForeignKey(
        Partida,
        related_name="estimaciones",
        on_delete=models.CASCADE
    )

    monto = models.DecimalField(max_digits=22,decimal_places=4)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Estimaciones por Partidas"


class TipoGasto(TimeStampedModel):

    codigo = models.CharField(max_length=2)

    nombre = models.CharField(max_length=100)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Tipos de Gasto"


class TipoOrganismo(TimeStampedModel):

    codigo = models.CharField(max_length=2)

    nombre = models.CharField(max_length=100)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Tipos de Organismos"
        

class AccionInterna(TimeStampedModel):

    codigo = models.CharField(max_length=11)

    # anio = models.CharField(max_length=4)
    
    descripcion = models.TextField()

    accion_especifica = models.ForeignKey(
        AccionEspecifica,
        related_name="acciones_internas",
        on_delete=models.CASCADE
    )

    tipo_gasto = models.ForeignKey(
        TipoGasto,
        related_name="acciones_internas",
        on_delete=models.CASCADE
    )

    nivel = models.CharField(max_length=1) # 1 = 1000000, 2000000 - 2 = 1070000, 2070000, 2110000 - 3 = 1070001, 2070001, 2110001

    fuente_financiamiento = models.ForeignKey(
        FuenteFinanciamiento,
        related_name="acciones_internas",
        on_delete=models.CASCADE
    )

    auxiliar = models.CharField(max_length=4)

    transferencia = models.BooleanField(default=False)

    tipo_organismo = models.ForeignKey(
        TipoOrganismo,
        related_name="acciones_internas",
        on_delete=models.CASCADE
    )

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Acciones Internas"

class CCostoAccInt(TimeStampedModel):

    centro_costo = models.ForeignKey(
        CentroCosto,
        related_name="ccosto_accint",
        on_delete=models.CASCADE
    )

    accion_interna = models.ForeignKey(
        AccionInterna,
        related_name="ccosto_accint",
        on_delete=models.CASCADE
    )

    anio = models.CharField(max_length=4)

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Centros de Costos - Acciones Internas"


class CtasCCostoAInt(TimeStampedModel):

    ccosto_accint = models.ForeignKey(
        CCostoAccInt,
        related_name="ctas_ccosto_aint",
        on_delete=models.CASCADE
    )

    partida = models.ForeignKey(
        Partida,
        related_name="ctas_ccosto_aint",
        on_delete=models.CASCADE
    )

    anio = models.CharField(max_length=4)

    mto_original = models.DecimalField(max_digits=22,decimal_places=4)

    mto_actualizado = models.DecimalField(max_digits=22,decimal_places=4)
    
    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Cuentas - Centros de Costos - Acciones Internas",
        unique_together = (("ccosto_accint", "partida", "anio"),)
>>>>>>> e5739afc86d30ed3fab46e9e4bd1d887ca5b28fe
