import requests

api_url="https://jsonplaceholder.typicode.com/todos/"
#peticion get

todo={"userId":1,"title":"Compra leshe","completed": False}
response= requests.post(api_url,json=todo) ##request de la pagina para obtener sus recursos
#imprimir el json de la respuesta
print(response.json()) #print en pantalla del json

print("Code:", response.status_code)