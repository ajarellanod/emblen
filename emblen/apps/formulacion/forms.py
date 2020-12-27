from django import forms

from apps.formulacion.models import (Partida, Departamento, UnidadEjecutora)


class PartidaForm(forms.ModelForm):
    class Meta:
        model = Partida
        fields = ("cuenta","descripcion", "saldo")


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ("nombre","codigo", "unidad_ejecutora")


class UnidadEjecutoraForm(forms.ModelForm):
    class Meta:
        model = UnidadEjecutora
        fields = "__all__"