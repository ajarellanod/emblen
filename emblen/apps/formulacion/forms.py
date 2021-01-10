from django import forms

from apps.formulacion.models import (
    Partida,
    Departamento,
    UnidadEjecutora,
    CentroCosto,
    Programa,
    AccionEspecifica
)


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


class CentroCostoForm(forms.ModelForm):
    class Meta:
        model = CentroCosto
        fields = ("codigo","nombre")


class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        exclude = ("codigo", "anio", "estado", "contador", "duracion")
        
        
class AccionEspecificaForm(forms.ModelForm):
    class Meta:
        model = AccionEspecifica
        exclude = ("codigo", "contador", "duracion")
