""" 
Queremos guardar los nombres y la edades de los alumnos de un curso. 
Realiza un programa que introduzca el nombre y la edad de cada alumno. 
El proceso de lectura de datos terminará cuando se introduzca como nombre un 
asterisco "*".
Al finalizar se mostrará los siguientes datos:
    • Todos lo alumnos mayores de edad (adultos)
    • Los alumnos mayores (los que tienen más edad).
"""

# Inicializar variables
alumnos = {}
adultos = []
mayores = []
mayor = 0
i = 0

# Añadir alumnos al diccionario
while True:
    nombre = input("Nombre del alumno: ")
    if nombre != "*":
        edad = int(input(f"Edad de {nombre}: "))
        print()
        alumnos[nombre] = edad
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

# Imprimir alumnos adultos
print("Alumnos adultos: ", end="") 
# Imprimir nombres con coma al final hasta llegar al último nombre   
for i in range(len(adultos)):
    if i < len(adultos) - 1:
        print(adultos[i], end=", ")
    else:
        print(adultos[i])

# Imprimir alumnos mayores
print("Alumnos mayores: ", end="") 
# Imprimir nombres con coma al final hasta llegar al último nombre   
for i in range(len(mayores)):
    if i < len(mayores) - 1:
        print(mayores[i], end=", ")
    else:
        print(mayores[i])