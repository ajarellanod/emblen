from django.urls import path

from apps.formulacion import views

urlpatterns = [
        path("formulacion/", views.FormulacionView.as_view(), name="formulacion"),
        path("formulacion/partidas", views.PartidaView.as_view(), name="formulacionPartidas"),
        path('formulacion/<pk>/update', views.PartidaUpdateView.as_view(), name="update_partida"),
        path('formulacion/<pk>/delete', views.PartidaDeleteView.as_view(), name="delete_partida"),
]