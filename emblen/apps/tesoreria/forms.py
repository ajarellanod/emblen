from django import forms

from apps.tesoreria.models import (
    Cuenta
)


class CuentaForm(forms.ModelForm):
    class Meta:
        model = Cuenta
        fields = "__all__"
