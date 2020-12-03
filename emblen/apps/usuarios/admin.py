from django.contrib import admin

from apps.usuarios import models


admin.site.register(models.Perfil)

@admin.register(models.Rol)
class RolAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')