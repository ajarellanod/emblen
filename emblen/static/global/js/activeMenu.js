$(document).ready(function(){

    let url = String(window.location);
    let modulo;
    let menu;
    let opcion;

    if(url.indexOf("formulacion") > -1){
      modulo = 'm_formulacion';

      if(url.indexOf("unidades-ejecutoras") > -1){
        menu = 'm_organizacion';
        opcion = 'm_unidades_ejecutoras';
      }
      if(url.indexOf("departamentos") > -1){
        menu = 'm_organizacion';
        opcion = 'm_despartamentos';
      }
      if(url.indexOf("centros-costos") > -1){
        menu = 'm_organizacion';
        opcion = 'm_centros_costos';
      }
      if(url.indexOf("partidas") > -1){
        menu = 'm_organizacion';
        opcion = 'm_partidas';
      }
      
      if( (url.indexOf("programa") > -1) || (url.indexOf("programas") > -1) ){
        menu = 'm_cargaLey';
        opcion = 'm_programas';
      }
      if( (url.indexOf("accion-especifica") > -1) || (url.indexOf("acciones-especificas") > -1) ){
        menu = 'm_cargaLey';
        opcion = 'm_acc_especificas';
      }
      if(url.indexOf("estimacion") > -1){
        menu = 'm_cargaLey';
        opcion = 'm_estimaciones';
      }
      if( (url.indexOf("accion-interna") > -1)  || (url.indexOf("acciones-internas") > -1) ){
        menu = 'm_cargaLey';
        opcion = 'm_acc_internas';
      }
      if(url.indexOf("partida-accion-interna") > -1){
        menu = 'm_cargaLey';
        opcion = 'm_partidas_acc_internas';
      }
      if(url.indexOf("linea-programa") > -1){
        menu = 'm_cargaLey';
        opcion = 'm_lineas_patria';
      }
      if(url.indexOf("plan-desarrollo") > -1){
        menu = 'm_cargaLey';
        opcion = 'm_plan_desarrollo_estadal';
      }
      if(url.indexOf("reporte") > -1){
        menu = 'm_reportes';
        opcion = 'm_r_formulacion';
      }      
      
    }
    else if(url.indexOf("planificacion") > -1){
        modulo = 'm_planificacion';

    
    }
    else if(url.indexOf("ejecucion") > -1){
      modulo = 'm_ejecucion';

  
    }
    else if(url.indexOf("contabilidad") > -1){
      modulo = 'm_contabilidad';

  
    }
    else if(url.indexOf("compras") > -1){
      modulo = 'm_compras';

  
    }
    else if(url.indexOf("tesoreria") > -1){
      modulo = 'm_tesoreria';

  
    }

    $('#'+modulo, ).attr('class','nav-link active');
    $('#'+menu).attr('class','nav-link active-menu ');
    $('#'+menu).click();
    $('#'+opcion).attr('class','nav-link active-option-menu');
  });