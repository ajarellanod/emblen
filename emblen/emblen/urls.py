from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.formulacion.urls', 'apps.formulacion'), namespace="formulacion")),
    path('', include(('apps.usuarios.urls', 'apps.usuarios'), namespace="usuarios")),
]
