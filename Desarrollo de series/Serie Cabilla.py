""" 
Serie Cabilla

Crear un programa en python que tenga X y Y como entradas reales y N como entero,
que acumule el sumatorio los N términos de la serie:

{N / [X * Y^(N-1)]} - { [X^2 * Y^(N-2)] / (N-3)} + {(N-5) / [X^3 * Y^(N-5)]} + ...
"""

# Inicializar variables
x = y = termino = sumatorio = 0.0
n = añadido = j = 0
signo = -1


# Proceso
x = float(input("Valor de X: "))
y = float(input("Valor de Y: "))
n = int(input("Valor (entero) de N: "))

for i in range(1, n+1):
    # Residuo con divisor 2 para saber si es número par
    residuo = i % 2    

    if residuo != 0:
        termino = (n - añadido) / ((x**i) * (y**(n - (1+añadido))))
    else:
        # Si N - 3 - Añadido = 0, no se puede dividir, por lo que hacemos:
        if (n - 3 - añadido) != 0:
            termino = - ((x**i) * (y**(n-2 - añadido))) / (n - (3+añadido)) 
        else:
            termino = 0
        añadido += 4

    print("termino ", i, "= ", termino)
    sumatorio += termino

# Salida
print("\nSalida del programa")
print("Sumatorio = ", sumatorio)