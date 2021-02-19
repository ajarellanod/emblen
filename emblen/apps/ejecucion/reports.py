from braces.views import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from apps.base.views import EmblenReport

from apps.ejecucion.models import OrdenPago


class OrdenPagoReport(LoginRequiredMixin, EmblenReport):
    view_template = "ejecucion/r/orden_pago_V.html"
    report_template = "ejecucion/r/orden_pago.html"
    with_modal = True

    def altpost(self, request):
        orden = request.POST.get("orden")
        if orden:
            return {"orden": orden}
        else:
            return redirect("ejecucion:principal")