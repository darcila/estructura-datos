class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Pila:
    def __init__(self):
        self.cima = None
    
    def apilar(self, dato):
        nodo = Nodo(dato)
        if self.cima == None:
            self.cima = nodo
            return
        nodo.siguiente = self.cima
        self.cima = nodo
    
    def desapilar(self):
        if self.cima == None:
            return None
        dato = self.cima.dato
        self.cima = self.cima.siguiente
        return dato

pila = Pila()
pila.apilar(7)
pila.apilar(6)
pila.apilar(5)
pila.apilar(4)

print(pila.desapilar())
print(pila.desapilar())
print(pila.desapilar())
print("termino desapilando")