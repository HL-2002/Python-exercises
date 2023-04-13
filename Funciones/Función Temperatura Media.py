""" 
Crear una función que calcule la temperatura media de un día a partir de la 
temperatura máxima y mínima. 

Crear un programa principal, que utilizando la función anterior, vaya pidiendo 
la temperatura máxima y mínima de cada día y vaya mostrando la media. El 
programa pedirá el número de días que se van a introducir.
"""

# Inicializar variables
dias = 0
min = max = temperatura = suma = promedio = 0.0

# Proceso
dias = int(input("Introduzca la cantidad de días: "))
# Definición de función lambda para temperatura media
media = lambda min, max: (min + max) / 2

for i in range(1, dias + 1):
    min = float(input("\nTemperatura Mínima de día {0}: ".format(i)))
    max = float(input("Temperatura Máxima de día {0}: ".format(i)))
    temperatura = media(min,max)
    print("Temperatura Media de día {0}: {1:5.2f}˚".format(i, temperatura))
    suma += temperatura

promedio = suma / dias
print("\nTemperatura media de todos los días: {0:5.2f}˚".format(promedio))