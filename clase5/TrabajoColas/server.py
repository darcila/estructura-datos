# se debe instalar uvicorn: pip install uvicorn
# se debe instalar FastAPI: pip install fastapi
# se debe instalar pydantic: pip install pydantic
# COmando para ejecutar el servidor uvicorn server:app --reload --port 8080
from fastapi import FastAPI
from paquete.cola import Cola
from paquete import Vehiculo

app = FastAPI()
cola = Cola()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/estado")
def estado():
    elementos = cola.contar()
    return {"status": "ok", "elementos": elementos}

@app.post("/encolar")
def encolar(vehiculo: Vehiculo):
    cola.encolar(vehiculo)
    return {"status": "ok"}

@app.get("/desencolar")
def desencolar():
    elemento = cola.desencolar()
    return {"status": "ok", "elemento": elemento}

@app.get("/ver_todos")
def ver_todos():
    elementos = cola.ver_listado()
    return {"status": "ok", "elementos": elementos}