from django.shortcuts import render
from django.views.generic import TemplateView


class InicioSesion(TemplateView):
    template_name = "usuarios/inicio.html"