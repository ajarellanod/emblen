from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db.models.functions import Substr

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
        """
        Devuelve queryset de las partidas hijas del nivel siguiente
        """

        debe_comenzar = self.sin_ceros() 

        siguiente_nivel = self.nivel + 1

        return Partida.objects.filter(
            nivel=siguiente_nivel, cuenta__startswith=debe_comenzar
        )
        

    class Meta:
        ordering = ('-creado',)


    def __str__(self):
        return self.cuenta