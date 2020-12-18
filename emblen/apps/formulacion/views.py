from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy 
from django.http import JsonResponse
from django.db.models.functions import Substr

from braces.views import LoginRequiredMixin, MultiplePermissionsRequiredMixin

from apps.formulacion.models import Partida
from apps.formulacion.forms import PartidaForm
from apps.formulacion.serializers import PartidaSerializer


class PrincipalView(LoginRequiredMixin, View):

    template_name = "formulacion/principal.html"

    def get(self, request):
        return render(request, self.template_name)


class PartidaListView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, ListView):

    # MultiplePermissionsRequiredMixin
    permissions = {"all": ("formulacion.view_partida",)}

    # ListView
    queryset = Partida.objects.filter(estatus=True)
    paginate_by = 5
    template_name = "formulacion/partidas.html"
    success_url = "formulacion:partidas"


class PartidaUpdateView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, UpdateView): 
    
    permissions = {"all": ("formulacion.view_partida",)}

    model = Partida 
    form_class = PartidaForm
    template_name = "formulacion/partidaU.html"
    success_url = reverse_lazy('formulacion:partidas')


class PartidaDeleteView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, DeleteView):
   
    permissions = {"all": ("formulacion.view_partida",)}

    model = Partida
    success_url = reverse_lazy('formulacion:partidas')


class PartidaCreateView(LoginRequiredMixin, View):
    
    template_name = "formulacion/crear_partida.html"
    
    def get(self, request):
        partidas_principales = Partida.objects.filter(
            estatus=True, nivel=1
        ).annotate(option=Substr('cuenta', 1, 1))

        return render(request, self.template_name, {'partidas': partidas_principales})
    
    def post(self, request):
        # Filtro de Partidas
        if request.POST.get("data") is not None:
            id_partida = request.POST.get("data")
            partida = Partida.objects.filter(pk=id_partida).first()
            output = {
                "partida_madre": PartidaSerializer(partida).data,
                "partidas_hijas": PartidaSerializer(partida.siguientes(), many=True).data,
            }
            return JsonResponse(output, safe=False)

        # Guardando la nueva partida
        elif request.POST.get("saldo") is not None:
            partida = PartidaForm(data=request.POST)
            if partida.is_valid():
                partida.save()
                return redirect('formulacion:partidas')
            else:
                pass