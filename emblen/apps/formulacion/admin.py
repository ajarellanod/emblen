from django.contrib import admin

from apps.formulacion import models


admin.site.register(models.Sector)

admin.site.register(models.Dependencia)

admin.site.register(models.Departamento)

admin.site.register(models.Proyecto)

admin.site.register(models.AccionEspecifica)

admin.site.register(models.Partida)