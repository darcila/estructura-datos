# creacion de una funcion recursiva. 
# crear funcion recursiva con factoriales 
# 5! = 5*4*3*2*1 = 120

resultado_factorial = 1
for i in range(1,6):
    print(i)
    resultado_factorial = resultado_factorial * i
print(resultado_factorial)

# 5 * 4! -  4 * 3! - 3 * 2! - 2 * 1! - 1 * 0!
# funcion recursiva
def factorial(numero):
    if numero == 1:
        return 1
    return numero * factorial(numero - 1)
print(factorial(5))

# tarea 1 Crear una funcion recursiva que me calcule una multiplicación a base de sumas 
# ejemplo 3 * 5 = 5 + 5 + 5 = 15

#tarea 2 Crear una funcion recursova que calcule una división a base de restas 
# ejemplo 10 / 2 = 10 - 2 - 2 - 2 - 2 - 2 = 5
