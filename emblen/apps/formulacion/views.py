from django.shortcuts import render
from django.views import View

from braces.views import LoginRequiredMixin, MultiplePermissionsRequiredMixin

from apps.formulacion.models import Partida
from apps.formulacion.forms import PartidaForm


class PartidaView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, View):
    
    template_name = "formulacion/principal.html"
    
    permissions = {
        "all": ("formulacion.view_partida",)
    }

    def get(self, request):
        partidas = Partida.objects.filter(estatus=True)
        partida_form = PartidaForm()
        return render(request, self.template_name, {'partidas': partidas, 'form': partida_form})
    
    def post(self, request):
        pass