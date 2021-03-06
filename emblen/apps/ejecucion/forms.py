from django import forms

from apps.ejecucion.models import (
    TipoOrdenPago,
    ClaseOrdenPago,
    OrdenPago,
    DocumentoPagar,
    Modificacion
)


class TipoOrdenPagoForm(forms.ModelForm):
    class Meta:
        model = TipoOrdenPago
        fields = "__all__"

class DocumentoPagarForm(forms.ModelForm):
    class Meta:
        model = DocumentoPagar
        exclude = ("compromiso",)


class OrdenPagoForm(forms.ModelForm):
    class Meta:
        model = OrdenPago
        fields = (
            "orden_pago",
            "anio",
            "tipo",
            "fecha",
            "clase",
            "unidad_origen",
            "fuente_financiamiento",
            "monto",
            "descripcion",
            "monto_deduciones",
            "estatus",
            "elaborador",
            "documento_pagar"
        )

class ModificacionForm(forms.ModelForm):
    class Meta:
        model = Modificacion
        exclude = ("descripcion","tipo_modificacion","saldo")