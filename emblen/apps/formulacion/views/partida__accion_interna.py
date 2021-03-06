from django.shortcuts import render, redirect, get_object_or_404
from apps.base.views import EmblenView, EmblenPermissionsMixin, EmblenDeleteView

from apps.formulacion.models import (
    Partida,
    AccionInterna,
    EjercicioPresupuestario,
    PartidaAccionInterna
)
from apps.formulacion.serializers import PartidaAccionInternaSerializer


class PartidaAccionInternaView(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("formulacion.add_partidaaccioninterna",)}
    template_name = "formulacion/partida_accion_interna.html"
    json_post = True

    def altget(self, request):
        acciones = AccionInterna.objects.all()
        partidas = Partida.objects.exclude(nivel=1)
        return {"acciones": acciones, "partidas": partidas}

    def jsonpost(self, request):
        serializer = PartidaAccionInternaSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save(
                mto_actualizado=serializer.validated_data["mto_original"]
            )
            return {"part_acc": serializer.data}
        else:
            return {"error": "No se pudo guardar"}


class PartidaAccionInternaEspecificaView(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("formulacion.add_partidaaccioninterna",)}
    template_name = "formulacion/partida_accion_interna.html"
    json_post = True

    def altget(self, data, pk):
        acciones = AccionInterna.objects.filter(id=pk)
        partidas = Partida.objects.filter(nivel__gte=2,cuenta__startswith="4").order_by("cuenta")
        anio_ejercicio = EjercicioPresupuestario.objects.filter(condicion=0)
        partida_accion = PartidaAccionInterna.objects.filter(accion_interna_id=pk)
        return {"acciones": acciones, "partidas": partidas, "anio_ejercicio": anio_ejercicio, "partida_accion": partida_accion}

    def jsonpost(self, request):
        part_acc = PartidaAccionInternaSerializer(data=request.POST)
        if part_acc.is_valid():
            part_acc.save(mto_actualizado=part_acc.validated_data["mto_original"])
            return {"part_acc": part_acc.data}
        else:
            return {"error": "No se pudo guardar"}


class PartidaAccionInternaDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_partidaaccioninterna",)}
    model = PartidaAccionInterna
    success_url = "../../"
    def get(self, request, *args, **kwargs):
        if self.model and self.success_url:
            obj = get_object_or_404(self.model, pk=kwargs["pk"])
            obj.eliminar()
            return redirect(self.success_url+str(obj.accion_interna_id))
        else:
            raise ValueError("Model and/or SuccessURL don't set")

