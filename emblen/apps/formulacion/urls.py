from django.urls import path

from apps.formulacion import views

urlpatterns = [
    path("", views.PrincipalView.as_view(), name="principal"),
    path("partidas/", views.PartidaListView.as_view(), name="partidas"),
    path('partida/crear/', views.PartidaCreateView.as_view(), name="crear_partida"),
    path('partida/<pk>/', views.PartidaView.as_view(), name="ver_partida"),
    path('partida/<pk>/eliminar/', views.PartidaDeleteView.as_view(), name="eliminar_partida"),
    path('departamento/crear/', views.DepartamentoCreateView.as_view(), name="crear_departamento"),
    path('departamento/<pk>/', views.DepartamentoView.as_view(), name="ver_departamento"),
    path("departamentos/", views.DepartamentoListView.as_view(), name="departamentos"),
    path('departamento/<pk>/eliminar/', views.DepartamentoDeleteView.as_view(), name="eliminar_departamento"),
]