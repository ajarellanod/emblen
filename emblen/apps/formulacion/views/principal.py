from django.db.models import Max

from apps.base.views import EmblenView
from braces.views import LoginRequiredMixin

from apps.formulacion.models import (
    EjercicioPresupuestario,
    Programa,
    AccionEspecifica
)


class PrincipalView(LoginRequiredMixin, EmblenView):
    template_name = "formulacion/principal.html"
    
    def altget(self, request):
        anio_ejercicio = EjercicioPresupuestario.objects.filter(condicion=1)
        anio_formulacion = EjercicioPresupuestario.objects.filter(condicion=0)

        proyectos = Programa.objects.filter(nivel=1).count()
        acc_esp_proyectos = AccionEspecifica.objects.filter(programa__nivel = 1).count()

        acc_centralizadas = Programa.objects.filter(nivel=2).count()
        acc_esp_acc_centralizadas = AccionEspecifica.objects.filter(programa__nivel = 2).count()

        max_proyecto1 = Programa.objects.filter(
                nivel=1
            ).aggregate(Max('id'))

        max_proyecto = Programa.objects.filter(id = max_proyecto1['id__max'])

        max_especifica1 = Programa.objects.filter(
                nivel=2
            ).aggregate(Max('id'))

        max_especifica = Programa.objects.filter(id = max_especifica1['id__max'])
        return {'anio_ejercicio': anio_ejercicio, 'anio_formulacion': anio_formulacion, 'proyectos': proyectos, 'acc_centralizadas': acc_centralizadas, 'acc_esp_proyectos': acc_esp_proyectos, 'acc_esp_acc_centralizadas': acc_esp_acc_centralizadas, 'max_proyecto': max_proyecto, 'max_especifica': max_especifica}
