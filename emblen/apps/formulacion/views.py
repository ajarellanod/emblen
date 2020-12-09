import json

from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView, FormMixin
from django.views.generic import ListView
from django.urls import reverse_lazy 
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.core.serializers import serialize

from braces.views import LoginRequiredMixin, MultiplePermissionsRequiredMixin

from apps.formulacion.models import Partida
from apps.formulacion.forms import PartidaForm
from apps.base.serializers import PartidaSerializer


class PrincipalView(LoginRequiredMixin, View):

    template_name = "formulacion/principal.html"

    def get(self, request):
        return render(request, self.template_name)


class PartidaView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, FormMixin, ListView):

    # MultiplePermissionsRequiredMixin
    permissions = {
        "all": ("formulacion.view_partida",)
    }

    # ListView
    queryset = Partida.objects.filter(estatus=True)
    context_object_name = "partidas"
    paginate_by = 5

    # FormMixin
    form_class = PartidaForm

    # ListView y FormMixin
    template_name = "formulacion/partida.html"
    success_url = "formulacion:partidas"

    # Metodo Propio - ListView no permite metodo POST
    def post(self, request):
        
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

        return redirect(self.success_url)


class PartidaUpdateView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, UpdateView): 
    
    permissions = {
        "all": ("formulacion.view_partida",)
    }

    model = Partida 

    form_class = PartidaForm

    template_name = "formulacion/partidaU.html"

    success_url = reverse_lazy('formulacion:partidas')


class PartidaDeleteView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, DeleteView):
   
    permissions = {
        "all": ("formulacion.view_partida",)
    }

    model = Partida

    form_class = PartidaForm()

    template_name = "formulacion/partidaD.html"

    success_url = reverse_lazy('formulacion:partidas')


class PartidaCreateView(LoginRequiredMixin, View):
    
    template_name = "formulacion/crear_partida.html"
    
    def get(self, request):
        return render(request, self.template_name, {'form': PartidaForm()})
    
    def post(self, request):
        if request.POST.get("data") is not None:
            id_partida = json.loads(request.POST.get("data"))
            output = serialize('json', Partida.obten_hijos(id_partida), cls=PartidaSerializer)
            return JsonResponse(output, safe=False)