export function activeMenu(modulo, menu, opcion){

    if (modulo.length > 0){
        $("#"+modulo).addClass("active");
    }
    
    if (menu.length > 0){
        $("#"+menu).addClass("active-menu");
        $("#"+menu).click();
    }

    if (opcion.length > 0){
        $("#"+opcion).addClass("active-option-menu");
    }

    
}