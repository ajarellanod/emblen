from django import forms
from django.db.models.functions import Substr

from apps.formulacion.models import Partida
from apps.formulacion.models import CentroCosto


class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = ("cuenta","descripcion", "saldo")


class CentroCostoForm(forms.ModelForm):
    class Meta:
        model = CentroCosto
        fields = ("codigo","nombre")