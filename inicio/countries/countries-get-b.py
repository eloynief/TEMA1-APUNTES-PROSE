from flask import *

app=Flask(__name__)

countries=[
    {"id":1,"name": "cosa rara","capital":"olas","area":513120},
    {"id":2,"name": "cosa segunda","capital":"adios","area":7617930},
    {"id":3,"name": "among us","capital":"si","area":1010408},
    {"id":4,"name": "696969","capital":"no","area":123456}
]

@app.get("/countries/<int:id>")

def get_country(id): 
    
    for country in countries:
        if country['id']==id:
            return country,200
        
    return {"error":"Country not found"},404


