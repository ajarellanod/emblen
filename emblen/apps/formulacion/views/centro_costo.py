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

from apps.formulacion.serializers import CentroCostoSerializer
from apps.formulacion.forms import CentroCostoForm
from apps.formulacion.models import CentroCosto


class CentroCostoView(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("formulacion.view_centro_costo",)}
    template_name = "formulacion/ccosto.html"
    json_post = True
    
    def altget(self, request, pk):
        ccosto = get_object_or_404(CentroCosto, pk=pk)
        return {"ccosto": ccosto}
    
    def jsonpost(self, request, pk):
        ccosto = get_object_or_404(CentroCosto, pk=pk)
        nombre = request.POST.get("nombre")
        if nombre is not None and nombre != "":
            ccosto.nombre = nombre        
            ccosto.save()
            return {"msg": "Centro de Costo Guardado Exitosamente", "icon": "success"}
        else:
            return {"msg": "Centro de Costo Fallo al Guardar", "icon": "error"}


class CentroCostoListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_centro_costo",)}
    queryset = CentroCosto.objects.all()
    paginate_by = 8
    template_name = "formulacion/ccostos.html"
    success_url = "formulacion:centros_costos"

    
class CentroCostoDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    """Vista para borrar los centros de costo"""
    permissions = {"all": ("formulacion.delete_centro_costo",)}
    model = CentroCosto
    success_url = 'formulacion:centros_costos'


class CentroCostoCreateView(EmblenPermissionsMixin, EmblenView):
    """
    Se crean los centros de costo de nivel 3 por medio de los auxiliares
    """

    # Variables Necesarias
    permissions = {"all": ("formulacion.add_centro_costo",)}
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
            return redirect('formulacion:centros_costos')
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
            