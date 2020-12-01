from django.db import models

class TimeStampedModel(models.Model):
    """
    Una clase abstracta que provee un ``creado`` y ``modificado`` automaticamente.
    """
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True