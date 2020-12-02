from django.shortcuts import render

# Create your views here.
#from django.views.generic import TemplateView

from django.shortcuts import render, get_object_or_404
from .models import Partida

class formulacion():
    #template_name = "formulacion/principal.html"

    def partida_lista(request):
        partidas = Partida.objects.filter(estatus="1")
        return render(request,
                    'formulacion/principal.html',
                    {'partidas': partidas})