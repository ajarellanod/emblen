from django import forms

from apps.compras.models import (
    TipoBeneficiario,
    Beneficiario,
    TipoDocumento,
    DocumentoPagar,
    DetalleDocumentoPagar,
    TipoContrato,
    Contrato,
    BeneficiarioContrato,
    ContratoPartida,
    TipoOrden,
    Orden
)


class TipoBeneficiarioForm(forms.ModelForm):
    class Meta:
        model = TipoBeneficiario
        fields = "__all__"


class BeneficiarioForm(forms.ModelForm):
    class Meta:
        model = Beneficiario
        fields = "__all__"


class OrdenForm(forms.ModelForm):
    class Meta:
        model = Orden
        fields = "__all__"

class DocumentoPagarForm(forms.ModelForm):
    class Meta:
        model = DocumentoPagar
        exclude = ("compromiso",)

        