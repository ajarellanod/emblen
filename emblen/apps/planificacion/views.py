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
# Create your views here.
# ----- Planificacion -----

class PrincipalView(LoginRequiredMixin, TemplateView):
    template_name = "planificacion/principal.html"