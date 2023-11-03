from flask import *

app=Flask(__name__)


countries=[
    {"id":1,"name": "cosa rara","capital":"olas","area":513120},
    {"id":2,"name": "cosa segunda","capital":"adios","area":7617930},
    {"id":3,"name": "among us","capital":"si","area":1010408},
    {"id":4,"name": "696969","capital":"no","area":123456}
]

@app.route('/')
def index(): #decimos que es lo que muestra al acceder al index
    return countries ##muestra en la pagina las tablas

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port=5050)
