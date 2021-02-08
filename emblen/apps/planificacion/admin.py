from django.contrib import admin

from .models import (
    TiposDocumento,
    Documento,
    AcumuladosPresupuestario
)

# Register your models here.
admin.site.register(TiposDocumento)
admin.site.register(Documento)
admin.site.register(AcumuladosPresupuestario)