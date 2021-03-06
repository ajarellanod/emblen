from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView
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


# ----- Modificacion -----

class ModificacionView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("planificacion.add_modificacion",)}
    template_name = "planificacion/crear_modificacion.html"
    form_class = ModificacionForm
    success_url = "planificacion:principal"

    def form_valid(self, form):
        modificacion = form.save(commit=False)
        modificacion.afecta_partida()
        modificacion.gen_rest_attrs()
        return super().form_valid(modificacion)


class ModificacionTraspasoView(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("planificacion.add_modificacion",)}
    template_name = "planificacion/crear_traspaso.html"
    json_post = True

    def jsonpost(self, request):
        pass