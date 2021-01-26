from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView, TemplateView
from django.http import JsonResponse, Http404
from django.db.models.functions import Substr
from braces.views import LoginRequiredMixin

from apps.base.views import (
    EmblenView,
    EmblenPermissionsMixin,
    EmblenDeleteView,
    EmblenFormView
)

from apps.formulacion.serializers import (
    PartidaSerializer,
    CentroCostoSerializer,
    EstimacionSerializer,
    PartidaAccionInternaSerializer
)

from apps.formulacion.forms import (
    PartidaForm,
    DepartamentoForm,
    UnidadEjecutoraForm,
    CentroCostoForm,
    ProgramaForm, 
    AccionEspecificaForm,
    AccionInternaForm,
    LineaProgramaForm,
    PlanDesarrolloForm,
)

from apps.formulacion.models import (
    Partida,
    Departamento,
    UnidadEjecutora,
    CentroCosto,
    Programa,
    AccionEspecifica,
    Estimacion,
    AccionInterna
)


# ----- Formulacion -----

class PrincipalView(LoginRequiredMixin, TemplateView):
    template_name = "formulacion/principal.html"
    

# ----- Partidas -----

class PartidaView(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("formulacion.view_partida",)}
    template_name = "formulacion/partida.html"
    json_post = True
    
    def altget(self, request, pk):
        partida = get_object_or_404(Partida, pk=pk)
        return {"partida": partida}
    
    def jsonpost(self, request, pk):
        partida = get_object_or_404(Partida, pk=pk)
        descripcion = request.POST.get("descripcion")
        if descripcion is not None and descripcion != "":
            partida.descripcion = descripcion        
            partida.save()
            return {"msg": "Partida Guardada Exitosamente", "icon": "success"}
        else:
            return {"msg": "Partida Fallo al Guardar", "icon": "error"}


class PartidaListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_partida",)}
    queryset = Partida.objects.all()
    paginate_by = 8
    template_name = "formulacion/partidas.html"
    success_url = "formulacion:partidas"
    
    
class PartidaDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_partida",)}
    model = Partida
    success_url = 'formulacion:partidas'


class PartidaCreateView(EmblenPermissionsMixin, EmblenView):
    """
    Se crean las partidas de nivel 6 por medio de los auxiliares
    """

    # Variables Necesarias
    permissions = {"all": ("formulacion.add_partida",)}
    template_name = "formulacion/crear_partida.html"
    json_post = True

    # Variables de Ayuda
    partidas = Partida.objects.filter(nivel=1).annotate(option=Substr('cuenta', 1, 1))
    
    def altget(self, request):
        return {'partidas': self.partidas}

    def altpost(self, request):
        # Se reciben los formularios para guardar una nueva partida

        # Comprobando que hayan enviado el saldo
        if request.POST.get("saldo") is not None:

            #Creando el formulario y validandolo
            partida_form = PartidaForm(data=request.POST)
            if partida_form.is_valid():
                partida = partida_form.save(commit=False)
                partida.nivel = 6
                partida.save()
                return redirect('formulacion:partidas')
            else:
                return {'partidas': self.partidas,'form': partida_form}
        else:
            return Http404()

    def jsonpost(self, request):
        # Se manda un json con las partidas serializadas

        try:
            # Obteniendo la partida
            id_partida = int(request.POST.get("data"))
            partida = get_object_or_404(Partida, pk=id_partida)
            
            # Salida
            partida_madre = PartidaSerializer(partida).data
            partidas_hijas = PartidaSerializer(partida.siguientes(), many=True).data
            return {"partida_madre": partida_madre,"partidas_hijas": partidas_hijas}

        # Si existe error transformando el request
        except TypeError:
            return {"partida_madre": "Partida Inexistente","partidas_hijas":[]}


# ----- Centros de Costos ----- 

class CentroCostoView(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("formulacion.view_centro_costo",)}
    template_name = "formulacion/ccosto.html"
    json_post = True
    
    def altget(self, request, pk):
        ccosto = get_object_or_404(CentroCosto, pk=pk)
        return {"ccosto": ccosto}
    
    def jsonpost(self, request, pk):
        ccosto = get_object_or_404(CentroCosto, pk=pk)
        nombre = request.POST.get("nombre")
        if nombre is not None and nombre != "":
            ccosto.nombre = nombre        
            ccosto.save()
            return {"msg": "Centro de Costo Guardado Exitosamente", "icon": "success"}
        else:
            return {"msg": "Centro de Costo Fallo al Guardar", "icon": "error"}


class CentroCostoListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_centro_costo",)}
    queryset = CentroCosto.objects.all()
    paginate_by = 8
    template_name = "formulacion/ccostos.html"
    success_url = "formulacion:centros_costos"
    
    
class CentroCostoDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    """Vista para borrar los centros de costo"""
    permissions = {"all": ("formulacion.delete_centro_costo",)}
    model = CentroCosto
    success_url = 'formulacion:centros_costos'


class CentroCostoCreateView(EmblenPermissionsMixin, EmblenView):
    """
    Se crean los centros de costo de nivel 3 por medio de los auxiliares
    """

    # Variables Necesarias
    permissions = {"all": ("formulacion.add_centro_costo",)}
    template_name = "formulacion/crear_ccosto.html"
    json_post = True

    # Variables de Ayuda
    ccostos = CentroCosto.objects.filter(nivel=1).annotate(option=Substr('codigo', 1, 1))
    
    def altget(self, request):
        return {'ccostos': self.ccostos}

    def altpost(self, request):
        # Se reciben los formularios para guardar un nuevo centro de costo

        #Creando el formulario y validandolo
        ccosto_form = CentroCostoForm(data=request.POST)
        if ccosto_form.is_valid():
            ccosto = ccosto_form.save(commit=False)
            ccosto.nivel = 3
            ccosto.save()
            return redirect('formulacion:centros_costos')
        else:
            return {'ccostos': self.ccostos,'form': ccosto_form}

    def jsonpost(self, request):
        # Se manda un json con los centros de costo serializados

        try:
            # Obteniendo el centro de costo
            id_ccosto = int(request.POST.get("data"))
            ccosto = get_object_or_404(CentroCosto, pk=id_ccosto)
            
            # Salida
            ccosto_madre = CentroCostoSerializer(ccosto).data
            ccostos_hijas = CentroCostoSerializer(ccosto.siguientes(), many=True).data
            return {"ccosto_madre": ccosto_madre,"ccostos_hijas": ccostos_hijas}

        # Si existe error transformando el request
        except TypeError:
            return {"ccosto_madre": "Centro de Costo Inexistente","ccostos_hijas":[]}


# ----- Departamentos -----

class DepartamentoView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.view_departamento",)}
    template_name = "formulacion/departamento.html"
    form_class = DepartamentoForm
    instance_model = Departamento
    success_url = "formulacion:departamentos"


class DepartamentoListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_departamento",)}
    template_name = "formulacion/departamentos.html"
    success_url = "formulacion:departamentos"
    queryset = Departamento.objects.all().order_by("codigo")
    paginate_by = 8
    

class DepartamentoCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_departamento",)}
    template_name = "formulacion/departamento.html"
    form_class = DepartamentoForm
    success_url = "formulacion:departamentos"


class DepartamentoDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_departamento",)}
    model = Departamento
    success_url = "formulacion:departamentos"


# ----- Unidades Ejecutoras -----

class UnidadEjecutoraView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.view_unidadejecutora",)}
    template_name = "formulacion/unidad_ejecutora.html"
    form_class = UnidadEjecutoraForm
    instance_model = UnidadEjecutora
    success_url = "formulacion:unidades_ejecutoras"


class UnidadEjecutoraListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_unidadejecutora",)}
    template_name = "formulacion/unidades_ejecutoras.html"
    success_url = "formulacion:unidades_ejecutoras"
    queryset = UnidadEjecutora.objects.all().order_by("codigo")
    paginate_by = 8


class UnidadEjecutoraCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_unidadejecutora",)}
    template_name = "formulacion/unidad_ejecutora.html"
    form_class = UnidadEjecutoraForm
    success_url = "formulacion:unidades_ejecutoras"


class UnidadEjecutoraDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_unidadejecutora",)}
    model = UnidadEjecutora
    success_url = "formulacion:unidades_ejecutoras"


# ----- Programas -----

class ProgramaListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_programa",)}
    template_name = "formulacion/programas.html"
    success_url = "formulacion:programas"
    queryset = Programa.objects.all().order_by("codigo")
    paginate_by = 8


class ProgramaView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.view_programa",)}
    template_name = "formulacion/crear_programa.html"
    instance_model = Programa
    form_class = ProgramaForm
    success_url = "formulacion:programas"

    def altpost(self, request, pk, *args, **kwargs):
        programa = get_object_or_404(self.instance_model, pk=pk)
        new_request = request.POST.copy()
        new_request.update({
            "nivel": programa.nivel, 
            "responsable": programa.responsable.id
        })

        form = self.form_class(instance=programa, data=new_request)

        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return {"form":form}
            
class ProgramaCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_programa",)}
    template_name = "formulacion/crear_programa.html"
    form_class = ProgramaForm
    success_url = "formulacion:programas"

    def form_valid(self, form):
        programa = form.save(commit=False)
        programa.gen_rest_attrs()
        return super().form_valid(programa)


class ProgramaDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_programa",)}
    model = Programa
    success_url = "formulacion:programas"

    
# ----- AccionEspecifica -----

class AccionEspecificaListView(EmblenPermissionsMixin, ListView):
    permissions = {"all": ("formulacion.view_accionespecifica",)}
    template_name = "formulacion/acciones_especificas.html"
    success_url = "formulacion:acciones_especificas"
    queryset = AccionEspecifica.objects.all().order_by("codigo")
    paginate_by = 8


class AccionEspecificaView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.change_accionespecifica",)}
    template_name = "formulacion/crear_accion_especifica.html"
    instance_model = AccionEspecifica
    form_class = AccionEspecificaForm
    success_url = "formulacion:acciones_especificas"
    
    def altpost(self, request, pk, *args, **kwargs):
        accion = get_object_or_404(self.instance_model, pk=pk)
        new_request = request.POST.copy()
        new_request.update({
            "programa": accion.programa, 
            "responsable": accion.responsable.id
        })

        form = self.form_class(instance=accion, data=new_request)

        if form.is_valid():
            form.save()
            return redirect(self.success_url)
        else:
            return {"form":form}


class AccionEspecificaCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_accionespecifica",)}
    template_name = "formulacion/crear_accion_especifica.html"
    form_class = AccionEspecificaForm
    success_url = "formulacion:acciones_especificas"
    
    def form_valid(self, form):
        accion_especifica = form.save(commit=False)
        accion_especifica.gen_rest_attrs()
        return super().form_valid(accion_especifica)


class AccionEspecificaDeleteView(EmblenPermissionsMixin, EmblenDeleteView):
    permissions = {"all": ("formulacion.delete_accionespecifica",)}
    model = AccionEspecifica
    success_url = "formulacion:acciones_especificas"


# ----- Estimacion -----

class EstimacionView(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("formulacion.add_estimacion",)}
    template_name = "formulacion/estimacion.html"
    json_post = True

    def altget(self, request):
        acciones = AccionEspecifica.objects.all()
        partidas = Partida.objects.exclude(nivel=1)
        return {"acciones": acciones, "partidas": partidas}

    def jsonpost(self, request):
        estimacion = EstimacionSerializer(data=request.POST)
        if estimacion.is_valid():
            estimacion.save()
            return {"estimacion": estimacion.data}
        else:
            return {"error": "No se pudo guardar"}


# ----- Acción Interna -----

class AccionInternaCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_accioninterna",)}
    template_name = "formulacion/crear_accion_interna.html"
    form_class = AccionInternaForm
    success_url = "formulacion:principal"

    def form_valid(self, form):
        accion_interna = form.save(commit=False)
        accion_interna.gen_rest_attrs()
        return super().form_valid(accion_interna)


# ----- PartidaAccionInterna -----

class PartidaAccionInternaView(EmblenPermissionsMixin, EmblenView):
    permissions = {"all": ("formulacion.add_partidaaccioninterna",)}
    template_name = "formulacion/partida_accion_interna.html"
    json_post = True

    def altget(self, request):
        acciones = AccionInterna.objects.all()
        partidas = Partida.objects.exclude(nivel=1)
        return {"acciones": acciones, "partidas": partidas}

    def jsonpost(self, request):
        part_acc = PartidaAccionInternaSerializer(data=request.POST)
        if part_acc.is_valid():
            part_acc.save(mto_actualizado=part_acc.validated_data["mto_original"])
            return {"part_acc": part_acc.data}
        else:
            return {"error": "No se pudo guardar"}


# ----- Linea Programa -----

class LineaProgramaCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_lineaprograma",)}
    template_name = "formulacion/crear_linea_programa.html"
    form_class = LineaProgramaForm
    success_url = "formulacion:principal"

    def form_valid(self, form):
        linea_programa = form.save(commit=False)
        linea_programa.gen_rest_attrs()
        return super().form_valid(linea_programa)


# ----- Plan de Desarrollo -----

class PlanDesarrolloCreateView(EmblenPermissionsMixin, EmblenFormView):
    permissions = {"all": ("formulacion.add_plandesarrollo",)}
    template_name = "formulacion/crear_plan_desarrollo.html"
    form_class = PlanDesarrolloForm
    success_url = "formulacion:principal"

    def form_valid(self, form):
        plan_desarrollo = form.save(commit=False)
        plan_desarrollo.gen_rest_attrs()
        return super().form_valid(plan_desarrollo)