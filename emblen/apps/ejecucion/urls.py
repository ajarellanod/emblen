from django.urls import path

from apps.ejecucion import views, reports

urlpatterns = [
    path('', views.PrincipalView.as_view(), name='principal'),
]

urlreports = [
    path('r/orden-pago/', reports.OrdenPagoReport.as_view(), name='re_orden_pago'),
]


urlpatterns += urlreports