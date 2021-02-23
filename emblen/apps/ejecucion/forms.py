from django import forms

from apps.ejecucion.models import (
    TipoOrdenPago,
    ClaseOrdenPago,
    OrdenPago
)


class TipoOrdenPagoForm(forms.ModelForm):
    class Meta:
        model = TipoOrdenPago
        fields = "__all__"


class OrdenPagoForm(forms.ModelForm):
    class Meta:
        model = OrdenPago
        fields = ("orden_pago","anio", "tipo","fecha", "clase","contador",
        "unidad_origen","fuente_financiamiento","monto", "descripcion",
        "saldo", "monto_deduciones", "saldo_deducciones", "estatus")

    # documento
    # comprobante
    # comprobante_reverso
    # elaborador
    # verificador
    # anulador
    # reversor