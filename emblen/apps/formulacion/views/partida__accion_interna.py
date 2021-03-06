from apps.base.views import EmblenView, EmblenPermissionsMixin

from apps.formulacion.models import Partida, AccionInterna
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
