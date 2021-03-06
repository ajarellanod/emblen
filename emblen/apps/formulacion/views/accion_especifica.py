from django.views.generic import ListView

from apps.base.views import (
    EmblenPermissionsMixin,
    EmblenDeleteView,
    EmblenFormView
)

from apps.formulacion.models import AccionEspecifica
from apps.formulacion.forms import AccionEspecificaForm


class AccionEspecificaListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_accionespecifica",)}
    template_name = "formulacion/acciones_especificas.html"
    success_url = "formulacion:acciones_especificas"
    paginate_by = 8

    def get_queryset(self):
        programa = self.request.GET.get('programa')
        if programa:
            return AccionEspecifica.objects.filter(programa=programa).order_by("codigo")
        return AccionEspecifica.objects.order_by("codigo")


class AccionEspecificaView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.change_accionespecifica",)}
    template_name = "formulacion/crear_accion_especifica.html"
    update_form = True
    form_class = AccionEspecificaForm
    success_url = "formulacion:acciones_especificas"
        
    def get_data(self, data, instance):
        new_data = data.copy()
        new_data.update({
            "programa": instance.programa, 
            "responsable": instance.responsable.id
        })
        return super().get_data(new_data, instance)


class AccionEspecificaCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_accionespecifica",)}
    template_name = "formulacion/crear_accion_especifica.html"
    form_class = AccionEspecificaForm
    success_url = "formulacion:acciones_especificas"

    def form_valid(self, form):
        accion_especifica = form.save(commit=False)
        accion_especifica.gen_rest_attrs()
        return super().form_valid(accion_especifica)


class AccionEspecificaDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_accionespecifica",)}
    model = AccionEspecifica
    success_url = "formulacion:acciones_especificas"
    