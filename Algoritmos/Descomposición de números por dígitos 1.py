"""
Aplicación de consola que cree un numero entero formado por los dígitos pares 
de un numero de cedula tomándolos desde el más significativo al menos significativo.

Prueba: 17366821, siendo el resultado 6682
        1298012375, siendo el resultado 2802
"""

# Inicializar variables
# Numero, digito, longitud, potencia
num = dgt = lngt = pot = 0

# Proceso
num = int(input("Número entero a descomponer: "))
lngt = len(str(num))
pot = lngt - 1

print("Longitud de número: ", lngt)
print("Divisor inicial: ", (10 ** pot), "\n")

while num != 0:
    dgt = num // (10 ** pot)
    num = num % (10 ** pot)
    pot -= 1

    if (dgt % 2) == 0:
        print(dgt, end='')

print("\n")

# Salida