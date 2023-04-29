""" 
Práctica de listas:
- Integrar 5 notas en una lista,
- Longitud de la lista,
- Contar si hay una nota repetida, la posición y cuántas veces se repite,
- Obtener el sumatorio y promedio de las notas.
"""

def main():
    notas = [12, 14, 20, 14, 10]
    print(f"Longitud de la lista: {len(notas)}\n")
    repetido(notas)
    suma_promedio(notas)

def repetido(lista) -> None:
    """ 
    Posible alternativa a probar

    from collections import default_dict

    def list_duplicates(list):
        # Crea un diccionario cuyos valores serán una lista por defecto
        dic = default_dict(list)
        # Enumera la lista, tal que i es el índice de la lista y value el valor de dicho índice
        for i, value in enumerate(list):
            # Añade al diccionario el índice con el valor como clave
            dic[value].append(i)
        # Retorna el valor y los indices de los elementos de la lista basado en el diccionario creado, solo si dicho valor está presente en más de 1 índice
        return ((value, index) for value, index in dic.items() if len(index) > 1)

    # Organiza las claves del diccionario creado e imprime cada entrada del mismo
    for dup in sorted(list_duplicates(notas)):
        print(dup)
    """

    repeticion = 0
    repetido = []
    indices = []

    # Evaluar cada valor de la lista
    for i in range(len(lista)) :
        # Conocer veces que se repite el valor
        repeticion = lista.count(lista[i])
        
        if repeticion > 1:
            # Guardar valor en lista de valores repetidos y continuar sólo si ese valor no está presente
            repetido.append(lista[i])
            # Conocer los índices en que se repite dicho valor
            if repetido.count(lista[i]) == 1:
                for j in range(i, len(lista)):
                    if lista[i] == lista[j]:
                        indices.append(j)
                
                # Imprimir datos de valor repetido
                print(f"Índices de número repetido {lista[i]}: {indices}")
                print(f"Repetición de {lista[i]}: {repeticion}\n")

        # Reiniciar variables para próximo valor
        indices = []
        repeticion = 0

    return None

def suma_promedio(lista) -> None:
    # Función que suma cada nota y luego promedia dicho valor por cantidad de elementos
    suma = 0
    promedio = 0

    for elemento in lista:
        suma += elemento

    promedio = suma / len(lista)

    print(f"Sumatorio de notas: {suma}")
    print(f"Promedio de notas: {promedio:.1f}")

    return None

main()