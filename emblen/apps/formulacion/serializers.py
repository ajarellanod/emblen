from rest_framework import serializers

from apps.formulacion.models import Partida, CentroCosto, Estimacion


class PartidaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partida
        fields = ['id', 'cuenta', 'descripcion', 'saldo']


class CentroCostoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CentroCosto
        fields = ['id', 'codigo', 'nombre']


class EstimacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estimacion
        fields = ['id', 'accion_especifica', 'partida', 'anio', 'monto']