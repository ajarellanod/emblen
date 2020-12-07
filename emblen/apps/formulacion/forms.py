from django import forms

from apps.formulacion.models import Partida


class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = ("cuenta","descripcion","nivel", "saldo")

        widgets = {
            'descripcion': forms.TextInput(),
            'nivel': forms.TextInput(attrs={'readonly': 'readonly'}),
            # 'cuenta': forms.TextInput(attrs={'pattern':'\d*','max': '14'}),
            'cuenta': forms.NumberInput(attrs={'pattern':'\d*','max': '99999999999999'}),
        }

        labels = {
            'cuenta': 'Codigo de Cuenta',
            'descripcion': 'Descripción',
            'nivel': 'Nivel',
            'saldo': 'Saldo',
        }
        
        error_messages  = {
            'cuenta': {
                'unique': ('La cuenta ya existe, por favor verifique.')
            }
        }

        def __init__(self, *args, **kwargs):
            super(PartidaForm, self).__init__(*args, **kwargs)
            self.fields['saldo'].required = False