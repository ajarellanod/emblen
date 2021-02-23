from django import forms

from apps.tesoreria.models import (
    Banco,
    TipoCuenta,
    Cuenta,
    TipoImpuesto,
    Pago,
    RetencionDeduccion
)


class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = "__all__"
