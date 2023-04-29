""" 
Se quiere realizar un programa que lea por teclado las 5 notas obtenidas por un
alumno (comprendidas entre 0 y 10).

A continuación debe mostrar todas las notas, la nota media, la nota más alta 
que ha sacado y la menor.
"""

# Inicializar variables
notas = []
i = 0
suma = media = mayor = menor = 0

# Entrada de i datos con verificación
while True:
    if i <= 4:
        nota = int(input(f"Nota {i+1}: "))
        if 0 <= nota <= 10:
            notas.append(nota)
            i += 1
        else:
            print("Dato no válido, la nota debe estar entre 0 y 10\n")
    else:
        break

# Cálculo de media y nota más alta
for i in range(len(notas)):
    suma += notas[i]

    # Guardar 1ra nota como la mayor y menor nota hasta ahora
    if i == 0:
        mayor = notas[i]
        menor = notas[i]
    # Comparar nueva nota con la mayor y menor nota hasta el momento
    else:
        if notas[i] > mayor:
            mayor = notas[i]
        elif notas[i] < menor:
            menor = notas[i]

media = suma / len(notas)

# Imprimir datos
print(f"\nNotas: {notas[0]} | {notas[1]} | {notas[2]} | {notas[3]} | {notas[4]}")
print(f"Media: {media}")
print(f"Mayor nota: {mayor}")
print(f"Menor nota: {menor}")