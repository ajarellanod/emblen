from django import forms

from apps.formulacion.models import Partida


class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = ("cuenta","descripcion","nivel", "saldo")

        widgets = {
            'descripcion': forms.TextInput(),
        }

        labels = {
            'cuenta': 'Codigo de Cuenta',
            'descripcion': 'Descripción',
            'nivel': 'Nivel',
            'saldo': 'Saldo',
        }

        def __init__(self, *args, **kwargs):
            super(PartidaForm, self).__init__(*args, **kwargs)
            self.fields['saldo'].required = False