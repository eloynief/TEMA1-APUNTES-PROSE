import requests

api_url="https://jsonplaceholder.typicode.com/todos/10"
#peticion get

#modifica los elementos elegidos
todo={"title":"Compra leshe","completed": False}


response= requests.patch(api_url,json=todo) ##request de la pagina para obtener sus recursos
#imprimir el json de la respuesta
print(response.json()) #print en pantalla del json

print("Code:", response.status_code)