from django.urls import path

from apps.formulacion import views

urlpatterns = [
    path("", views.PrincipalView.as_view(), name="principal"),
    path("partidas/", views.PartidaListView.as_view(), name="partidas"),
    path('partida/crear/', views.PartidaCreateView.as_view(), name="crear_partida"),
    path('partida/<pk>/', views.PartidaView.as_view(), name="ver_partida"),
    path('partida/<pk>/eliminar/', views.PartidaDeleteView.as_view(), name="eliminar_partida"),
]