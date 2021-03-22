from django.views.generic import ListView

from apps.base.views import (
    EmblenPermissionsMixin,
    EmblenDeleteView,
    EmblenFormView
)

from apps.formulacion.models import EjercicioPresupuestario
from apps.formulacion.forms import EjercicioPresupuestarioForm


class EjercicioPresupuestarioListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_ejerciciopresupuestario",)}
    queryset = EjercicioPresupuestario.objects.all().order_by('-anio')
    template_name = "formulacion/ejercicios_presupuestarios.html"
    success_url = "formulacion:ejercicios_presupuestarios"
    paginate_by = 8



class EjercicioPresupuestarioCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_ejerciciopresupuestario",)}
    template_name = "formulacion/crear_ejercicio_presupuestario.html"
    form_class = EjercicioPresupuestarioForm
    success_url = "formulacion:ejercicios_presupuestarios"

    def form_valid(self, form):
        ejercicio_presupuestario = form.save(commit=False)
        ejercicio_presupuestario.gen_rest_attrs()
        return super().form_valid(ejercicio_presupuestario)


class EjercicioPresupuestarioView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.change_ejerciciopresupuestario",)}
    template_name = "formulacion/crear_ejercicio_presupuestario.html"
    form_class = EjercicioPresupuestarioForm
    update_form = True
    success_url = "formulacion:ejercicios_presupuestarios"


    def get_data(self, data, instance):
        new_data = data.copy()
        new_data.update({"condicion": 1})     
        return super().get_data(new_data, instance)

    # def form_valid(self, form):
    #     ejercicio_presupuestario = form.save(commit=False)
    #     return super().form_valid(ejercicio_presupuestario)


class EjercicioPresupuestarioDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_ejerciciopresupuestario",)}
    model = EjercicioPresupuestario
    success_url = "formulacion:ejercicios_presupuestarios"
    