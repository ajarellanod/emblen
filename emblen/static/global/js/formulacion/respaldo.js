
$("#id_cuenta").keyup(function(){
  

});

$('#id_cuenta').focusout(function() {

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





$('#partida_N1 option:selected').attr("selected",false);
var valor1=$("#partida_N1 option[value="+ nivel1 +"]");
if(valor1.length){
  $("#partida_N1 option[value="+ nivel1 +"]").attr("selected",true);
  var desc_nivel1=$('#partida_N1 option:selected').text();
  if(codigo_partida.length<3){
    $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br>'); 
  }
}
else{
  $('#relacion_partidas').html('<strong style="color:red;">Nivel 1: '+nivel1+' - PARTIDA NO REGISTRADA</strong><br>'); 
}     


if(codigo_partida.length>=3){
nivel2=codigo_partida.substr(0, 3)+'00000000000';
$('#partida_N2 option:selected').attr("selected",false);
var valor2=$("#partida_N2 option[value="+ nivel2 +"]");
if(valor2.length){    
  $("#partida_N2 option[value="+ nivel2 +"]").attr("selected",true);
  var desc_nivel2=$('#partida_N2 option:selected').text();
  if(codigo_partida.length<5){
    $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br>'); 
  }
}
else{
  $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong style="color:red;">Nivel 2: '+nivel2+' - PARTIDA NO REGISTRADA</strong><br>'); 
}    
} 

if(codigo_partida.length>=5){
nivel3=codigo_partida.substr(0, 5)+'000000000';
$('#partida_N3 option:selected').attr("selected",false);
var valor3=$("#partida_N3 option[value="+ nivel3 +"]");
if(valor3.length){
  $("#partida_N3 option[value="+ nivel3 +"]").attr("selected",true);
  var desc_nivel3=$('#partida_N3 option:selected').text();
  if(codigo_partida.length<7){
    $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br>'); 
  }
}
else{
  $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong style="color:red;">Nivel 3: '+nivel3+' - PARTIDA NO REGISTRADA</strong><br>'); 
}
}

if(codigo_partida.length>=7){
nivel4=codigo_partida.substr(0, 7)+'0000000';
$('#partida_N4 option:selected').attr("selected",false);
var valor4=$("#partida_N4 option[value="+ nivel4 +"]");
if(valor4.length){
  $("#partida_N4 option[value="+ nivel4 +"]").attr("selected",true);
  var desc_nivel4=$('#partida_N4 option:selected').text();
  if(codigo_partida.length<9){
    $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong>Nivel 4: </strong>'+desc_nivel4+'<br>'); 
  }      
}
else{
  $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong style="color:red;">Nivel 4: '+nivel4+' - PARTIDA NO REGISTRADA</strong><br>'); 
} 
}

if(codigo_partida.length>=9){
nivel5=codigo_partida.substr(0, 9)+'00000';
$('#partida_N5 option:selected').attr("selected",false);
var valor5=$("#partida_N5 option[value="+ nivel5 +"]");
if(valor5.length){
  $("#partida_N5 option[value="+ nivel5 +"]").attr("selected",true);
  var desc_nivel5=$('#partida_N5 option:selected').text();
  if(codigo_partida.length<11){
    $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong>Nivel 4: </strong>'+desc_nivel4+'<br><strong>Nivel 5: </strong>'+desc_nivel5+'<br>'); 
  }
}
else{
  $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong>Nivel 4: </strong>'+desc_nivel4+'<br><strong style="color:red;">Nivel 5: '+nivel5+' - PARTIDA NO REGISTRADA</strong><br>'); 
}    
}

if(codigo_partida.length>=11){
nivel6=codigo_partida.substr(0, 11)+'000';
$('#partida_N6 option:selected').attr("selected",false);
var valor6=$("#partida_N6 option[value="+ nivel6 +"]");
if(valor6.length){    
  $("#partida_N6 option[value="+ nivel6 +"]").attr("selected",true);
  var desc_nivel6=$('#partida_N6 option:selected').text();
  $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong>Nivel 4: </strong>'+desc_nivel4+'<br><strong>Nivel 5: </strong>'+desc_nivel5+'<br><strong>Nivel 6: </strong>'+desc_nivel6)+'<br>'; 
}
else{
  if (desc_nivel1 === undefined) {
    $('#relacion_partidas').html('<strong style="color:red;">Nivel 1: '+nivel1+' - PARTIDA NO REGISTRADA</strong><br>'); 
  }
  else
  {
    if (desc_nivel2 === undefined) {
      $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong style="color:red;">Nivel 2: '+nivel2+' - PARTIDA NO REGISTRADA</strong><br>');  
    }
    else{
      if (desc_nivel3 === undefined) {
        $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong style="color:red;">Nivel 3: '+nivel3+' - PARTIDA NO REGISTRADA</strong><br>'); 
      }
      else{
        if (desc_nivel4 === undefined) {
          $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong style="color:red;">Nivel 4: '+nivel4+' - PARTIDA NO REGISTRADA</strong><br>'); 
        }
        else{
          if (desc_nivel5 === undefined) {
            $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong>Nivel 4: </strong>'+desc_nivel4+'<br><strong style="color:red;">Nivel 5: '+nivel5+' - PARTIDA NO REGISTRADA</strong><br>');
          }
          else{
            $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong>Nivel 4: </strong>'+desc_nivel4+'<br><strong>Nivel 5: </strong>'+desc_nivel5+'<br><strong style="color:red;">Nivel 6: '+nivel6+' - PARTIDA NO REGISTRADA</strong><br>'); 
          }
        }
      }
    }
  }

}     
}



// Segunda parte


if((codigo_partida.length>=1) ){
    nivel1=codigo_partida.substr(0, 1)+'0000000000000';
    $('#partida_N1 option:selected').attr("selected",false);
    var valor1=$("#partida_N1 option[value="+ nivel1 +"]");
    if(valor1.length){
      $("#partida_N1 option[value="+ nivel1 +"]").attr("selected",true);
      var desc_nivel1=$('#partida_N1 option:selected').text();
      if(codigo_partida.length<3){
        $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br>'); 
      }
    }
    else{
      $('#relacion_partidas').html('<strong style="color:red;">Nivel 1: '+nivel1+' - PARTIDA NO REGISTRADA</strong><br>'); 
    }     
  }

  if(codigo_partida.length>=3){
    nivel2=codigo_partida.substr(0, 3)+'00000000000';
    $('#partida_N2 option:selected').attr("selected",false);
    var valor2=$("#partida_N2 option[value="+ nivel2 +"]");
    if(valor2.length){    
      $("#partida_N2 option[value="+ nivel2 +"]").attr("selected",true);
      var desc_nivel2=$('#partida_N2 option:selected').text();
      if(codigo_partida.length<5){
        $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br>'); 
      }
    }
    else{
      $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong style="color:red;">Nivel 2: '+nivel2+' - PARTIDA NO REGISTRADA</strong><br>'); 
    }    
  } 

  if(codigo_partida.length>=5){
    nivel3=codigo_partida.substr(0, 5)+'000000000';
    $('#partida_N3 option:selected').attr("selected",false);
    var valor3=$("#partida_N3 option[value="+ nivel3 +"]");
    if(valor3.length){
      $("#partida_N3 option[value="+ nivel3 +"]").attr("selected",true);
      var desc_nivel3=$('#partida_N3 option:selected').text();
      if(codigo_partida.length<7){
        $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br>'); 
      }
    }
    else{
      $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong style="color:red;">Nivel 3: '+nivel3+' - PARTIDA NO REGISTRADA</strong><br>'); 
    }
  }

  if(codigo_partida.length>=7){
    nivel4=codigo_partida.substr(0, 7)+'0000000';
    $('#partida_N4 option:selected').attr("selected",false);
    var valor4=$("#partida_N4 option[value="+ nivel4 +"]");
    if(valor4.length){
      $("#partida_N4 option[value="+ nivel4 +"]").attr("selected",true);
      var desc_nivel4=$('#partida_N4 option:selected').text();
      if(codigo_partida.length<9){
        $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong>Nivel 4: </strong>'+desc_nivel4+'<br>'); 
      }      
    }
    else{
      $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong style="color:red;">Nivel 4: '+nivel4+' - PARTIDA NO REGISTRADA</strong><br>'); 
    } 
  }

  if(codigo_partida.length>=9){
    nivel5=codigo_partida.substr(0, 9)+'00000';
    $('#partida_N5 option:selected').attr("selected",false);
    var valor5=$("#partida_N5 option[value="+ nivel5 +"]");
    if(valor5.length){
      $("#partida_N5 option[value="+ nivel5 +"]").attr("selected",true);
      var desc_nivel5=$('#partida_N5 option:selected').text();
      if(codigo_partida.length<11){
        $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong>Nivel 4: </strong>'+desc_nivel4+'<br><strong>Nivel 5: </strong>'+desc_nivel5+'<br>'); 
      }
    }
    else{
      $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong>Nivel 4: </strong>'+desc_nivel4+'<br><strong style="color:red;">Nivel 5: '+nivel5+' - PARTIDA NO REGISTRADA</strong><br>'); 
    }    
  }

  if(codigo_partida.length>=11){
    nivel6=codigo_partida.substr(0, 11)+'000';
    $('#partida_N6 option:selected').attr("selected",false);
    var valor6=$("#partida_N6 option[value="+ nivel6 +"]");
    if(valor6.length){    
      $("#partida_N6 option[value="+ nivel6 +"]").attr("selected",true);
      var desc_nivel6=$('#partida_N6 option:selected').text();
      $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong>Nivel 4: </strong>'+desc_nivel4+'<br><strong>Nivel 5: </strong>'+desc_nivel5+'<br><strong>Nivel 6: </strong>'+desc_nivel6)+'<br>'; 
    }
    else{
      $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong>Nivel 4: </strong>'+desc_nivel4+'<br><strong>Nivel 5: </strong>'+desc_nivel5+'<br><strong style="color:red;">Nivel 6: '+nivel6+' - PARTIDA NO REGISTRADA</strong><br>'); 
    }     
  }

  
  // nivel1=codigo_partida.substr(0, 1)+'0000000000000';
  // $("#partida_N1 option[value="+ nivel1 +"]").attr("selected",true);
  // var desc_nivel1=$('#partida_N1 option:selected').text();

  // nivel2=codigo_partida.substr(0, 3)+'00000000000';;
  // $("#partida_N2 option[value="+ nivel2 +"]").attr("selected",true);
  // var desc_nivel2=$('#partida_N2 option:selected').text();

  // nivel3=codigo_partida.substr(0, 5)+'000000000';
  // $("#partida_N3 option[value="+ nivel3 +"]").attr("selected",true);
  // var desc_nivel3=$('#partida_N3 option:selected').text();

  // nivel4=codigo_partida.substr(0, 7)+'0000000';
  // $("#partida_N4 option[value="+ nivel4 +"]").attr("selected",true);
  // var desc_nivel4=$('#partida_N4 option:selected').text();

  // nivel5=codigo_partida.substr(0, 9)+'00000';
  // $("#partida_N5 option[value="+ nivel5 +"]").attr("selected",true);
  // var desc_nivel5=$('#partida_N5 option:selected').text();

  // nivel6=codigo_partida.substr(0, 11)+'000';
  // $("#partida_N6 option[value="+ nivel6 +"]").attr("selected",true);
  // var desc_nivel6=$('#partida_N6 option:selected').text();

  // $('#relacion_partidas').html('<strong>Nivel 1: </strong>'+desc_nivel1+'<br><strong>Nivel 2: </strong>'+desc_nivel2+'<br><strong>Nivel 3: </strong>'+desc_nivel3+'<br><strong>Nivel 4: </strong>'+desc_nivel4+'<br><strong>Nivel 5: </strong>'+desc_nivel5+'<br><strong>Nivel 6: </strong>'+desc_nivel6)+'<br>'; 











  ////////////////////////////ULTIMO


  $(document).ready(function () {
    $('#btn_partidaNew').click(function() { 
      // var form_idx = $('#id_form-TOTAL_FORMS').val(); 
      var estatus=$("#partidaNew3").attr("class");
      if (estatus){
        $("#partidaNew3").attr("class","");
        $("#btn_partidaNew").attr("class","btn btn-sm btn-primary disabled");
      }
      // else{
      //   valor = $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1); 
      //   $('#partidaNew2').append($('#partidaNew').html().replace(/__prefix__/g, form_idx)); 
      // }
    
    });
    // $( "#btn_partidaNew" ).click(function() {
    //     // $( "#book" ).hide( "slow", function() {
    //     //   alert( "Animation complete." );
    //     // });
    //     $('#partidaNew').toggle();
    //   });
    
    
    // $('.btn_partidaUpd').click(function() {
    //   cuenta=$(this).val();
    //   var form_idx = $('#id_form-TOTAL_FORMS').val(); 
    //   var estatus=$("#partidaNew3").attr("class");
    //   if (estatus){
    //     $("#partidaNew3").attr("class","");
    //   }
    //   else{
    //     valor = $('#id_form-TOTAL_FORMS').val(parseInt(form_idx) + 1); 
    //     $('#partidaNew2').append($('#partidaNew').html().replace(/__prefix__/g, form_idx)); 
    //   }
    
    // });
    
    
    var dict = [];
    var partidaN=[];
    var color=[];
    $("#partida_N1 option").each(function() { // add 
        dict.push({
            key:  $(this).val(),
            value: $(this).text()
      });
    });
    
    function revisa_Partida(partida,dict,nivel) {
      partidaN[nivel]=0;
      color[nivel]='black';
    
      for (let i in dict) {
        if (partida===dict[i]['key']){
          partidaN[nivel]=dict[i]['value'];
        }
        else{
          
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
        default:
          text = "No value found";
      }
    
    }
    
    $('#id_cuenta').bind("keyup", function () {
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
    
    function busqueda_nivel(codigo_partida){
      if(codigo_partida.substr(9,2)=='00'){
        numeroNivel=6;
      }
      else{
        numeroNivel=5;
      }
    
      if(codigo_partida.substr(7,2)=='00'){
        numeroNivel=4;
      }
      else{
        numeroNivel=3;
      }
    
      if(codigo_partida.substr(5,2)=='00'){
        numeroNivel=3;
      }
      else{
        numeroNivel=2;
      }
      
      if(codigo_partida.substr(3,2)=='00'){
        numeroNivel=2;
      }        
      else{
        numeroNivel=1;
      }
      
      if(codigo_partida.substr(1,2)=='00'){
        numeroNivel=1;
      }
    
    }
    
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
    
    var input=  document.getElementById('id_cuenta');
    input.addEventListener('input',function(){
      if (this.value.length > 14) 
         this.value = this.value.slice(0,14); 
    })
    
    
      $('#id_descripcion').blur(function () {
        this.value = this.value.toUpperCase();
      });
    
    });