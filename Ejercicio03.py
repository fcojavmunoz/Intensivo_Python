# Ejercicio 3
#
#
# Enunciado: Crea una función que calcule los números primos entre 1 y N, siendo N el parámetro que recibe la función.
#
#
# Objetivo:
#
#
# - Uso de bucles anidados
# - El uso de colecciones


n = int(input('Introduce un número: '))
comienzo = 1
lista_primos = []

while comienzo <= n:
    contador = 1
    x = 0
    while contador <= comienzo:
        if comienzo % contador == 0:
            x = x + 1
        contador = contador + 1
    if x == 2:
        lista_primos.append(comienzo)
    comienzo = comienzo + 1

print(f'Los números primos entre 1 y {n} son: \n{lista_primos}')
