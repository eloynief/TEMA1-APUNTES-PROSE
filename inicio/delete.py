import requests

api_url="https://jsonplaceholder.typicode.com/todos/10"


response= requests.delete(api_url) ##request de la pagina para borrar el recurso que tenga dentro de las ()


#imprimir el json de la respuesta
print(response.status_code)

print(response.json()) #print en pantalla del json