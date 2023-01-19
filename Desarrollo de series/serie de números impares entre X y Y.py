"""
Dados los valores de X e Y, donde X < Y, ambos enteros, elabore un programa 
que calcule la sumatoria de los números impares entre X e Y. El programa debe
verificar que X es menor que Y, de no cumplirse se debe emitir el mensaje 
correspondiente.
"""

# Inicializar valores
x = y = termino = sumatorio = rango = 0
j = 1

# Proceso
x = int(input("Valor (entero) de X: "))
y = int(input("valor (entero) de Y: "))

if x < y:
    # Ciclo para contar únicamente los números impares
    for i in range(x, y):
        if (i % 2 != 0):
            termino = i
            print("termino ", j, "= ", termino)
            sumatorio += termino
            j += 1

else:
    print("X > Y, por lo que no se puede ejecutar la suma")

# Salida
print("\n——— Salida ———")
print("Sumatorio = ", sumatorio)