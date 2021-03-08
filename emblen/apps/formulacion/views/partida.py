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

from apps.formulacion.serializers import PartidaSerializer
from apps.formulacion.forms import PartidaForm
from apps.formulacion.models import Partida


class PartidaView(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("formulacion.view_partida",)}
    template_name = "formulacion/partida.html"
    json_post = True
    
    def altget(self, request, pk):
        partida = get_object_or_404(Partida, pk=pk)
        return {"partida": partida}
    
    def jsonpost(self, request, pk):
        partida = get_object_or_404(Partida, pk=pk)
        descripcion = request.POST.get("descripcion")
        if descripcion is not None and descripcion != "":
            partida.descripcion = descripcion        
            partida.save()
            return {"msg": "Partida Guardada Exitosamente", "icon": "success"}
        else:
            return {"msg": "Partida Fallo al Guardar", "icon": "error"}


class PartidaListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_partida",)}
    queryset = Partida.objects.all().order_by("cuenta")
    paginate_by = 8
    template_name = "formulacion/partidas.html"
    success_url = "formulacion:partidas"
    
    
class PartidaDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_partida",)}
    model = Partida
    success_url = 'formulacion:partidas'


class PartidaCreateView(EmblenPermissionsMixin, EmblenView):
    """
    Se crean las partidas de nivel 6 por medio de los auxiliares
    """
    # Variables Necesarias
    permissions = {"all": ("formulacion.add_partida",)}
    template_name = "formulacion/crear_partida.html"
    json_post = True

    # Variables de Ayuda
    partidas = Partida.objects.filter(nivel=1).annotate(option=Substr('cuenta', 1, 1)).order_by("cuenta")
    
    def altget(self, request):
        return {'partidas': self.partidas}

    def altpost(self, request):
        # Se reciben los formularios para guardar una nueva partida
        # Comprobando que hayan enviado el saldo
        if request.POST.get("cuenta") is not None:
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
