from django.views.generic import ListView

from apps.base.views import (
    EmblenPermissionsMixin,
    EmblenDeleteView,
    EmblenFormView
)

from apps.formulacion.models import UnidadEjecutora
from apps.formulacion.forms import UnidadEjecutoraForm


class UnidadEjecutoraListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_unidadejecutora",)}
    template_name = "formulacion/unidades_ejecutoras.html"
    success_url = "formulacion:unidades_ejecutoras"
    queryset = UnidadEjecutora.objects.all().order_by("codigo")
    paginate_by = 8


class UnidadEjecutoraCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_unidadejecutora",)}
    template_name = "formulacion/unidad_ejecutora.html"
    form_class = UnidadEjecutoraForm
    success_url = "formulacion:unidades_ejecutoras"
    

class UnidadEjecutoraView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.view_unidadejecutora",)}
    template_name = "formulacion/unidad_ejecutora.html"
    form_class = UnidadEjecutoraForm
    update_form = True
    success_url = "formulacion:unidades_ejecutoras"


class UnidadEjecutoraDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_unidadejecutora",)}
    model = UnidadEjecutora
    success_url = "formulacion:unidades_ejecutoras"
