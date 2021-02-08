from django import forms

from apps.compras.models import (
    TiposBeneficiario,
    Beneficiario,
    Compromiso
)


class TiposBeneficiarioForm(forms.ModelForm):
    class Meta:
        model = TiposBeneficiario
        fields = "__all__"


class BeneficiarioForm(forms.ModelForm):
    class Meta:
        model = Beneficiario
        fields = "__all__"


class CompromisoForm(forms.ModelForm):
    class Meta:
        model = Compromiso
        fields = "__all__"