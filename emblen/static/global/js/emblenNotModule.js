// //
// Query Functions - For make queries to the server
// //

function postQuery(url, token, data, callback=false, params=false){
  
  // Joining data response with token and json
  data["csrfmiddlewaretoken"] = token;
  data["json"] = true;
  
  $.ajax({
    type: "POST",
    url: url,
    dataType: "json", 
    data: data,
    success: function(response){
      if (callback){
        if (params){
          callback(response, params);
        } else {
          callback(response);
        }  
      }else{
        return response
      }
    },
    error: function(error){
      return error;
    }
  });
}


// //
// Input Functions - For create inputs with masks
// //

function inputCurrency(selector){

  $(selector).each(function(){
    if($(this).val()){
      $(this).val($(this).val().replace(".", ","));
    }
  });

  Inputmask("decimal", {
    positionCaretOnClick: "radixFocus",
    groupSeparator: ".",
    radixPoint: ",",
    _radixDance: true,
    rightAlign: false,
    numericInput: true,
    autoUnmask: true,
    placeholder: "0",
    definitions: {
        "0": {
            validator: "[0-9\uFF11-\uFF19]"
        }
    }
  }).mask($(selector));
}


function inputDate(selector){

  $(selector).each(function(){
    if($(this).val()){
      let values = $(this).val().split("-");
      let value = `${values[2]}/${values[1]}/${values[0]}`
      $(this).val(value)
    }
  });

  Inputmask({alias:"datetime", inputFormat: "dd/mm/yyyy"}).mask(selector);
}


// //
// Tranform Functions - Modify the format of the text
// //

function transformCurrency(str){
  return str.replace(/.{1,3}(?=(.{3})*$)/g, '.\$&')
    .replace("..", ",")
    .replace(/(\.)/, "")
}


function textToCurrency(str, symbol="Bs"){
  return symbol + " " + transformCurrency(str)
}