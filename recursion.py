
























def division(dividendo, divisor, cociente=0):
    if dividendo < divisor:
        return cociente, dividendo
    return division(dividendo - divisor, divisor, cociente+1)

print(division(20, 3))