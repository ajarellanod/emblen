from django.contrib import admin

# Register your models here.

from apps.nucleo import models


admin.site.register(models.Publicacion)

admin.site.register(models.MovimientoGasto)
