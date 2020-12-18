from django import forms
from django.db.models.functions import Substr

from apps.formulacion.models import Partida


class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = ("cuenta","descripcion", "saldo")