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

from apps.planificacion.models import (
    Modificacion
)

from apps.planificacion.forms import (
    ModificacionForm
)

# ----- Planificación -----

class PrincipalView(LoginRequiredMixin, TemplateView):
    template_name = "planificacion/principal.html"
    

class ModificacionView(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("planificacion.add_modificacion",)}
    template_name = "formulacion/crear_modificacion.html"
    form_class = ModificacionForm
    success_url = "formulacion:programas"

    def form_valid(self, form):
        modificacion = form.save(commit=False)
        modificacion.gen_rest_attrs()
        return super().form_valid(modificacion)
    

