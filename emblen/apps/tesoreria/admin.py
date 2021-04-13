from django.contrib import admin

from apps.tesoreria import models


admin.site.register(models.Banco)

admin.site.register(models.TipoCuenta)

admin.site.register(models.Cuenta)

admin.site.register(models.CuentaBeneficiario)

admin.site.register(models.TipoImpuesto)

admin.site.register(models.ImpuestoBeneficiario)

admin.site.register(models.ImpuestoContrato)

admin.site.register(models.Pago)

admin.site.register(models.RetencionDeduccion)
