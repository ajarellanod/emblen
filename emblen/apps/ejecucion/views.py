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
    AfectacionPresupuestariaForm
)

from apps.ejecucion.serializers import (
    AfectacionPresupuestariaSerializer,
)

from apps.ejecucion.models import (
    TipoOrdenPago,
    OrdenPago,
    AfectacionPresupuestaria
)

from apps.formulacion.models import (
    PartidaAccionInterna,
    EjercicioPresupuestario,
    Partida
)

from apps.compras.models import (
    DocumentoPagar
)
# ----- Ejecución -----

class PrincipalView(LoginRequiredMixin, TemplateView):
    template_name = "ejecucion/principal.html"


# ----- Documento a Pagar -----
# class DocumentoPagarListView(EmblenPermissionsMixin, ListView):
#     permissions = {"all": ("ejecucion.view_documentopagar",)}
#     template_name = "ejecucion/documentos_pagar.html"
#     success_url = "ejecucion:documentos_pagar"
#     queryset = DocumentoPagar.objects.all().order_by("numero")
#     paginate_by = 8

# class DocumentoPagarView(EmblenPermissionsMixin, EmblenFormView):
#     permissions = {"all": ("ejecucion.view_documentopagar",)}
#     template_name = "ejecucion/crear_documento_pagar.html"
#     form_class = DocumentoPagarForm
#     update_form = True
#     success_url = "ejecucion:documentos_pagar"

# class DocumentoPagarCreateView(EmblenPermissionsMixin, EmblenFormView):
#     permissions = {"all": ("ejecucion.add_documentopagar",)}
#     template_name = "ejecucion/crear_documento_pagar.html"
#     form_class = DocumentoPagarForm
#     success_url = "ejecucion:documentos_pagar"

#     def form_valid(self, form):
#         documento_pagar = form.save(commit=False)
#         # DocumentoPagar.gen_rest_attrs()
#         return super().form_valid(documento_pagar)

# class DocumentoPagarDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
#     permissions = {"all": ("ejecucion.delete_documentopagar",)}
#     model = DocumentoPagar
#     success_url = "ejecucion:documentos_pagar"


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
        orden_pago = form.save(commit=False)
        orden_pago.gen_rest_attrs()
        return super().form_valid(orden_pago)


class OrdenPagoView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("ejecucion.view_ordenpago",)}
    template_name = "ejecucion/crear_orden_pago.html"
    update_form = True
    form_class = OrdenPagoForm
    success_url = "ejecucion:ordenes_pagos"
    
    def get_data(self, data, instance):
        new_data = data.copy()
        # new_data.update({
        #     "nivel": instance.nivel, 
        #     "elaborador": instance.responsable.id
        # })
        return super().get_data(new_data, instance)


class OrdenPagoDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("ejecucion.delete_ordenpago",)}
    model = OrdenPago
    success_url = "ejecucion:ordenes_pagos"