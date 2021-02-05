from django.contrib import admin

from apps.compras import models


admin.site.register(models.TiposBeneficiario)

admin.site.register(models.Beneficiario)

admin.site.register(models.Compromiso)
