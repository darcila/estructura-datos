from pydantic import BaseModel

class Pruebas(BaseModel):
    nombre: str # Nombre de la prueba tecnica
    resultado: bool # Resultado de la prueba tecnica True si paso, False si no paso

class Vehiculo(BaseModel):
    tipo: str # Tipo de vehiculo (moto, carro, camion, etc)
    matricula: str # Matrcula o placa del vehiculo
    color: str # Color del vehiculo
    marca: str # Marca del vehiculo
    kilometraje: int # Kilometraje del vehiculo
    pruebas: list[Pruebas]  # Arreglo de pruebas tecnicas
    