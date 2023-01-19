"""
El matemático italiano Leonardo Fibonacci propuso la siguiente serie numérica, 
en la cual los dos primeros términos son 0 y 1, a partir de aquí cada nuevo 
termino se calcula como el penúltimo mas el último, desarrolle la serie para 
los primeros N términos, imprima cada termino y al final la sumatoria de los mismos.
"""

# Inicializar variables
n = ta = tb = termino = sumatorio = 0
tb = 1

# Proceso
n = int(input("Valor (entero) de N: "))

for i in range (0, n):
    if i <= 1:
        termino = ta
    else:
        termino = ta + tb
    print(termino)
    sumatorio += termino

    # Operación para siguiente término
    ta = tb
    tb = termino



    

        

# Salida
print("\n——— Salida ———")
print("Sumatorio = ", sumatorio)