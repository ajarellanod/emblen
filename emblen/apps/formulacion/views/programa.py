from django.views.generic import ListView

from apps.base.views import (
    EmblenPermissionsMixin,
    EmblenDeleteView,
    EmblenFormView
)

from apps.formulacion.models import Programa
from apps.formulacion.forms import ProgramaForm


class ProgramaListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_programa",)}
    template_name = "formulacion/programas.html"
    success_url = "formulacion:programas"
    queryset = Programa.objects.all().order_by("codigo")
    paginate_by = 8


class ProgramaCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_programa",)}
    template_name = "formulacion/crear_programa.html"
    form_class = ProgramaForm
    success_url = "formulacion:programas"

    def form_valid(self, form):
        programa = form.save(commit=False)
        programa.gen_rest_attrs()
        return super().form_valid(programa)


class ProgramaView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.view_programa",)}
    template_name = "formulacion/crear_programa.html"
    update_form = True
    form_class = ProgramaForm
    success_url = "formulacion:programas"
    
    def get_data(self, data, instance):
        new_data = data.copy()
        new_data.update({
            "nivel": instance.nivel, 
            "responsable": instance.responsable.id
        })
        return super().get_data(new_data, instance)


class ProgramaDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_programa",)}
    model = Programa
    success_url = "formulacion:programas"
