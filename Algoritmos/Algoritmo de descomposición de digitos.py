"""
Descomposición de números:
1. Último al primer dígito
2. Primer al último dígito
"""

# Inicializar variables —————
num1 = dig1 = num2 = dig2 = num = cont = den = pot = 0

# Proceso —————
num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
print("\n")

# Descomposición de número 1 del último a primer dígito
print("Dígitos Número 1: ", end = "")
while num1 != 0:
    dig1 = num1 % 10
    num1 //= 10
    print(dig1, end = "")
print("\n")

# Descomposición de número 2 del primer al último dígito
print("Dígitos del Número 2: ", end = "")

# Obteniendo el denominador base 10
"""
temp = num2
while temp != 0:
    temp //= 10
    cont += 1
    print(cont)
den = 10 ** (cont - 1)
"""

# Obteniendolo por longitud de caracteres
pot = len(str(num2))
den = 10 ** (pot - 1)

while num2 != 0:
    dig2 = num2 // den
    num2 %= den
    den //= 10
    print(dig2, end = "")
print("\n")
