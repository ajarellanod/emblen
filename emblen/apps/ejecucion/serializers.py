from rest_framework import serializers

from apps.ejecucion.models import (
    AfectacionPresupuestaria
)




class AfectacionPresupuestariaSerializer(serializers.ModelSerializer):
    codigo_partida = serializers.CharField(source='partida_accioninterna.cuenta', read_only=True)
    
    class Meta:
        model = AfectacionPresupuestaria
        fields = ['id', 'partida_accioninterna', 'anio', 'monto', 'numero','codigo_partida']