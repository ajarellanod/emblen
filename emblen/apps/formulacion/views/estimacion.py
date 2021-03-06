from django.shortcuts import render, redirect, get_object_or_404
from apps.base.views import EmblenView, EmblenPermissionsMixin, EmblenDeleteView

from apps.formulacion.models import (
    Partida, 
    AccionEspecifica, 
    Estimacion, 
    EjercicioPresupuestario
)
from apps.formulacion.serializers import EstimacionSerializer


class EstimacionView(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("formulacion.add_estimacion",)}
    template_name = "formulacion/estimacion.html"
    json_post = True

    def altget(self, request):
        acciones = AccionEspecifica.objects.all()
        partidas = Partida.objects.exclude(nivel=1)
        return {"acciones": acciones, "partidas": partidas}

    def jsonpost(self, request):
        serializer = EstimacionSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return {"estimacion": serializer.data}
        else:
            return {"error": "No se pudo guardar"}


class Estimacion2View(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("formulacion.add_estimacion",)}
    template_name = "formulacion/estimacion.html"
    json_post = True

    def altget(self, data, pk):
        acciones = AccionEspecifica.objects.filter(id=pk)
        partidas = Partida.objects.filter(nivel=2,cuenta__startswith="4").order_by("cuenta")
        anio_ejercicio = EjercicioPresupuestario.objects.filter(condicion=0)
        estimacion = Estimacion.objects.filter(accion_especifica_id=pk)
        return {"acciones": acciones, "partidas": partidas, "anio_ejercicio": anio_ejercicio,"estimacion": estimacion}

    def jsonpost(self, request):
        estimacion = EstimacionSerializer(data=request.POST)
        if estimacion.is_valid():
            estimacion.save()
            return {"estimacion": estimacion.data}
        else:
            return {"error": "No se pudo guardar"}


class EstimacionDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_estimacion",)}
    model = Estimacion
    success_url = "../../"
    def get(self, request, *args, **kwargs):
        if self.model and self.success_url:
            obj = get_object_or_404(self.model, pk=kwargs["pk"])
            obj.eliminar()
            return redirect(self.success_url+str(obj.accion_especifica_id))
        else:
            raise ValueError("Model and/or SuccessURL don't set")
