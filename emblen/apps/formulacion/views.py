from django.shortcuts import render, redirect, get_object_or_404
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


class PartidaDeleteView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, View):
    permissions = {"all": ("formulacion.view_partida",)}
    
    def get(self, request, pk):
        partida = get_object_or_404(Partida, pk=pk)
        partida.estatus = False
        partida.save()
        return redirect('formulacion:partidas')


class PartidaCreateView(LoginRequiredMixin, View):
    
    template_name = "formulacion/crear_partida.html"
    partidas = Partida.objects.filter(estatus=True, nivel=1).annotate(option=Substr('cuenta', 1, 1))
    
    def get(self, request):
        return render(request, self.template_name, {'partidas': self.partidas})
    
    def post(self, request):
         # Guardando la nueva partida
        if request.POST.get("saldo") is not None:
            partida = PartidaForm(data=request.POST)
            if partida.is_valid():
                partida = partida.save(commit=False)
                partida.nivel = 6
                partida.save()
                return redirect('formulacion:partidas')
            else:
                return render(request, self.template_name, {'partidas': self.partidas, 'form': partida})
        
        # Filtro de Partidas
        try:
            id_partida = int(request.POST.get("data"))
            
            if id_partida is not None:
                partida = Partida.objects.filter(pk=id_partida).first()
                output = {
                    "partida_madre": PartidaSerializer(partida).data,
                    "partidas_hijas": PartidaSerializer(partida.siguientes(), many=True).data,
                }
                return JsonResponse(output, safe=False)
        except TypeError:
            output = {"partida_madre": "Partida Inexistente","partidas_hijas":[]}
            return JsonResponse(output, safe=False)