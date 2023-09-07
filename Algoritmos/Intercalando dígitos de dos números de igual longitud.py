"""
Intercalando dígitos de dos números de igual longitud
"""

# ————— Inicializar variables —————
num1 = dig1 = len1 = num2 = dig2 = len2 = den = pot = 0

# ————— Proceso —————
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))

len1 = len(str(num1))
len2 = len(str(num2))
den = 10 ** (len1 - 1)
print("Número intercalado: ", end = "")

if len1 == len2:
    while (num1 != 0) or (num2 != 0):
        dig1 = num1 // den
        num1 %= den
        print(dig1, end = "")
        dig2 = num2 // den
        num2 %= den
        print(dig2, end = "")
        den //= 10
    print("\n\nFin del programa")
else:
    print("No se puede realizar la operación sin números con igual longitud")
