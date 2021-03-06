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

    def altget(self, request):
        return {'anio_ejercicio': self.anio_ejercicio, 'anio_formulacion': self.anio_formulacion, 'proyectos': self.proyectos, 'acc_centralizadas': self.acc_centralizadas, 'acc_esp_proyectos': self.acc_esp_proyectos, 'acc_esp_acc_centralizadas': self.acc_esp_acc_centralizadas, 'max_proyecto': self.max_proyecto, 'max_especifica': self.max_especifica}
