from flask import *

app=Flask(__name__)


countries=[
    {"id":1,"name": "cosa rara","capital":"olas","area":513120},
]

##indica la country para eliminarla >:v
@app.delete("/countries/<int:id>")

##funcion para borrar una country seleccionada entre las countries
def delete_country(id): 

        #buscar el id en concreto que se ha escrito
 for country in countries:
    if country["id"]==id:
        #
        countries.remove(country)

       ##se devuelve vacía para que asi se pueda borrar
    return "{}", 200
    #si no cumple con el formato json 
 return{"error":"Nose encontro la country"},415
