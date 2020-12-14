from rest_framework import serializers

from apps.formulacion.models import Partida


class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partida
        fields = ['id', 'cuenta', 'descripcion', 'saldo']