"""
Composición de número Z con cantidad de dígitos pares,
conformado por el valor absoluto de la diferencia entre sus dígitos extremos.
"""

# ————— Inicializar variables ——————
num = z = dig1 = dig2 = long = den = digz = 0

# ————— Proceso ——————
num = int(input("Número para composición: "))
print("Número Z: ", end = " ")

long = len(str(num))
den = 10 ** (long - 1)

if (long % 2 == 0):
    while num != 0:
        # Dígito de extremo izquierdo
        dig1 = num // den
        #Dígito de extremo derecho
        dig2 = num % 10
        # Valor absoluto de la resta
        digz = abs(dig1 - dig2)
        print(digz, end = "")
        # Valores para próximo cálculo
        num %= den 
        num //= 10
        den //= 100
    print("\n")
else:
    print("Error: Longitud de número impar")