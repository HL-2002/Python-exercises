"""
Serie factorización, cuyo resultados serán expresados con 2 decimales.
"""

# Inicializar variables
a = b = n = n_factor = 0
term = s = 0.0

# Proceso
n = int(input("Cantidad entera de términos a sumar: "))
a = int(input("Valor entero de A: "))
b = int(input("Valor entero de B: "))

for i in range(0, n):
    if i == 0:
        n_factor = 1
        den = 1
    elif i == 1:
        n_factor = n
    else:
        n_factor *= (n - i + 1)
        den *= i
    
    num = n_factor * a ** (n-i) * b ** i
    
    term = num / den
    s += term

    print("Termino {0:1d}: {1:15.2f}".format(i, term))

print("Sumatorio: {0:15.2f}".format(s))    