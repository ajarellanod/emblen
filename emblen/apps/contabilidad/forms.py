from django import forms

from apps.contabilidad.models import (
    CuentaContable,
    Comprobante,
    AsientoContable
)


class ComprobanteForm(forms.ModelForm):
    class Meta:
        model = Comprobante
        fields = "__all__"