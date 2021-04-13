from django.contrib import admin

from apps.ejecucion import models


admin.site.register(models.TipoOrdenPago) 

admin.site.register(models.ClaseOrdenPago) 

admin.site.register(models.OrdenPago)

admin.site.register(models.AfectacionPresupuestaria)

admin.site.register(models.AfectacionContrato)