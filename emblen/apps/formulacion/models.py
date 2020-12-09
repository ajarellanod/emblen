from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

from apps.base.models import TimeStampedModel
from django.core.exceptions import NON_FIELD_ERRORS


class Sector(models.Model):

    codigo = models.CharField(max_length=14)

    descripcion = models.TextField()

    estatus = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Sectores"


class Dependencia(models.Model):

    sector = models.ForeignKey(
        Sector,
        related_name="dependencias",
        on_delete=models.CASCADE
    )

    codigo = models.CharField(max_length=14)

    descripcion = models.TextField()

    estatus = models.BooleanField(default=True)


class Departamento(models.Model):

    dependencia = models.ForeignKey(
        Dependencia,
        related_name="departamentos",
        on_delete=models.CASCADE
    )

    codigo = models.CharField(max_length=14)

    descripcion = models.TextField()

    nivel = models.IntegerField()

    estatus = models.BooleanField(default=True)


class Proyecto(TimeStampedModel):

    dependencia = models.ForeignKey(
        Dependencia,
        related_name="proyectos",
        on_delete=models.CASCADE
    )

    ano = models.CharField(max_length=4)

    codigo = models.CharField(max_length=14)

    resumen = models.CharField(max_length=500)

    descripcion = models.TextField()

    inicio = models.DateTimeField()

    fin = models.DateTimeField()

    objetivo_historico = models.TextField()

    objetivo_nacional = models.TextField()

    objetivo_estrategico = models.TextField()

    objetivo_general = models.TextField()

    problema = models.TextField()

    codigo_estado = models.CharField(max_length=14)

    codigo_municipio = models.CharField(max_length=14)

    codigo_parroquia = models.CharField(max_length=14)


class AccionEspecifica(TimeStampedModel):

    proyecto = models.ForeignKey(
        Proyecto,
        related_name="acciones_especificas",
        on_delete=models.CASCADE
    )

    codigo = models.CharField(max_length=14)

    resumen = models.CharField(max_length=500)

    descripcion = models.TextField()

    inicio = models.DateTimeField()

    fin = models.DateTimeField()

    objetivo_historico = models.TextField()

    objetivo_nacional = models.TextField()

    objetivo_estrategico = models.TextField()

    objetivo_general = models.TextField()

    problema = models.TextField()

    class Meta:
        verbose_name_plural = "Acciones Especificas"


class Partida(TimeStampedModel):
    """ 
    Almanecena las partidas presupuestarias de Recursos y Egresos.
    """
    
    NIVELES = {
        1: 0,
        2: 3,
        3: 5,
        4: 7,
        5: 9,
        6: 11,
        7: 14
    }
    
    cuenta = models.CharField(max_length=14,unique=True)

    descripcion = models.TextField()

    nivel = models.IntegerField()

    saldo = models.DecimalField(max_digits=22,decimal_places=4,null=True)

    estatus = models.BooleanField(default=True)

    @staticmethod
    def obten_hijos(pk):
        
        # First query
        principal_object = Partida.objects.filter(pk=pk).first()
        
        # Resolving the information
        must_start = principal_object.cuenta[0:Partida.NIVELES[principal_object.nivel]]
        nivel = principal_object.nivel + 1
        
        # Getting the correct info
        related_objects = Partida.objects.filter(nivel=nivel, cuenta__startswith=must_start)
        
        return related_objects
        

    class Meta:
        ordering = ('-creado',)

    def __str__(self):
        return self.descripcion