from django.urls import path

from apps.ejecucion import views, reports

urlpatterns = [
    path('', views.PrincipalView.as_view(), name='principal'),

    path('ordenes-pagos/', views.OrdenPagoListView.as_view(), name='ordenes_pagos'),
    path('orden-pago/crear/', views.OrdenPagoCreateView.as_view(), name='c_orden_pago'),
]

urlreports = [
    path('r/orden-pago/', reports.OrdenPagoReport.as_view(), name='re_orden_pago'),
]


urlpatterns += urlreports