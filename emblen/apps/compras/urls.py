from django.urls import path

from apps.compras import views, reports

urlpatterns = [
    path('', views.PrincipalView.as_view(), name='principal'),
    path('documentos-pagar/', views.DocumentoPagarListView.as_view(), name='documentos_pagar'),
    path('documento-pagar/crear/', views.DocumentoPagarCreateView.as_view(), name='c_documento_pagar'),
    path('documento-pagar/<int:pk>/eliminar/', views.DocumentoPagarDeleteView.as_view(), name='e_documento_pagar'),

]

urlreports = [
    path('r/orden-compra/', reports.OrdenCompraReport.as_view(), name='re_orden_compra'),
]


urlpatterns += urlreports
