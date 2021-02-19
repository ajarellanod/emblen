from django import forms

from apps.ejecucion.models import (
    TipoOrdenPago,
    ClaseOrdenPago,
    TipoDocumento,
    DocumentoPagar,
    OrdenPago,
    DeduccionOrdenPago,
    DetalleOrdenPago
)


class TipoOrdenPagoForm(forms.ModelForm):
    class Meta:
        model = TipoOrdenPago
        fields = "__all__"


class OrdenPagoForm(forms.ModelForm):
    class Meta:
        model = OrdenPago
        fields = ("orden_pago","anio", "tipo","fecha", "clase","contador",
        "unidad_origen","fuente_financiamiento","monto","beneficiario", "descripcion","monto_imponible",
        "saldo", "monto_deduciones", "saldo_deducciones", "estatus")
  
    # documento
    # comprobante
    # comprobante_reverso
    # elaborador
    # verificador
    # anulador
    # reversor

class DetalleOrdenPagoForm(forms.ModelForm):
    class Meta:
        model = DetalleOrdenPago
        fields = "__all__"