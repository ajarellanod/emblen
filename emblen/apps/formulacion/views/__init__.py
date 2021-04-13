# Formulacion Views

from .principal import PrincipalView

from .estimacion import EstimacionView, Estimacion2View, EstimacionDeleteView

from .partida__accion_interna import (
    PartidaAccionInternaView,
    PartidaAccionInternaEspecificaView,
    PartidaAccionInternaDeleteView
)

from .accion_especifica import (
    AccionEspecificaListView,
    AccionEspecificaCreateView,
    AccionEspecificaView,
    AccionEspecificaDeleteView
)

from .accion_interna import (
    AccionInternaListView,
    AccionInternaCreateView,
    AccionInternaView,
    AccionInternaDeleteView
)

from .centro_costo import (
    CentroCostoListView,
    CentroCostoCreateView,
    CentroCostoView,
    CentroCostoDeleteView
)

from .departamento import (
    DepartamentoListView,
    DepartamentoCreateView,
    DepartamentoView,
    DepartamentoDeleteView
)

from .programa import (
    ProgramaListView,
    ProgramaCreateView,
    ProgramaView,
    ProgramaDeleteView
)

from .linea_programa import (
    LineaProgramaListView,
    LineaProgramaCreateView,
    LineaProgramaView,
    LineaProgramaDeleteView
)

from .partida import (
    PartidaListView,
    PartidaCreateView,
    PartidaView,
    PartidaDeleteView
)

from .plan_desarrollo import (
    PlanDesarrolloListView,
    PlanDesarrolloCreateView,
    PlanDesarrolloView,
    PlanDesarrolloDeleteView
)

from .unidad_ejecutora import (
    UnidadEjecutoraListView,
    UnidadEjecutoraCreateView,
    UnidadEjecutoraView,
    UnidadEjecutoraDeleteView
)

from .ingreso_presupuestario import (
    IngresoListView,
    IngresoCreateView,
    IngresoView,
    IngresoDeleteView
)


from .ejercicio_presupuestario import (
    EjercicioPresupuestarioListView,
    EjercicioPresupuestarioCreateView,
    EjercicioPresupuestarioView,
    EjercicioPresupuestarioDeleteView
)
