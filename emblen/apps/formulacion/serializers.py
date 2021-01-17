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
    codigo_accion = serializers.CharField(source='accion_especifica.codigo', read_only=True)
    codigo_partida = serializers.CharField(source='partida.cuenta', read_only=True)

    class Meta:
        model = Estimacion
        fields = ['id', 'accion_especifica', 'partida', 'anio', 'monto', 'codigo_accion', 'codigo_partida']