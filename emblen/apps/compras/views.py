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

from apps.compras.forms import (
    DocumentoPagarForm
)

from apps.compras.models import (
    DocumentoPagar
)


# ----- Compras -----

class PrincipalView(LoginRequiredMixin, TemplateView):
    template_name = "compras/principal.html"
    

class DocumentoPagarListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("compras.view_documentopagar",)}
    template_name = "compras/documentos_pagar.html"
    success_url = "compras:documentos_pagar"
    queryset = DocumentoPagar.objects.all().order_by("numero")
    paginate_by = 8


class DocumentoPagarCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("compras.add_documentopagar",)}
    template_name = "compras/crear_documento_pagar.html"
    form_class = DocumentoPagarForm
    success_url = "compras:documentos_pagar"

    def form_valid(self, form):
        documento_pagar = form.save(commit=False)
        # DocumentoPagar.gen_rest_attrs()
        return super().form_valid(documento_pagar)

class DocumentoPagarDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("compras.delete_documentopagar",)}
    model = DocumentoPagar
    success_url = "compras:documentos_pagar"
