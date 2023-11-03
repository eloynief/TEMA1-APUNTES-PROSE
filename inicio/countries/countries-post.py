from flask import *

app=Flask(__name__)

def _find_next_id():

    ##suma 1 a la cantidad de countries por cada country añadida
    return max(country["id"] for country in countries)+1



countries=[
    {"id":1,"name": "cosa rara","capital":"olas","area":513120},
]

@app.post("/countries")

def add_country(): 
    if request.is_json:
        country=request.get_json()

        country ["id"]= _find_next_id()

        ##se añade la country a la countries
        countries.append(country)

        return country,201
    
    return{"error":"Request debe ser punto jota son"},415

