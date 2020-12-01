from django.urls import path

from apps.usuarios import views

urlpatterns = [
    path("inicio/", views.InicioSesion.as_view(), name="inicio"),
]