from django.urls import path

from apps.formulacion import views

urlpatterns = [
        path("formulacion/", views.formulacion.partida_lista, name="partida_lista"),
]