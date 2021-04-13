from django.urls import path

from apps.ejecucion import views, reports

urlpatterns = [
    path('', views.PrincipalView.as_view(), name='principal'),

    # path('documentos-pagar/', views.DocumentoPagarListView.as_view(), name='documentos_pagar'),
    # path('documento-pagar/<int:pk>/', views.DocumentoPagarView.as_view(), name='v_documento_pagar'),
    # path('documento-pagar/crear/', views.DocumentoPagarCreateView.as_view(), name='c_documento_pagar'),
    # path('documento-pagar/<int:pk>/eliminar/', views.DocumentoPagarDeleteView.as_view(), name='e_documento_pagar'),

    path('ordenes-pagos/', views.OrdenPagoListView.as_view(), name='ordenes_pagos'),
    path('ordenes-pagos/<int:pk>/', views.OrdenPagoView.as_view(), name='v_orden_pago'),
    path('orden-pago/crear/', views.OrdenPagoCreateView.as_view(), name='c_orden_pago'), 
    path('orden-pago/<int:pk>/eliminar/', views.OrdenPagoDeleteView.as_view(), name='e_orden_pago'), 

]

urlreports = [
    path('r/orden-pago/', reports.OrdenPagoReport.as_view(), name='re_orden_pago'),
]


urlpatterns += urlreports