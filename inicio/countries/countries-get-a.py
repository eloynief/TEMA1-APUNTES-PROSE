from flask import *

app=Flask(__name__)

countries=[
    {"id":1,"name": "cosa rara","capital":"olas","area":513120},
    {"id":2,"name": "cosa segunda","capital":"adios","area":7617930},
    {"id":3,"name": "among us","capital":"si","area":1010408},
    {"id":4,"name": "696969","capital":"no","area":123456}
]

@app.get("/countries")

def get_countries(): 
    return jsonify(countries)