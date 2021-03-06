from django.views.generic import ListView

from apps.base.views import (
    EmblenPermissionsMixin,
    EmblenDeleteView,
    EmblenFormView
)

from apps.formulacion.models import LineaPrograma
from apps.formulacion.forms import LineaProgramaForm


class LineaProgramaListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_lineaprograma",)}
    template_name = "formulacion/lineas_programas.html"
    paginate_by = 8

    def get_queryset(self):
        programa = self.request.GET.get('programa')
        if programa:
            return LineaPrograma.objects.filter(programa=programa).order_by("codigo")
        return LineaPrograma.objects.order_by("codigo")


class LineaProgramaView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.change_lineaprograma",)}
    template_name = "formulacion/crear_linea_programa.html"
    form_class = LineaProgramaForm
    update_form = True
    success_url = "formulacion:principal"

    def get_data(self, data, instance):
        new_data = data.copy()
        new_data.update({"programa": instance.programa})
        return super().get_data(new_data, instance)


class LineaProgramaCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_lineaprograma",)}
    template_name = "formulacion/crear_linea_programa.html"
    form_class = LineaProgramaForm
    success_url = "formulacion:principal"

    def form_valid(self, form):
        linea_programa = form.save(commit=False)
        linea_programa.gen_rest_attrs()
        return super().form_valid(linea_programa)


class LineaProgramaDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_lineaprograma",)}
    model = LineaPrograma
    success_url = "formulacion:principal"
    