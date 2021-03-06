from apps.base.views import EmblenView, EmblenPermissionsMixin

from apps.formulacion.models import Partida, AccionEspecifica
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
            