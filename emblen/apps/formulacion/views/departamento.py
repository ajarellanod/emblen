from django.views.generic import ListView

from apps.base.views import (
    EmblenPermissionsMixin,
    EmblenDeleteView,
    EmblenFormView
)

from apps.formulacion.models import Departamento
from apps.formulacion.forms import DepartamentoForm


class DepartamentoListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_departamento",)}
    template_name = "formulacion/departamentos.html"
    success_url = "formulacion:departamentos"
    queryset = Departamento.objects.all().order_by("codigo")
    paginate_by = 8
    

class DepartamentoCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_departamento",)}
    template_name = "formulacion/departamento.html"
    form_class = DepartamentoForm
    success_url = "formulacion:departamentos"


class DepartamentoView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.view_departamento",)}
    template_name = "formulacion/departamento.html"
    form_class = DepartamentoForm
    update_form = True
    success_url = "formulacion:departamentos"


class DepartamentoDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_departamento",)}
    model = Departamento
    success_url = "formulacion:departamentos"
