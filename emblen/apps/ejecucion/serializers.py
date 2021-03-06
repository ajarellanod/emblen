from rest_framework import serializers

from apps.ejecucion.models import (
    Modificacion
)




class ModificacionSerializer(serializers.ModelSerializer):
    codigo_partida = serializers.CharField(source='partida_accioninterna.cuenta', read_only=True)
    codigo_orden = serializers.CharField(source='documento_referenciado.orden_pago', read_only=True)
    
    class Meta:
        model = Modificacion
        fields = ['id', 'partida_accioninterna', 'documento_referenciado',
        'anio', 'monto', 'numero','codigo_partida','codigo_orden','descripcion','tipo_modificacion', 'saldo']

 # partida_accioninterna 
    # documento_referenciado 

    # anio
            # monto 
    # numero
       # descripcion 
    # tipo_modificacion
 

    # saldo 


    # exclude = ()
    # exclude = ("descripcion","tipo_modificacion","saldo")