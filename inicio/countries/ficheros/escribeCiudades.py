from flask import *

app=Flask(__name__)


import json ##importa las funciones para los archivos json

def _find_next_id():

    ##suma 1 a la cantidad de countries por cada country añadida
    return max(country["id"] for country in countries)+1


def escribeFichero():
    archivo=open("database.json","r")
    countries=json.load(archivo) #
    archivo.close #se cierra el archivo
    return countries #devuelve las countries

@app.get("/countries/<int:id>")

def get_country(id):
    countries=escribeFichero() ##se crea variable que usa el lee fichero

    for country in countries:
        if country['id']==id:
            return country,200
        
    return{"error":"tus muslas"},404



def add_country(): 

    countries=escribeFichero()

    if request.is_json:
        country=request.get_json()

        country ["id"]= _find_next_id()

        ##se añade la country a la countries
        countries.append(country)
        escribeFichero(countries)
        
        ##
        return country,201
    
    return{"error":"Request debe ser punto jota son"},415

