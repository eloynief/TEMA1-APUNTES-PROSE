##borrar si es necesario





def modify_country(id): 

    ##si la petición cumple con el formato de json
    if request.is_json:
                
                return country, 200
    #si no cumple con el formato json 
    return{"error":"Request debe ser punto jota son"},415

