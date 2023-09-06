# primer acercamiento a las listas enlazadas
# definicionde una lista enlazada: Una lista enlazada es una estructura de datos lineal en la que los elementos no están almacenados en posiciones contiguas de memoria, sino que cada elemento tiene un puntero al siguiente elemento

numero1 = 5
numero2 = 5 

#print(numero1 == numero2)
#print(type(numero1))
#print(id(numero1))

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


# ejercicio de clase 4
# crear una linsta enlazada por medio de una funcion recursiva que reciba como parametro el tamaño de la lista
# el dato que contendra cada nodo sera un numero aleatorio. 

