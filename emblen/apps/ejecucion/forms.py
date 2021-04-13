from django import forms

from apps.ejecucion.models import (
    TipoOrdenPago,
    ClaseOrdenPago,
    OrdenPago,
    AfectacionPresupuestaria
)


class TipoOrdenPagoForm(forms.ModelForm):
    class Meta:
        model = TipoOrdenPago
        fields = "__all__"


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

class AfectacionPresupuestariaForm(forms.ModelForm):
    class Meta:
        model = AfectacionPresupuestaria
        fields = "__all__"