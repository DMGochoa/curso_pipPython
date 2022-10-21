import requests

# Funcion para solicitud
def get_categories():
    # Solicitud a la api fake
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    # Imprimir estado, respuesta y tipo de respuesta
    #print(r.status_code) # Status 200 es que todo estuvo OK
    #print(r.text) # Nos retorna una lista con diccionarios
    #print(type(r.text)) # Pero nos indica que es un string y no tiene formato de lista
    categories = r.json() # Dentro de request podemos pasar de un string a un formato json que
    # python lo va poder reconocer y podemos manejarlo.
    print(categories)
    for category in categories:
        print(category['name'])