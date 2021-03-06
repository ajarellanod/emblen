from django.views.generic import ListView

from apps.base.views import (
    EmblenPermissionsMixin,
    EmblenDeleteView,
    EmblenFormView
)

from apps.formulacion.models import PlanDesarrollo
from apps.formulacion.forms import PlanDesarrolloForm


class PlanDesarrolloListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_plandesarrollo",)}
    template_name = "formulacion/planes_desarrollo.html"
    paginate_by = 8

    def get_queryset(self):
        programa = self.request.GET.get('programa')
        if programa:
            return PlanDesarrollo.objects.filter(programa=programa).order_by("codigo")
        return PlanDesarrollo.objects.order_by("codigo")


class PlanDesarrolloCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_plandesarrollo",)}
    template_name = "formulacion/crear_plan_desarrollo.html"
    form_class = PlanDesarrolloForm
    success_url = "formulacion:principal"

    def form_valid(self, form):
        plan_desarrollo = form.save(commit=False)
        plan_desarrollo.gen_rest_attrs()
        return super().form_valid(plan_desarrollo)


class PlanDesarrolloView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.view_departamento",)}
    template_name = "formulacion/crear_plan_desarrollo.html"
    form_class = PlanDesarrolloForm
    update_form = True
    success_url = "formulacion:principal"


class PlanDesarrolloDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_plandesarrollo",)}
    model = PlanDesarrollo
    success_url = "formulacion:principal"
