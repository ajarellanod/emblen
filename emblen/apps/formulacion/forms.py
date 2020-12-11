from django import forms
from django.db.models.functions import Substr

from apps.formulacion.models import Partida


class AltModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.nueva_cuenta


class PartidaForm(forms.ModelForm):
    
    codigo_uno = AltModelChoiceField(queryset=Partida.objects.filter(estatus=True, nivel=1).annotate(nueva_cuenta=Substr('cuenta', 1, 1)));
    
    class Meta:
        model = Partida
        fields = ("cuenta","descripcion","nivel", "saldo")

        widgets = {
            'nivel': forms.TextInput(attrs={'readonly': 'readonly'}),
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