import { inputCurrency, inputDate } from "./emblen.js";

$(document).ready(function(){

    // Turn on all elements with this classes
    inputCurrency(".inputCurrency");
    inputDate(".inputDate");


    // Listen closest form for submit
    $(".inputCurrency").closest("form").on("submit", function(){
        $('.inputCurrency').each(function(){
            $(this).inputmask("remove");
            let value = parseFloat($(this).inputmask('unmaskedvalue').replace(",", "."));
            $(this).val(value);
        });
    });

});

