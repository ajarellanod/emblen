from django.shortcuts import render
from django.views import View

# Create your views here.
#from django.views.generic import TemplateView

from django.shortcuts import render, get_object_or_404
from .models import Partida

class PartidaView(View):
    
    template_name = "formulacion/principal.html"

    def get(self, request):
        partidas = Partida.objects.filter(estatus=True)
        return render(request, self.template_name, {'partidas': partidas})