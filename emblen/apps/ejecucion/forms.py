from django import forms

from apps.ejecucion.models import (
    TiposOrdenPago,
    OrdenesPago,
    DetallesOrdenesPago
)


class TiposOrdenPagoForm(forms.ModelForm):
    class Meta:
        model = TiposOrdenPago
        fields = "__all__"


class OrdenesPagoForm(forms.ModelForm):
    class Meta:
        model = OrdenesPago
        fields = "__all__"


class DetallesOrdenesPagoForm(forms.ModelForm):
    class Meta:
        model = DetallesOrdenesPago
        fields = "__all__"