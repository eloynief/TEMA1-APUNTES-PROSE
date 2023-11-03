import requests

#
api_url="https://jsonplaceholder.typicode.com/todos/10"

#peticion get
response= requests.get(api_url) ##request de la pagina para obtener sus recursos

print(response.json()) #print en pantalla del json



#
todo={"userId":1,"title":"Compra leshe","completed": False}

#peticion put
response= requests.put(api_url,json=todo) ##request de la pagina para obtener sus recursos


#imprimir el json de la respuesta
print(response.json()) #print en pantalla del json

print(response.status_code)