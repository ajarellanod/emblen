from django import forms

from apps.contabilidad.models import (
    Comprobante
)


class ComprobanteForm(forms.ModelForm):
    class Meta:
        model = Comprobante
        fields = "__all__"