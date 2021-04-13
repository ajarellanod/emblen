from braces.views import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

from apps.base.views import EmblenReport

from apps.compras.models import Orden


class OrdenCompraReport(LoginRequiredMixin, EmblenReport):
    view_template = "compras/r/orden_compra_V.html"
    report_template = "compras/r/orden_compra.html"
    with_modal = True

    def altpost(self, request):
        orden = request.POST.get("orden")
        if orden:
            return {"orden": orden}
        else:
            return redirect("compras:principal")