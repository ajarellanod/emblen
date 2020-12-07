from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy 
from django.core.paginator import Paginator

from braces.views import LoginRequiredMixin, MultiplePermissionsRequiredMixin

from apps.formulacion.models import Partida
from apps.formulacion.forms import PartidaForm


class PrincipalView(LoginRequiredMixin, View):

    template_name = "formulacion/principal.html"

    def get(self, request):
        return render(request, self.template_name)


class PartidaView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, View):
    
    template_name = "formulacion/partida.html"
    
    permissions = {
        "all": ("formulacion.view_partida",)
    }

    def get(self, request):
        partidas = Partida.objects.filter(estatus=True)
        partida_form = PartidaForm()
        paginator = Paginator(partidas, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, self.template_name, {'partidas': partidas, 'form': partida_form,'page_obj': page_obj})

    def post(self, request):
        form= PartidaForm(request.POST)
        if form.is_valid():
            form.save()

        partidas = Partida.objects.filter(estatus=True)
        partida_form = PartidaForm()
        paginator = Paginator(partidas, 5)

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        return render(request, self.template_name, {'partidas': partidas, 'form': partida_form,'page_obj': page_obj})


class PartidaUpdateView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, UpdateView): 
    
    permissions = {
        "all": ("formulacion.view_partida",)
    }

    model = Partida 

    form_class = PartidaForm

    template_name = "formulacion/partidaU.html"

    success_url = reverse_lazy('formulacion:formulacion')


class PartidaDeleteView(LoginRequiredMixin, MultiplePermissionsRequiredMixin, DeleteView):
   
    permissions = {
        "all": ("formulacion.view_partida",)
    }

    model = Partida 

    form_class = PartidaForm()

    template_name = "formulacion/partidaD.html"

    success_url = reverse_lazy('formulacion:formulacion')

