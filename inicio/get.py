import requests

api_url="https://jsonplaceholder.typicode.com/todos/1"
#peticion get
response= requests.get(api_url) ##request de la pagina para obtener sus recursos

print(response.json()) #print en pantalla del json