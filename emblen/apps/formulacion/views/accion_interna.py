from django.views.generic import ListView

from apps.base.views import (
    EmblenPermissionsMixin,
    EmblenDeleteView,
    EmblenFormView
)

from apps.formulacion.models import AccionInterna
from apps.formulacion.forms import AccionInternaForm


class AccionInternaListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_accioninterna",)}
    queryset = AccionInterna.objects.all().order_by("accion_especifica","codigo")
    template_name = "formulacion/acciones_internas.html"
    success_url = "formulacion:acciones_internas"
    paginate_by = 8


class AccionInternaCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_accioninterna",)}
    template_name = "formulacion/crear_accion_interna.html"
    form_class = AccionInternaForm
    success_url = "formulacion:acciones_internas"

    def form_valid(self, form):
        accion_interna = form.save(commit=False)
        accion_interna.gen_rest_attrs()
        return super().form_valid(accion_interna)


class AccionInternaView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.change_accioninterna",)}
    template_name = "formulacion/crear_accion_interna.html"
    form_class = AccionInternaForm
    update_form = True
    success_url = "formulacion:acciones_internas"

    def get_data(self, data, instance):
        new_data = data.copy()
        new_data.update({"accion_interna": instance.accion_interna})
        return super().get_data(new_data, instance)


class AccionInternaDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_accioninterna",)}
    model = AccionInterna
    success_url = "formulacion:acciones_internas"
    