"""
Serie 2

Desarrolle la siguiente serie:
S = (2X / 2!) - (3X / 3!) + (4X / 4!) - ... + (NX / N!)

Controlando la suma con la condición de que se seguirá sumando siempre y cuando
la el valor absoluto de la diferencia entre el término anterior y el término a 
sumar sea mayor al epsilon especificado.
"""

from math import fabs

# Inicializar variables
x = epsilon = termino = sumatorio = tAnt = diferencia = 0.0
i = 1
signo = -1
factorial = 2

# Proceso
x = float(input("Valor de X: "))
epsilon = float(input("Valor de Epsilon: "))

tAnt = 0
termino = (2 * x) / 2
diferencia = fabs(tAnt - termino)

while diferencia > epsilon:
    print("termino ", i, "= ", termino)
    sumatorio += termino
    tAnt = termino

    # Cálculo de nuevo término y su diferencia con el anterior
    i += 1
    factorial *= (i+1)
    termino = (signo ** (i+1)) * (i+1) * (x ** i) / factorial
    diferencia = fabs(tAnt - termino)

# Salida
print("\n——— Salida ———")
print("Sumatorio = ", sumatorio)

