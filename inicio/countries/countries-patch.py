from flask import *

app=Flask(__name__)


countries=[
    {"id":1,"name": "cosa rara","capital":"olas","area":513120},
]

##indica la country para modificar
@app.put("/countries/<int:id>")
@app.patch("/countries/<int:id>")

##funcion para modificar una country seleccionada entre las countries
def modify_country(id): 

    ##si la petición cumple con el formato de json
    if request.is_json:

        #esta variable guarda el json
        ##guarda el json en esta variable
        newCountry=request.get_json()

        for country in countries:
            if country["id"]==id:
                #por cada elemento dentro de newCountry
                for element in newCountry:
                    country[element]=newCountry[element]

                ##se devuele la country si cumple con le formato json
                return country, 200
    #si no cumple con el formato json 
    return{"error":"Request debe ser punto jota son"},415

