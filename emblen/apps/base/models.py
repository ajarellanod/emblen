from django.db import models

from apps.base.shortcuts import softdelete_by_object

class EmblenQuerySet(models.QuerySet):
    def eliminar(self):
        self.update(eliminado=True)

class EmblenManager(models.Manager):
    use_for_related_fields = True

    def todos(self):
        return EmblenQuerySet(self.model, using=self._db)

    def eliminados(self):
        return self.todos().filter(eliminado=True)

    def get_queryset(self):
        return self.todos().exclude(eliminado=True)


class EmblenBaseModel(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    eliminado = models.BooleanField(default=False, editable=False)
    
    class Meta:
        abstract = True

    def eliminar(self):
        self.eliminado = True
        self.save()

    def eliminar_relaciones(self):
        softdelete_by_object(self)

    objects = EmblenManager()