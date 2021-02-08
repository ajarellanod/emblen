from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('apps.usuarios.urls', 'apps.usuarios'), namespace="usuarios")),
    path('formulacion/', include(('apps.formulacion.urls', 'apps.formulacion'), namespace="formulacion")),
    path('planificacion/', include(('apps.planificacion.urls', 'apps.planificacion'), namespace="planificacion")),
    path('ejecucion/', include(('apps.ejecucion.urls', 'apps.ejecucion'), namespace="ejecucion")),
    path('contabilidad/', include(('apps.contabilidad.urls', 'apps.contabilidad'), namespace="contabilidad")),
    path('compras/', include(('apps.compras.urls', 'apps.compras'), namespace="compras")),
    path('tesoreria/', include(('apps.tesoreria.urls', 'apps.tesoreria'), namespace="tesoreria")),
]
