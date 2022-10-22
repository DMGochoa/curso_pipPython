import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse

"""
Para ejecutar esto como un server toca ejecutar el comando
uvicorn web-server/main:app --reload
"""

app = FastAPI()

# Funcion en laque se devuelve un valor
# el decurador indica la ruta
@app.get('/')
def get_list():
    return [1,2,3,]

# en el response se especifica que se envia un html
@app.get('/contact', response_class=HTMLResponse)
def get_pagina():
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()