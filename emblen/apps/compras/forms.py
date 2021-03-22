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
    PartidaContrato,
    TipoCompromiso,
    Compromiso
)


class TipoBeneficiarioForm(forms.ModelForm):
    class Meta:
        model = TipoBeneficiario
        fields = "__all__"


class BeneficiarioForm(forms.ModelForm):
    class Meta:
        model = Beneficiario
        fields = "__all__"


class CompromisoForm(forms.ModelForm):
    class Meta:
        model = Compromiso
        fields = "__all__"

class DocumentoPagarForm(forms.ModelForm):
    class Meta:
        model = DocumentoPagar
        exclude = ("compromiso",)

        