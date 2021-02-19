from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse, Http404
from django.db.models.functions import Substr
from braces.views import LoginRequiredMixin

from apps.base.views import (
    EmblenView,
    EmblenPermissionsMixin,
    EmblenDeleteView,
    EmblenFormView
)

from apps.ejecucion.forms import (
    TipoOrdenPagoForm,
    OrdenPagoForm,
    DetalleOrdenPagoForm
)

from apps.ejecucion.models import (
    TipoOrdenPago,
    OrdenPago,
    DetalleOrdenPago
)

# ----- Ejecución -----

class PrincipalView(LoginRequiredMixin, TemplateView):
    template_name = "ejecucion/principal.html"


# ----- Ordenes de Pago -----

class OrdenPagoListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("ejecucion.view_ordenpago",)}
    template_name = "ejecucion/ordenes_pagos.html"
    success_url = "ejecucion:ordenes_pagos"
    paginate_by = 8

    def get_queryset(self):
        ordenespago = self.request.GET.get('ordenespago')
        if ordenespago:
            return OrdenPago.objects.filter(orden_pago=ordenespago).order_by("orden_pago")
        return OrdenPago.objects.order_by("orden_pago")


class OrdenPagoCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("ejecucion.add_ordenpago",)}
    template_name = "ejecucion/crear_orden_pago.html"
    form_class = OrdenPagoForm
    success_url = "ejecucion:ordenes_pagos"
    
    def form_valid(self, form):
        ordenes_pago = form.save(commit=False)
        ordenes_pago.gen_rest_attrs()
        return super().form_valid(ordenes_pago)