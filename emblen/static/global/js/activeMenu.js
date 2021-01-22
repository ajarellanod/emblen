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
      
      if(url.indexOf("programa") > -1){
        menu = 'm_cargaLey';
        opcion = 'm_programas';
      }
      if(url.indexOf("unidad-especifica") > -1){
        menu = 'm_cargaLey';
        opcion = 'm_acc_especificas';
      }

    }
    else {
      if(url.indexOf("formulacion") > -1){
        modulo = 'm_formulacion';

      }
    }


    $('#'+modulo, ).attr('class','nav-link active');
    $('#'+menu).attr('class','nav-link active-menu ');
    $('#'+menu).click();
    $('#'+opcion).attr('class','nav-link active-option-menu');
  });