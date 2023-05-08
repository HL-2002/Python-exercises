""" Parcial II - Programación II """

# Identificación
print("""Nombre y apellido: Henry Lang
Cédula: 30.020.022
Sección: 20311""",end="\n\n")

# Definir función principal para acceder a los diferentes programas
def main():
    # Inicializar variables
    opcion = 0

    print("""A continuación tiene una lista de los programas:
    1 - Nombres y edades de alumnos
    2 - Notas de un alumno
    3 - Los ejemplos de listas \n""")
    
    # Lectura de opción con verificación
    while True:
        opcion = int(input("Opción: "))
        print()

        if opcion == 1:
            # Ejecución de 1er programa
            nombres_edades()
            break
        elif opcion == 2:
            # Ejecución de 2do programa
            notas_alumno()
            break
        elif opcion == 3:
            ejemplos()
            break
        else:
            print("Opción no válida, inténtelo de nuevo...\n")

# 1er programa
def nombres_edades() -> None:
    # Bienvenida al programa
    print("––– Nombres y edades de alumnos –––\n")

    # Inicializar variables
    alumnos = {} # Diccionario de alumnos que identificará el nombre y lo asociará con la edad
    adultos = [] # Lista con todos los alumnos adultos
    mayores = [] # Lista con todos los alumnos con la mayor edad
    mayor = 0 # Mayor edad entre los alumnos
    i = 0 # Variable contadora

    # Añadir alumnos al diccionario
    while True:
        nombre = input("Nombre del alumno: ")
        if nombre != "*":
            edad = int(input(f"Edad de {nombre}: "))
            print()
            alumnos[nombre] = edad
        else:
            if len(alumnos) == 0:
                print("Por favor ingrese a un alumno...\n")
            else:
                break

    # Ver cuál es la mayor edad entre los alumnos
    for edad in alumnos.values():
        if i == 0:
            mayor = edad
            i += 1
        else:
            if edad > mayor:
                mayor = edad  

    # Conocer alumnos mayores de edad y aquellos con la mayor edad
    for nombre, edad in alumnos.items():
        if edad >= 18:
            adultos.append(nombre)
        if edad == mayor:
            mayores.append(nombre)

    # Impresión de resultados
    print()
    # Alumnos adultos
    if len(adultos) > 0:
        print("Alumnos adultos: ", end="") 
        imprimir_nombres(adultos)
    else:
        print("No hay adultos mayores de edad.")

    # Alumnos mayores
    print("Alumnos mayores: ", end="")   
    imprimir_nombres(mayores)
    
    return None

def notas_alumno() -> None:
    # Bienvenida al programa
    print("––– Notas de un alumno –––\n")

    # Inicializar variables
    notas = [] # Lista de todas las notas del alumno
    i = 0 # Variable contadora
    suma = media = mayor = menor = 0 # Datos a conocer

    # Entrada de i datos con verificación
    while True:
        # Ciclo hasta llegar a 5 notas
        if i <= 4:
            nota = int(input(f"Nota {i+1}: "))
            # Verificación de nota en intervalo deseado
            if 0 <= nota <= 10:
                notas.append(nota)
                i += 1
            else:
                print("Dato no válido, la nota debe estar entre 0 y 10\n")
        else:
            break

    # Cálculo de media y nota más alta
    for j in range(len(notas)):
        suma += notas[j]

        # Guardar 1ra nota como la mayor y menor nota hasta ahora
        if j == 0:
            mayor = notas[j]
            menor = notas[j]
        # Comparar nueva nota con la mayor y menor nota hasta el momento
        else:
            if notas[j] > mayor:
                mayor = notas[j]
            elif notas[j] < menor:
                menor = notas[j]

    media = suma / len(notas)

    # Imprimir datos
    print(f"\nNotas: {notas[0]} | {notas[1]} | {notas[2]} | {notas[3]} | {notas[4]}")
    print(f"Media: {media}")
    print(f"Mayor nota: {mayor}")
    print(f"Menor nota: {menor}")

    return None

# 3er programa
def ejemplos() -> None:
    # Bienvenida al programa 
    print("––– Los ejemplos de listas –––\n")

    print("Queremos hacer una lista de los estudiantes de Gryffindor")
    print("Para ello, inicializamos una lista con los más conocidos...\n")

    # Inicializar lista inicial de gryffindor
    gryffindor = ["Harry", "Hermione", "Ron"]

    print("Estudiantes de Gryffindor: ")
    imprimir_nombres(gryffindor)

    print("\nAunque nos faltan muchos más...")
    print("Afortunadamente la profesora McGonagall nos dio una lista de estudiantes\nque añadir con el método \".extend()\"...\n")
    
    # Inicializar lista de más estudiantes
    estudiantes = ["Neville", "Fred", "George", "Ginny", "Draco"]
    print("Lista de McGonagall: ")
    imprimir_nombres(estudiantes)

    # Añadir a la lista de estudiantes de Gryffindor con el método .extend(),
    # el cual nos permite acoplar los elementos de un iterable a la lista.
    gryffindor.extend(estudiantes)

    print("\nNueva lista de Gryffindor: ")
    imprimir_nombres(gryffindor)

    print("\nEspera... Draco no es miembro de Gryffindor!")
    print("Pero no hay problema, podemos sacarlo de la lista con el método \".remove()\"...\n")

    # Remover a Draco de la lista con el método ".remove()", el cual
    # elimina el primer elemento de la lista con el valor especificado.
    gryffindor.remove("Draco")
    imprimir_nombres(gryffindor)

# Función para imprimir nombres de las listas de varios programas
def imprimir_nombres(lista) -> None:
    for i in range(len(lista)):
        if i < len(lista) - 1:
            print(lista[i], end=", ")
        else:
            print(lista[i])
    return None

# Ejecución de la función principal
main()