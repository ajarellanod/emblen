from django.contrib import admin

from apps.compras import models


admin.site.register(models.TipoBeneficiario)

admin.site.register(models.Beneficiario)

admin.site.register(models.TipoDocumento)

admin.site.register(models.DocumentoPagar)

admin.site.register(models.DetalleDocumentoPagar)

admin.site.register(models.TipoContrato)

admin.site.register(models.Contrato)

admin.site.register(models.BeneficiarioContrato)

admin.site.register(models.ContratoPartida)

admin.site.register(models.AnticipoContrato)

admin.site.register(models.ValuacionContrato)

admin.site.register(models.TipoOrden)

admin.site.register(models.Orden)

admin.site.register(models.Compromiso)