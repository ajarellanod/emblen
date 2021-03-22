from django import forms

from apps.planificacion.models import (
    ModificacionGasto,
    ModificacionIngreso,
)


class ModificacionGastoForm(forms.ModelForm):
    class Meta:
        model = ModificacionGasto
        fields = ("partida_accioninterna", "descripcion", "monto", "tipo_modificacion")
