# ejercicio de clase 4
# crear una linsta enlazada por medio de una funcion recursiva que reciba como parametro el tamaño de la lista
# el dato que contendra cada nodo sera un numero aleatorio. 
import random 

numero1 = random.randint(1, 100)
numero2 = random.randint(1, 100)

print(numero1)
print(numero2)

lista_enlazada = crear_lista(10)


def crear_lista(tamano): 