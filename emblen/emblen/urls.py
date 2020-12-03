from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.formulacion.urls')),
    path('', include(('apps.usuarios.urls', 'apps.usuarios'), namespace="usuarios")),
]
