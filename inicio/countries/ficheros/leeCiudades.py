from flask import *

app=Flask(__name__)


import json ##importa las funciones para los archivos json

def leeFichero():
    archivo=open("database.json","r")
    countries=json.load(archivo) #
    archivo.close #se cierra el archivo
    return countries #devuelve las countries

@app.get("/countries/<int:id>")

def get_country(id):
    countries=leeFichero() ##se crea variable que usa el lee fichero

    for country in countries:
        if country['id']==id:
            return country,200
        
    return{"error":"tus muslas"},404