from django.contrib import admin

from .models import (
    TipoModificacion,
    Modificacion,
    AcumuladosPresupuestario
)

# Register your models here.
admin.site.register(TipoModificacion)
admin.site.register(Modificacion)
admin.site.register(AcumuladosPresupuestario)