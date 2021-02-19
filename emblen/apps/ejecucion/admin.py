from django.contrib import admin

from apps.ejecucion import models


admin.site.register(models.TipoOrdenPago) 

admin.site.register(models.ClaseOrdenPago) 

admin.site.register(models.TipoDocumento) 

admin.site.register(models.DocumentoPagar) 

admin.site.register(models.OrdenPago)

admin.site.register(models.DeduccionOrdenPago)

admin.site.register(models.DetalleOrdenPago)    