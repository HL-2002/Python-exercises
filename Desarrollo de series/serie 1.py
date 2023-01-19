""" 
Serie 1

Cree un programa que desarrolle una serie de la forma:

S = (2x / 2!) - (3x^2 / 3!) + (4x^3 / 4!) - ... + (nx^n-1 / n!)

Se espera que el usuario introduzca el valor de x y la cantidad de términos a sumar.
"""

# Inicializar variables
x = sumatorio = termino = 0.0
n = 0
signo = -1
coeficiente = factorial = 2

# Proceso
x = float(input("Valor de X: "))
n = int(input("Número (entero) de términos a sumar: "))

for i in range(n):
    # Formulación, suma e impresión de término
    termino = (signo ** coeficiente) * ((coeficiente) * (x ** (coeficiente - 1))) / factorial
    sumatorio += termino
    print("termino ", i+1,": ", termino)

    # Operaciones para próximo término
    coeficiente += 1
    factorial *= coeficiente 

# Salida
print("\nSalida de resultados")
print("Sumatorio = ", sumatorio)