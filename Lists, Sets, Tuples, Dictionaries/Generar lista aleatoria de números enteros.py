""" 
Realizar un programa que defina un vector llamado "vector_numeros" de 10 
enteros, a continuación lo inicialice con valores aleatorios (del 1 al 10) y 
posteriormente muestre en pantalla cada elemento del vector junto con su 
cuadrado y su cubo.
"""
from random import randint

# Definición del programa
def main():
    # Inicializar variables
    vector_numeros = []
    long = 10

    # Inicializar vector de números aleatorios
    vector_numeros = vector_ini(long)
    cuadrados_cubos(vector_numeros)

def vector_ini(long:int) -> list:
    """ Función que inicializa una lista de números aleatorios del 1 al 10 con 
    la longitud especificada.

    Args:
        len (int): Longitud de la lista deseada

    Returns:
        list: Lista inicializada
    """
    lista = []

    for i in range(0,long):
        lista.append(randint(1,10))
    
    return lista

def cuadrados_cubos(lista:list) -> None:
    """ Función que imprime en una tabla los elementos de una lista junto a sus 
    cuadrados y cubos.

    Args:
        lista (list): Lista a leer e imprimir
    """
    cuadrado = cubo = 0
    print("Elemento | Valor | Cuadrado | Cubo")
    for i, value in enumerate(lista):
        cuadrado = value ** 2
        cubo = value ** 3
        print("{0:^7}    {1:>5}   {2:>8}   {3:>4}".format(i, value, cuadrado, cubo))



# Llamado de función principal para ejecución del programa
main()