from rest_framework import serializers

from apps.formulacion.models import Partida
from apps.formulacion.models import CentroCosto


class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partida
        fields = ['id', 'cuenta', 'descripcion', 'saldo']


class CentroCostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroCosto
        fields = ['id', 'codigo', 'nombre']