from braces.views import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from apps.base.views import EmblenReport

from apps.formulacion.models import AccionEspecifica


class CreditosAsignadosReport(LoginRequiredMixin, EmblenReport):
    view_template = "formulacion/r/creditos_presupuestarios_V.html"
    report_template = "formulacion/r/creditos_presupuestarios.html"
    with_modal = True

    def altpost(self, request):
        anio = request.POST.get("anio")
        if anio:
            result = AccionEspecifica.objects.filter(programa__anio=anio).select_related(
                'programa__responsable__unidad_ejecutora__dependencia__sector'
            ).prefetch_related(
                'acciones_internas__partida_accioninternas'
            )
            return {"acc_especificas": result}
        else:
            return redirect("formulacion:principal")