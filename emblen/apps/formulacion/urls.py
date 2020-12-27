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
    
    path("unidades-ejecutoras/", views.UnidadEjecutoraListView.as_view(), name="unidades_ejecutoras"),
    path('unidad-ejecutora/crear/', views.UnidadEjecutoraCreateView.as_view(), name="crear_unidad_ejecutora"),
    path('unidad-ejecutora/<pk>/', views.UnidadEjecutoraView.as_view(), name="ver_unidad_ejecutora"),
    path('unidad-ejecutora/<pk>/eliminar/', views.UnidadEjecutoraDeleteView.as_view(), name="eliminar_unidad_ejecutora"),

    path("centros-costos/", views.CentroCostoListView.as_view(), name="centros_costos"),
    path('centro-costo/crear/', views.CentroCostoCreateView.as_view(), name="crear_centro_costo"),
    path('centro-costo/<pk>/', views.CentroCostoView.as_view(), name="ver_centro_costo"),
    path('centro-costo/<pk>/eliminar/', views.CentroCostoDeleteView.as_view(), name="eliminar_centro_costo"),
]