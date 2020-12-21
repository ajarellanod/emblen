from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView
from django.http import JsonResponse, Http404
from django.db.models.functions import Substr

from braces.views import LoginRequiredMixin, MultiplePermissionsRequiredMixin

from apps.formulacion.models import Partida
from apps.formulacion.forms import PartidaForm
from apps.formulacion.serializers import PartidaSerializer

from apps.base.views import EmblenView


class PrincipalView(EmblenView):

    permissions = {"all": ("formulacion.view_partida",)}

    template_name = "formulacion/principal.html"

    def get(self, request):
        return render(request, self.template_name)


class PartidaListView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, ListView):

    # MultiplePermissionsRequiredMixin
    permissions = {"all": ("formulacion.view_partida",)}

    # ListView
    queryset = Partida.objects.all()
    paginate_by = 5
    template_name = "formulacion/partidas.html"
    success_url = "formulacion:partidas"


class PartidaUpdateView(EmblenView): 
    permissions = {"all": ("formulacion.view_partida",)}
    template_name = "formulacion/partidaU.html"
    
    
class PartidaDeleteView(EmblenView):
    """Vista para borrar las partidas"""

    permissions = {"all": ("formulacion.delete_partida",)}
    
    def altget(self, request, pk):
        partida = get_object_or_404(Partida, pk=pk)
        partida.eliminar()
        return redirect('formulacion:partidas')


class PartidaCreateView(EmblenView):
    """
    Se crean las partidas de nivel 6 por medio de los auxiliares
    """

    # Variables Necesarias
    permissions = {"all": ("formulacion.view_partida",)}
    template_name = "formulacion/crear_partida.html"
    json_post = True

    # Variables de Ayuda
    partidas = Partida.objects.filter(nivel=1).annotate(option=Substr('cuenta', 1, 1))
    
    def altget(self, request):
        return {'partidas': self.partidas}

    def altpost(self, request):
        # Se reciben los formularios para guardar una nueva partida

        # Comprobando que hayan enviado el saldo
        if request.POST.get("saldo") is not None:

            #Creando el formulario y validandolo
            partida_form = PartidaForm(data=request.POST)
            if partida_form.is_valid():
                partida = partida_form.save(commit=False)
                partida.nivel = 6
                partida.save()
                return redirect('formulacion:partidas')
            else:
                return {'partidas': self.partidas,'form': partida_form}

        else:
            return Http404()

    def jsonpost(self, request):
        # Se manda un json con las partidas serializadas

        try:
            # Obteniendo la partida
            id_partida = int(request.POST.get("data"))
            partida = get_object_or_404(Partida, pk=id_partida)
            
            # Salida
            partida_madre = PartidaSerializer(partida).data
            partidas_hijas = PartidaSerializer(partida.siguientes(), many=True).data
            return {"partida_madre": partida_madre,"partidas_hijas": partidas_hijas}

        # Si existe error transformando el request
        except TypeError:
            return {"partida_madre": "Partida Inexistente","partidas_hijas":[]}