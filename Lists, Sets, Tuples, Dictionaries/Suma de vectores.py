""" 
Programa que declare tres vectores 'vector1', 'vector2' y 'vector3' de cinco 
enteros cada uno, pida valores para 'vector1' y 'vector2' y calcule 
vector3 = vector1 + vector2.
"""

# Definir función principal del programa
def main():
    # Inicializar variables
    vector1 = []
    vector2 = []
    vector3 = []
    i = j = coordenada = 0

    # Definir ambos vectores según input
    print("Vector 1 , introduzca \"_\" para terminar")
    while True:
        coordenada = input(f"Coordenada x{i}: ")
        if coordenada != "_":
            vector1.append(int(coordenada))
            i += 1
        else:
            if len(vector1) < 1:
                print("No ha introducido ninguna coordenada... por favor ingrese alguna")
            else: 
                break
    print()
    
    print("Vector 2, introduzca \"_\" para terminar")
    while True:
        coordenada = input(f"Coordenada x{j}: ")
        if coordenada != "_":
            vector2.append(int(coordenada))
            j += 1
        else:
            break
    print()

    print(f"Vector 1: {vector1}")
    print(f"Vector 2: {vector2}")

    vector3 = suma_vectorial(vector1,vector2)
    print(f"Vector 3: {vector3}")

def suma_vectorial(vector1:list, vector2:list) -> list:
    """Suma de cada coordenada de los vectores, extendiendo el vector de menor 
    dimensión a la dimensión del otro vector para posibilitar la suma.
    (La suma de vectores de diferente dimensión no es posible).

    Args:
        vector1 (list)
        vector2 (list)

    Returns:
        list: vector resultante
    """
    vector3 = []

    if len(vector1) > len(vector2):
        while len(vector1) > len(vector2):
            vector2.append(0)
    elif len(vector2) > len(vector1):
        while len(vector2) > len(vector1):
            vector1.append(0)
    
    for i in range(len(vector1)):
        vector3.append(vector1[i] + vector2[i])

    return vector3

# Ejecutar programa
main()