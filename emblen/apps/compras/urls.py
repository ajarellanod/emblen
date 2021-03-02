from django.urls import path

from apps.compras import views, reports

urlpatterns = [
    path('', views.PrincipalView.as_view(), name='principal'),

]

urlreports = [
    path('r/orden-compra/', reports.OrdenCompraReport.as_view(), name='re_orden_compra'),
]


urlpatterns += urlreports
