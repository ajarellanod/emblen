from django.db import models

# Create your models here.
from django.utils import timezone
from django.contrib.auth.models import User

class Partida(models.Model):
    Opcs_Estatus= (
        ('1', 'Activo'),
        ('0', 'Inactivo'),
    )
    cuenta = models.CharField(max_length=14)
    descripcion = models.TextField()
    nivel = models.CharField(max_length=1)
    saldo = models.FloatField()
    fecha_c = models.DateTimeField(auto_now_add=True)
    estatus = models.CharField(max_length=1,
                              choices=Opcs_Estatus,
                              default='1')
    class Meta:
        ordering = ('-fecha_c',)

    def __str__(self):
        return self.descripcion