from django import forms

from apps.planificacion.models import (
    Modificacion
)


class ModificacionForm(forms.ModelForm):
    class Meta:
        model = Modificacion
        fields = ("partida_accioninterna", "descripcion", "monto", )
