from django.urls import path

from apps.formulacion import views, reports

urlpatterns = [
    path('', views.PrincipalView.as_view(), name='principal'),

    path('partidas/', views.PartidaListView.as_view(), name='partidas'),
    path('partida/crear/', views.PartidaCreateView.as_view(), name='c_partida'),
    path('partida/<int:pk>/', views.PartidaView.as_view(), name='v_partida'),
    path('partida/<int:pk>/eliminar/', views.PartidaDeleteView.as_view(), name='e_partida'),

    path('departamento/crear/', views.DepartamentoCreateView.as_view(), name='c_departamento'),
    path('departamento/<int:pk>/', views.DepartamentoView.as_view(), name='v_departamento'),
    path('departamentos/', views.DepartamentoListView.as_view(), name='departamentos'),
    path('departamento/<int:pk>/eliminar/', views.DepartamentoDeleteView.as_view(), name='e_departamento'),
    
    path('unidades-ejecutoras/', views.UnidadEjecutoraListView.as_view(), name='unidades_ejecutoras'),
    path('unidad-ejecutora/crear/', views.UnidadEjecutoraCreateView.as_view(), name='c_unidad_ejecutora'),
    path('unidad-ejecutora/<int:pk>/', views.UnidadEjecutoraView.as_view(), name='v_unidad_ejecutora'),
    path('unidad-ejecutora/<int:pk>/eliminar/', views.UnidadEjecutoraDeleteView.as_view(), name='e_unidad_ejecutora'),

    path('centros-costos/', views.CentroCostoListView.as_view(), name='centros_costos'),
    path('centro-costo/crear/', views.CentroCostoCreateView.as_view(), name='c_centro_costo'),
    path('centro-costo/<int:pk>/', views.CentroCostoView.as_view(), name='v_centro_costo'),
    path('centro-costo/<int:pk>/eliminar/', views.CentroCostoDeleteView.as_view(), name='e_centro_costo'),

    path('programas/', views.ProgramaListView.as_view(), name='programas'),
    path('programa/<int:pk>/', views.ProgramaView.as_view(), name='v_programa'),
    path('programa/crear/', views.ProgramaCreateView.as_view(), name='c_programa'),
    path('programa/<int:pk>/eliminar/', views.ProgramaDeleteView.as_view(), name='e_programa'),

    path('acciones-especificas/', views.AccionEspecificaListView.as_view(), name='acciones_especificas'),
    path('accion-especifica/<int:pk>/', views.AccionEspecificaView.as_view(), name='v_accion_especifica'),
    path('accion-especifica/crear/', views.AccionEspecificaCreateView.as_view(), name='c_accion_especifica'),
    path('accion-especifica/<int:pk>/eliminar/', views.AccionEspecificaDeleteView.as_view(), name='e_accion_especifica'),

    path('estimacion/', views.EstimacionView.as_view(), name='estimacion'),
    path('estimacion/<int:pk>', views.Estimacion2View.as_view(), name='estimacion2'),
    path('estimacion/<int:pk>/eliminar/', views.EstimacionDeleteView.as_view(), name='e_estimacion'),

    path('acciones-internas/', views.AccionInternaListView.as_view(), name='acciones_internas'),
    path('accion-interna/<int:pk>/', views.AccionInternaView.as_view(), name='v_accion_interna'),
    path('accion-interna/crear/', views.AccionInternaCreateView.as_view(), name='c_accion_interna'),
    path('accion-interna/<int:pk>/eliminar/', views.AccionInternaDeleteView.as_view(), name='e_accion_interna'),


    path('partida-accion-interna/', views.PartidaAccionInternaView.as_view(), name='partida_accion_interna'),
    path('partida-accion-interna/<int:pk>', views.PartidaAccionInternaEspecificaView.as_view(), name='partida_accion_interna_especifica'),
    path('partida-accion-interna/<int:pk>/eliminar/', views.PartidaAccionInternaDeleteView.as_view(), name='e_partida_accion_interna'),

    path('ingresos/', views.IngresoListView.as_view(), name='ingresos'),
    path('ingreso/<int:pk>', views.IngresoView.as_view(), name='v_ingreso'),
    path('ingreso/crear/', views.IngresoCreateView.as_view(), name='c_ingreso'),
    path('ingreso/<int:pk>/eliminar/', views.IngresoDeleteView.as_view(), name='e_ingreso'),

    path('lineas-programas/', views.LineaProgramaListView.as_view(), name='lineas_programas'),
    path('linea-programa/<int:pk>/', views.LineaProgramaView.as_view(), name='v_linea_programa'),
    path('linea-programa/crear/', views.LineaProgramaCreateView.as_view(), name='c_linea_programa'),
    path('linea-programa/<int:pk>/eliminar/', views.LineaProgramaDeleteView.as_view(), name='e_linea_programa'),

    
    path('planes-desarrollos/', views.PlanDesarrolloListView.as_view(), name='planes_desarrollo'),
    path('plan-desarrollo/<int:pk>/', views.PlanDesarrolloView.as_view(), name='v_plan_desarrollo'),
    path('plan-desarrollo/', views.PlanDesarrolloCreateView.as_view(), name='c_plan_desarrollo'),
    path('plan-desarrollo/<int:pk>/eliminar/', views.PlanDesarrolloDeleteView.as_view(), name='e_plan_desarrollo'),

    path('ejercicios-presupuestarios/', views.EjercicioPresupuestarioListView.as_view(), name='ejercicios_presupuestarios'),
    path('ejercicio-presupuestario/<int:pk>/', views.EjercicioPresupuestarioView.as_view(), name='v_ejercicio_presupuestario'),
    path('ejercicio-presupuestario/crear/', views.EjercicioPresupuestarioCreateView.as_view(), name='c_ejercicio_presupuestario'),
    path('ejercicio-presupuestario/<int:pk>/eliminar/', views.EjercicioPresupuestarioDeleteView.as_view(), name='e_ejercicio_presupuestario'),
]


urlreports = [
    path('r/creditos-asigandos/', reports.CreditosAsignadosReport.as_view(), name='re_creditos_asigandos'),
]


urlpatterns += urlreports