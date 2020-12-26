from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse, Http404
from django.db.models.functions import Substr
from braces.views import LoginRequiredMixin

from apps.base.views import EmblenView, EmblenPermissionsMixin
from apps.formulacion.forms import PartidaForm, DepartamentoForm
from apps.formulacion.serializers import PartidaSerializer
from apps.formulacion.models import (Partida, Departamento)

# ----- Formulacion -----

class PrincipalView(LoginRequiredMixin, TemplateView):
    template_name = "formulacion/principal.html"


# ----- Partidas -----

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

    # MultiplePermissionsRequiredMixin
    permissions = {"all": ("formulacion.view_partida",)}

    # ListView
    queryset = Partida.objects.all()
    paginate_by = 8
    template_name = "formulacion/partidas.html"
    success_url = "formulacion:partidas"
    
    
class PartidaDeleteView(EmblenPermissionsMixin, EmblenView):
    """Vista para borrar las partidas"""

    permissions = {"all": ("formulacion.delete_partida",)}
    
    def altget(self, request, pk):
        partida = get_object_or_404(Partida, pk=pk)
        partida.eliminar()
        return redirect('formulacion:partidas')


class PartidaCreateView(EmblenPermissionsMixin, EmblenView):
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


# ----- Departamentos -----

class DepartamentoView(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("formulacion.view_departamento",)}
    template_name = "formulacion/departamento.html"
    
    def altget(self, request, pk):
        departamento = get_object_or_404(Departamento, pk=pk)
        departamento_form = DepartamentoForm(instance=departamento)
        return {"form": departamento_form}

    def altpost(self, request, pk):
        departamento = get_object_or_404(Departamento, pk=pk)
        
        departamento_form = DepartamentoForm(
            data=request.POST, instance=departamento
        )

        if departamento_form.is_valid():
            departamento_form.save()
            return redirect("formulacion:departamentos")
        else:
            return {"form": departamento_form}


class DepartamentoListView(EmblenPermissionsMixin, ListView):

    # MultiplePermissionsRequiredMixin
    permissions = {"all": ("formulacion.view_departamento",)}

    # ListView
    queryset = Departamento.objects.all().order_by("codigo")
    paginate_by = 8
    template_name = "formulacion/departamentos.html"
    success_url = "formulacion:departamentos"


class DepartamentoCreateView(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("formulacion.view_departamento",)}
    template_name = "formulacion/departamento.html"
    
    def altget(self, request):
        departamento_form = DepartamentoForm()
        return {"form": departamento_form}

    def altpost(self, request):
        departamento_form = DepartamentoForm(data=request.POST)
        if departamento_form.is_valid():
            departamento_form.save()
            return redirect("formulacion:departamentos")
        else:
            return {"form": departamento_form}


class DepartamentoDeleteView(EmblenPermissionsMixin, EmblenView):
    """Vista para borrar las departamentos"""

    permissions = {"all": ("formulacion.delete_departamento",)}
    
    def altget(self, request, pk):
        departamento = get_object_or_404(Departamento, pk=pk)
        departamento.eliminar()
        return redirect('formulacion:departamentos')