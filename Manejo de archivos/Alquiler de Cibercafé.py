"""
Alquiler de Cibercafé:
El archivo Ciber.txt contiene los datos de cada alquiler con el orden:
Número de la máquina, nombre del usuario, hora de inicio, hora de finalización.

La tarifa de cobro es la siguiente:
Por cada hora cumplida Bs. 500, por cada fracción de 15 min Bs. 100.

Para cada alquiler:
- Mostrar la máquina alquilada, el nombre del usuario, tiempo de uso y monto.
Para todos los alquileres:
- Mostrar el monto total recaudado y las veces que se alquiló cada máquina.
- Mostrar la 1ra máquina cuyo alquiler fue menor o igual a 30 minutos.
"""

# Entrada
archivo = "Ciber.txt"
alquileres = ""
alquiler = []
maquina = usuario = ""
h_inicio = min_inicio = h_final = min_final = t_inicio = t_final = t_total = h_total = min_total = 0
fraccion_min = fraccion_extra = monto = monto_total = 0
uso_maquina = [0, 0, 0]
menor_alquiler = ["", 0]
check = False

# Proceso
# Impresión para inicio de tabla
print("Máquina   Usuario   Tiempo de alquiler   Monto de alquiler")

# Procesamiento de archivo
alquileres = open(archivo)
for row in alquileres:
    alquiler = row.split(",")
    (maquina, usuario, h_inicio, min_inicio, h_final, min_final) = alquiler

    # Cálculo de tiempo de alquiler
    h_inicio = int(h_inicio)
    min_inicio = int(min_inicio)
    h_final = int(h_final)
    min_final = int(min_final)

    # Considerando alquiler de un día para otro
    if h_inicio > h_final:
        h_final += 24

    t_inicio = (h_inicio * 60) + min_inicio
    t_final = (h_final * 60) + min_final
    t_total = t_final - t_inicio

    h_total = t_total // 60
    min_total = t_total % 60

    fraccion_min = min_total // 15
    fraccion_extra = min_total % 15
    if fraccion_extra > 0:
        fraccion_min += 1

    # Cálculo de monto a cobrar
    monto = (h_total * 500) + (fraccion_min * 100)

    # Adición a monto total
    monto_total += monto

    # Adición de uso de máquina
    if maquina == "1":
        uso_maquina[0] += 1
    elif maquina == "2":
        uso_maquina[1] += 1
    elif maquina == "3":
        uso_maquina[2] += 1
    
    # Conocer 1er alquiler menor o igual a 30 minutos
    if (t_total <= 30) and (check == False):
        menor_alquiler[0] = maquina
        menor_alquiler[1] = t_total
        check == True

    # Impresión de datos
    print("{0:1} {1:8} {2:2d}:{3:2d} {4:5d} ".format(maquina, usuario, h_total, min_total, monto))

# Salida Final
print("\nMonto total recaudado: Bs. ", monto_total)
print("Veces alquiladas las máquinas:")
print("Maquina 1: {0:2d} | Maquina 2: {1:2d} | Maquina 3: {2:2d}".format(uso_maquina[0], uso_maquina[1], uso_maquina[2]))
print("1ra Máquina con alquiler menor o igual a 30 min: {0:1} con {1:2d} minutos".format(menor_alquiler[0], menor_alquiler[1]))