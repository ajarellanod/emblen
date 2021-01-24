from braces.views import LoginRequiredMixin

from apps.base.views import EmblenView

from apps.formulacion.models import AccionEspecifica


class CreditosAsignadosReport(LoginRequiredMixin, EmblenView):
    template_name = "formulacion/r/creditos_presupuestarios.html"

    def altget(self, request):
        qs = AccionEspecifica.objects.filter(programa__anio=2021).select_related(
            'programa__responsable__unidad_ejecutora__dependencia__sector'
        ).prefetch_related(
            'acciones_internas__partida_accioninternas'
        )
        
        return {"acc_especificas": qs}