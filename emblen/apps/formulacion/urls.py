from django.urls import path

from apps.formulacion import views

urlpatterns = [
    path("", views.PrincipalView.as_view(), name="principal"),
    path("partidas/", views.PartidaView.as_view(), name="partidas"),
    path('partidas/<pk>/actualizar/', views.PartidaUpdateView.as_view(), name="actualizar_partida"),
    path('partidas/<pk>/eliminar/', views.PartidaDeleteView.as_view(), name="eliminar_partida"),
]