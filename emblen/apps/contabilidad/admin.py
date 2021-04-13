from django.contrib import admin

from apps.contabilidad import models


admin.site.register(models.CuentaContable)

admin.site.register(models.AsientoContable)