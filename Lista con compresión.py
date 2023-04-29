""" 
Hacer un programa que inicialice un vector de números con valores aleatorios, 
y posterior ordene los elementos de menor a mayor.
"""
from random import getrandbits

# Inicializar variables
lista = ordenada = []

# Inicializar vector con número aleatorio entre 0 y 255
n = 10
lista = [getrandbits(8) for _ in range(n)]
print(f"Lista: {lista}")

# Ordenar vector
ordenada = lista.sort()
print(f"Lista ordenada: {lista}")

