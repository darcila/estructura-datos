class Vehiculo:

    marca: str
    modelo: int 
    color: str 
    cilindraje: int
    numero_ruedas: int 
    combustible: int

    def __init__(self, marca:str, combustible: int) -> None:
        self.marca = marca 
        self.combustible = combustible

    def __str__(self) -> str:
        return f"La marca del vehiculo es {self.marca} y el nivel de combustible es de {self.combustible}"

    def encender(self):
        pass 

    def acelerar(self):
        pass 

    def frenar(self):
        pass

    def __apagar(self):
        pass


class Moto(Vehiculo):
    pass 

class Carro(Vehiculo):
    pass 



vehiculo1 = Vehiculo('Mazda', 80)
print(vehiculo1)

moto1 = Moto('Honda', 50)
print(moto1)

carro1 = Carro('Renault', 70)
print(carro1)
print(carro1.__apagar())



