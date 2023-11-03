from flask import *

app=Flask(__name__)

@app.route('/')
def index(): #decimos que es lo que muestra al acceder al index
    return 'Hola bro como tas'

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0', port=5050)
