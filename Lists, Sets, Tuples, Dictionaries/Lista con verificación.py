""" 
Programa que declare un vector de diez elementos enteros y pida números para 
rellenarlo hasta que se llene el vector o se introduzca un número negativo. 
Entonces se debe imprimir el vector (sólo los elementos introducidos).
"""

# Inicializar variables
lista = []
i = 0

# Rellenar lista
while True:
    if i < 10: 
        n = int(input(f"Número {i+1}: "))
        if n >= 0:
            lista.append(n)
            i += 1
        else:
            break

# Imprimir lista
print(f"Lista de números: {lista}")