from django.core.serializers.json import DjangoJSONEncoder

from apps.formulacion.models import Partida

class PartidaSerializer(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, Partida):
            return str(obj)
        return super().default(obj)