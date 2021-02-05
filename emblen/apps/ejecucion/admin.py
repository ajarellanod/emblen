from django.contrib import admin

from apps.ejecucion import models


admin.site.register(models.TiposOrdenPago)

admin.site.register(models.OrdenesPago)

admin.site.register(models.Deduccion)

admin.site.register(models.DetallesOrdenesPago)

