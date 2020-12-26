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

from apps.formulacion.models import CentroCosto
from apps.formulacion.forms import CentroCostoForm
from apps.formulacion.serializers import CentroCostoSerializer

from apps.base.views import EmblenView


class PrincipalView(LoginRequiredMixin, View):

    permissions = {"all": ("formulacion.view_partida",)}

    template_name = "formulacion/principal.html"

    def get(self, request):
        return render(request, self.template_name)


class PartidaView(EmblenView):
    permissions = {"all": ("formulacion.view_partida",)}
    template_name = "formulacion/partida.html"
    json_post = True
    
    def altget(self, request, pk):
        partida = get_object_or_404(Partida, pk=pk)
        return {"partida": partida}
    
    def jsonpost(self, request, pk):
        partida = get_object_or_404(Partida, pk=pk)
        partida.descripcion = request.POST.get("descripcion")
        partida.save()
        return {"msg": "Partida Guardada Exitosamente"}


class PartidaListView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, ListView):

    # MultiplePermissionsRequiredMixin
    permissions = {"all": ("formulacion.view_partida",)}

    # ListView
    queryset = Partida.objects.all()
    paginate_by = 8
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


# Clases Centros de Costos
class CcostoView(EmblenView):
    permissions = {"all": ("formulacion.view_partida",)}
    template_name = "formulacion/ccosto.html"
    json_post = True
    
    def altget(self, request, pk):
        ccosto = get_object_or_404(CentroCosto, pk=pk)
        return {"ccosto": ccosto}
    
    def jsonpost(self, request, pk):
        ccosto = get_object_or_404(CentroCosto, pk=pk)
        ccosto.nombre = request.POST.get("nombre")
        ccosto.save()
        return {"msg": "Centro de Costo Guardado Exitosamente"}


class CcostoListView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, ListView):

    # MultiplePermissionsRequiredMixin
    permissions = {"all": ("formulacion.view_partida",)}

    # ListView
    queryset = CentroCosto.objects.all()
    paginate_by = 8
    template_name = "formulacion/ccostos.html"
    success_url = "formulacion:ccostos"


class CcostoUpdateView(EmblenView): 
    permissions = {"all": ("formulacion.view_partida",)}
    template_name = "formulacion/ccostoU.html"
    
    
class CcostoDeleteView(EmblenView):
    """Vista para borrar los centros de costo"""

    permissions = {"all": ("formulacion.delete_partida",)}
    
    def altget(self, request, pk):
        ccosto = get_object_or_404(CentroCosto, pk=pk)
        ccosto.eliminar()
        return redirect('formulacion:ccostos')


class CcostoCreateView(EmblenView):
    """
    Se crean los centros de costo de nivel 3 por medio de los auxiliares
    """

    # Variables Necesarias
    permissions = {"all": ("formulacion.view_partida",)}
    template_name = "formulacion/crear_ccosto.html"
    json_post = True

    # Variables de Ayuda
    ccostos = CentroCosto.objects.filter(nivel=1).annotate(option=Substr('codigo', 1, 1))
    
    def altget(self, request):
        return {'ccostos': self.ccostos}

    def altpost(self, request):
        # Se reciben los formularios para guardar un nuevo centro de costo

        #Creando el formulario y validandolo
        ccosto_form = CentroCostoForm(data=request.POST)
        if ccosto_form.is_valid():
            ccosto = ccosto_form.save(commit=False)
            ccosto.nivel = 3
            ccosto.save()
            return redirect('formulacion:ccostos')
        else:
            return {'ccostos': self.ccostos,'form': ccosto_form}

    def jsonpost(self, request):
        # Se manda un json con los centros de costo serializados

        try:
            # Obteniendo el centro de costo
            id_ccosto = int(request.POST.get("data"))
            ccosto = get_object_or_404(CentroCosto, pk=id_ccosto)
            
            # Salida
            ccosto_madre = CentroCostoSerializer(ccosto).data
            ccostos_hijas = CentroCostoSerializer(ccosto.siguientes(), many=True).data
            return {"ccosto_madre": ccosto_madre,"ccostos_hijas": ccostos_hijas}

        # Si existe error transformando el request
        except TypeError:
            return {"ccosto_madre": "Centro de Costo Inexistente","ccostos_hijas":[]}