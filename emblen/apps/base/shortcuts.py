# Este archivo contiene funciones para realizar procesos mas rapidamente.

def softdelete_by_object(obj):
    """
    Elimina logicamente los objectos relacionados
    """
    for nombre, _ in obj._meta.fields_map.items():
        try:
            queryset = getattr(obj, nombre).get_queryset()
            softdelete(queryset)
        except AttributeError:
            raise AttributeError(
                "Model {obj._meta.model.__name__} doesn't have define all related names"
            )
            

def softdelete(queryset):
    """
    Elimina logicamente todos los objetos relacionados a un primer queryset.
    """

    # Obtenemos el primer objeto del queryset
    first_object = queryset.first()
    
    if first_object is None:
        return False

    # Iteramos entre todas sus relaciones
    for name, _ in first_object._meta.fields_map.items():
        try:
            # Extraemos el modelo de la relacion
            Model = getattr(first_object, name).model
            
            # Extraemos el nombre de nuestro primer objeto en la clase relacion.
            # Creamos un filtro que nos permitira localizar todos los objeto...
            # de la clase relacion, relacionados con nuestro primer queryset.
            fter = {getattr(first_object, name).field.name + "__in": queryset}

            # Ejecutamos el filtro anterior
            new_queryset = Model.objects.get_queryset().filter(**fter)

            # Repetimos el procedimiento recursivamente
            softdelete(new_queryset)

        except AttributeError:
            raise AttributeError(
                "Model {first_object._meta.model.__name__} doesn't have define all related names"
            )

    # Eliminamos el queryset dado como input
    queryset.eliminar()
