from django.contrib import admin

from .models import (
    TipoModificacion,
    ModificacionIngreso,
    ModificacionGasto,
    AcumuladosPresupuestario
)

# Register your models here.
admin.site.register(TipoModificacion)
admin.site.register(ModificacionIngreso)
admin.site.register(ModificacionGasto)
admin.site.register(AcumuladosPresupuestario)