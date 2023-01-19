"""
La serie de Ulam comienza con cualquier número entero positivo, el siguiente 
termino de la serie se calcula así: 

Si el termino es par se divide por 2 (división entera), en caso 
contrario se multiplica por 3 y se le suma 1, este proceso se repite hasta se 
obtenga 1.
Ejemplo: si el número inicial es 26 la serie seria:
26,13,40,20,10,5,16,8,4,2,1

Escriba un programa que lea un número entero positivo y desarrolle la serie de 
Ulam para dicho número al final se debe imprimir la suma de todos los términos 
obtenidos.
"""

# Inicializar variables
n = sumatorio = 0
serie = []

# Proceso
n = int(input("Valor (natural) de N: "))

# Calculo de serie
while (n != 1):
    print(n, end = " ")
    if (n % 2) == 0:
        n //= 2
    else:
        n = (n * 3) + 1
    sumatorio += n
# Añadir número en que termina el ciclo
print (n)
sumatorio += n

# Salida
print("\n——— Salida ———")
print("Sumatorio = ", sumatorio)