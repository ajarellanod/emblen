$(document).ready(function () {

  //Variables
  var dict = [];
  var partidaN=[];
  var color=[];


  //Obteneindo las partidas y sus descripciones de un Select oculto
  $("#partida_N1 option").each(function() { // add 
      dict.push({
          key:  $(this).val(),
          value: $(this).text()
    });
  });

  //Mostrando formulario para ingresar nueva partida y deshabilitando boton
  $('#btn_partidaNew').click(function() {
    var estatus=$("#partidaNew3").attr("class");
    if (estatus){
      $("#partidaNew3").attr("class","");
      $("#btn_partidaNew").attr("class","btn btn-sm btn-primary disabled");
    }
  });

  //Función para Verificar la Relación de Partidas
  function revisa_Partida(partida,dict,nivel) {
    partidaN[nivel]=0;
    color[nivel]='black';

    for (let i in dict) {
      if (partida===dict[i]['key']){
        partidaN[nivel]=dict[i]['value'];
      }
    }

    if(partidaN[nivel]===0){
      partidaN[nivel]="<strong style='color:red;'>"+partida+" - PARTIDA NO REGISTRADA</strong>";
      color[nivel]='red';
    }

    switch (nivel) {
      case 1:
        $('#relacion_partidas').html('<strong style="color:'+color[1]+'">Nivel 1: </strong>'+partidaN[1]+'<br>'); 
        break;
      case 2:
        $('#relacion_partidas').html('<strong style="color:'+color[1]+'">Nivel 1: </strong>'+partidaN[1]+'<br><strong style="color:'+color[2]+'">Nivel 2: </strong>'+partidaN[2]+'<br>');
        break;
      case 3:
        $('#relacion_partidas').html('<strong style="color:'+color[1]+'">Nivel 1: </strong>'+partidaN[1]+'<br><strong style="color:'+color[2]+'">Nivel 2: </strong>'+partidaN[2]+'<br><strong style="color:'+color[3]+'">Nivel 3: </strong>'+partidaN[3]+'<br>');
        break;
      case 4:
        $('#relacion_partidas').html('<strong style="color:'+color[1]+'">Nivel 1: </strong>'+partidaN[1]+'<br><strong style="color:'+color[2]+'">Nivel 2: </strong>'+partidaN[2]+'<br><strong style="color:'+color[3]+'">Nivel 3: </strong>'+partidaN[3]+'<br><strong style="color:'+color[4]+'">Nivel 4: </strong>'+partidaN[4]+'<br>');
        break;
      case 5:
        $('#relacion_partidas').html('<strong style="color:'+color[1]+'">Nivel 1: </strong>'+partidaN[1]+'<br><strong style="color:'+color[2]+'">Nivel 2: </strong>'+partidaN[2]+'<br><strong style="color:'+color[3]+'">Nivel 3: </strong>'+partidaN[3]+'<br><strong style="color:'+color[4]+'">Nivel 4: </strong>'+partidaN[4]+'<br><strong style="color:'+color[5]+'">Nivel 5: </strong>'+partidaN[5]+'<br>');
        break;
      case 6:
        $('#relacion_partidas').html('<strong style="color:'+color[1]+'">Nivel 1: </strong>'+partidaN[1]+'<br><strong style="color:'+color[2]+'">Nivel 2: </strong>'+partidaN[2]+'<br><strong style="color:'+color[3]+'">Nivel 3: </strong>'+partidaN[3]+'<br><strong style="color:'+color[4]+'">Nivel 4: </strong>'+partidaN[4]+'<br><strong style="color:'+color[5]+'">Nivel 5: </strong>'+partidaN[5]+'<br><strong style="color:'+color[6]+'">Nivel 6: </strong>'+partidaN[6]+'<br>');
        break;
    }
  } 

  //Verificar la Relación de Partidas
  $('#id_cuenta').bind("keyup blur", function () {
    var codigo_partida= $("#id_cuenta").val();

    if(codigo_partida.length==0){
      $("#tr_relacion_partidas").attr("class","d-none");
      $('#relacion_partidas').html(''); 
    }
    else{
      $("#tr_relacion_partidas").attr("class","");
    }

    if((codigo_partida.length>=1) ){
      partida=codigo_partida.substr(0, 1)+'0000000000000';
      dets_Partida=revisa_Partida(partida,dict,1);

    }
    if((codigo_partida.length>=3) ){
      partida=codigo_partida.substr(0, 3)+'00000000000';
      dets_Partida=revisa_Partida(partida,dict,2);

    }
    if((codigo_partida.length>=5) ){
      partida=codigo_partida.substr(0, 5)+'000000000';
      dets_Partida=revisa_Partida(partida,dict,3);

    }
    if((codigo_partida.length>=7) ){
      partida=codigo_partida.substr(0, 7)+'0000000';
      dets_Partida=revisa_Partida(partida,dict,4);

    }
    if((codigo_partida.length>=9) ){
      partida=codigo_partida.substr(0, 9)+'00000';
      dets_Partida=revisa_Partida(partida,dict,5);
    }
    if((codigo_partida.length>=11) ){
      partida=codigo_partida.substr(0, 11)+'000';
      dets_Partida=revisa_Partida(partida,dict,6);
    }
  });

  //Verificar Nivel de Cuenta
  $('#id_cuenta').blur(function () {
    var codigo_partida= $("#id_cuenta").val();
    digitos=codigo_partida.length;
    while(digitos<14){
      $('#id_cuenta').val(codigo_partida+'0');
      codigo_partida= $("#id_cuenta").val();
      digitos=codigo_partida.length;
    }
    numeroNivel=0;
    if( codigo_partida.substr(0,1)!='0' ){
      numeroNivel=1;
    }

    if (numeroNivel===1){
      if( codigo_partida.substr(1,2)!='00' ){
        numeroNivel=2;
      }
    }

    if (numeroNivel===2){
      if( codigo_partida.substr(3,2)!='00' ){
        numeroNivel=3;
      }
    }

    if (numeroNivel===3){
      if( codigo_partida.substr(5,2)!='00' ){
        numeroNivel=4;
      }
    }

    if (numeroNivel===4){
      if( codigo_partida.substr(7,2)!='00' ){
        numeroNivel=5;
      }
    }
    
    if (numeroNivel===5){
      if( codigo_partida.substr(9,2)!='00' ){
        numeroNivel=6;
      }
    }
    
    if (numeroNivel===6){
      if( codigo_partida.substr(11,3)!='000' ){
        numeroNivel=7;
      }
    }

    $("#id_nivel").val(numeroNivel);
  });

  
  // var input=document.getElementById('id_cuenta');
  // input.addEventListener('input',function(){
  //   if (this.value.length > 14) 
  //     this.value = this.value.slice(0,14); 
  // })
  //Input Number Máximo 14 digitos
  $('#id_cuenta').bind("keyup keypress blur input", function () {
    if (this.value.length > 14) 
      this.value = this.value.slice(0,14); 
  });

  //Input Descripción en Mayúscula al salir
  $('#id_descripcion').blur(function () {
    this.value = this.value.toUpperCase();
  });

});