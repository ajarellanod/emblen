from django import forms

from apps.contabilidad.models import (
    CuentaContable,
    AsientoContable
)


class CuentaContableForm(forms.ModelForm):
    class Meta:
        model = CuentaContable
        fields = "__all__"


class AsientoContableForm(forms.ModelForm):
    class Meta:
        model = AsientoContable
        fields = "__all__"