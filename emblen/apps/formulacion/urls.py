from django.urls import path

from apps.formulacion import views, reports

urlpatterns = [
    path("", views.PrincipalView.as_view(), name="principal"),

    path("partidas/", views.PartidaListView.as_view(), name="partidas"),
    path('partida/crear/', views.PartidaCreateView.as_view(), name="c_partida"),
    path('partida/<pk>/', views.PartidaView.as_view(), name="v_partida"),
    path('partida/<pk>/eliminar/', views.PartidaDeleteView.as_view(), name="e_partida"),

    path('departamento/crear/', views.DepartamentoCreateView.as_view(), name="c_departamento"),
    path('departamento/<pk>/', views.DepartamentoView.as_view(), name="v_departamento"),
    path("departamentos/", views.DepartamentoListView.as_view(), name="departamentos"),
    path('departamento/<pk>/eliminar/', views.DepartamentoDeleteView.as_view(), name="e_departamento"),
    
    path("unidades-ejecutoras/", views.UnidadEjecutoraListView.as_view(), name="unidades_ejecutoras"),
    path('unidad-ejecutora/crear/', views.UnidadEjecutoraCreateView.as_view(), name="c_unidad_ejecutora"),
    path('unidad-ejecutora/<pk>/', views.UnidadEjecutoraView.as_view(), name="v_unidad_ejecutora"),
    path('unidad-ejecutora/<pk>/eliminar/', views.UnidadEjecutoraDeleteView.as_view(), name="e_unidad_ejecutora"),

    path("centros-costos/", views.CentroCostoListView.as_view(), name="centros_costos"),
    path('centro-costo/crear/', views.CentroCostoCreateView.as_view(), name="c_centro_costo"),
    path('centro-costo/<pk>/', views.CentroCostoView.as_view(), name="v_centro_costo"),
    path('centro-costo/<pk>/eliminar/', views.CentroCostoDeleteView.as_view(), name="e_centro_costo"),

    path('programa/<int:pk>/', views.ProgramaView.as_view(), name="v_programa"),
    path('programa/crear/', views.ProgramaCreateView.as_view(), name="c_programa"),
]