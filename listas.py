numeros = list()
continuar: bool = True

def agregar(numero: int) -> None:
    numeros.append(numero)

def eliminar() -> None:
    numeros.pop()

while continuar:
    print("Seleccione una opcion")
    print("1. Agregar un numero")
    print("2. Elimiar la ultima posicion")
    print("3. Salir")

    opcion = int(input())

    if opcion == 3:
        continuar = False
 
