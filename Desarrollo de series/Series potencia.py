"""
Crear un programa Python que tenga como entrada X e Y como real y N como entero, 
el cual acumulara en S los N primeros términos de la serie.
"""

# Inicializar variables
x = y = s = termino = numerador = denominador = 0.0
n = contn = 0
contd = 1

# Proceso

# Entrada de datos
x = float(input("Valor de X: "))
y = float(input("Valor de Y: "))
n = int(input("Número de términos en la serie: "))
print("\nTérminos de la Serie:")

for i in range(1, n+1):
    # Cálculo de términos impares
    if (i % 2 != 0):
        termino = (n - contn) / ((x ** i) * (y ** (n - contd)))

    # Cálculo de términos pares
    else:
        if (n - contd) != 0:
            termino = - ((x ** i) * (y ** (n - contn))) / (n - contd)
        else:
            termino = 0
    
    # Paso para siguiente término
    contn += 2
    contd += 2

    # Sumatorio e impresión de términos
    s += termino
    print("Termino ", i,": ", termino)

# Salida
print("\n——— Salida ———")
print("Sumatoria = ", s)
print("Fin del programa\n")