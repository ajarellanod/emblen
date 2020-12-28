from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse, Http404
from django.db.models.functions import Substr
from braces.views import LoginRequiredMixin

from apps.base.views import EmblenView, EmblenPermissionsMixin, EmblenDeleteView, EmblenFormView
from apps.formulacion.models import (Partida, Departamento, UnidadEjecutora, CentroCosto)


class TodasPartidasReport(LoginRequiredMixin, EmblenView):
    template_name = "formulacion/reportes/r_todas_partidas.html"
    
    def altget(self, request):
        partidas = Partida.objects.all()
        return {"partidas": partidas}