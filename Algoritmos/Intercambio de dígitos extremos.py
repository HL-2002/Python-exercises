"""
Crear una aplicación en Python 3.6 que dado un entero K de tres o más dígitos 
intercambie los dígitos extremos del número, por ejemplo si el numero K 
es: 234987, el resultado de intercambiar los extremos seria: 987234, esto en 
el caso de que la cantidad de dígitos sea par en caso, en caso de dígitos 
impares, ejemplo. 67589, el intercambio generaría 89567, al momento de 
suministrar el valor de K, el programa debe validar que esta valor tenga 
tres o más dígitos, en caso de no cumplirse esta condición se debe emitir un 
mensaje de error. La salida bebe mostrar el numero k leído y su valor con los 
extremos invertidos.
"""

# Incializar variables (Número K, K invertido, )
k = k_lenght = dig = 0
ki = ""

# Proceso
k = input("Inserte número entero K (tres o más dígitos): ")
k_lenght = len(k)
k = int(k)

if k_lenght >= 3:
    for i in range(0, k_lenght):
        dig = k % 10
        k //= 10
        ki += str(dig)   
    print("K invertido: ", ki)
else:
    print("Error: Su número tiene menos de 3 dígitos...")