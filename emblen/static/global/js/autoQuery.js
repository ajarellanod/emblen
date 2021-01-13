import { postQuery } from "./emblen.js";

$(document).ready(function(){

    // Obteniendo valores del QueryButton 
    let token = $("#queryButton").attr("token");
    let url = $("#queryButton").attr("url");
    let callback = $("#queryButton").attr("callback");

    $('#queryButton').on('click', function() {
        
        let dataInputs = {};

        $('.queryInput').each(function(){
            let name = $(this).attr("name");
            let value = $(this).val();
            dataInputs[name] = value;
        });
 
        $('.queryInputCurrency').each(function(){
            let name = $(this).attr("name");
            let value = parseFloat($(this).inputmask('unmaskedvalue').replace(",", "."));
            dataInputs[name] = value;
        });

        if(callback){
            postQuery(url, token, dataInputs, callbackFunction);
        }else{
            postQuery(url, token, dataInputs);
        }
    });
});