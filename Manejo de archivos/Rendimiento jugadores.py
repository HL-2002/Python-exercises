"""
Beisbol - Rendimiento de jugadores

El archivo Rendimiento.txt contiene los datos en orden:
Nombre, cantidad de ponches, sencillos bateados, dobles bateados, triples bateados, cuadrangulares bateados.

Para cada bateador:
- Calcular promedio de bateo y veces que se embasó.
Para todos los bateadores:
- Nombre del bateador con mayor promedio. De haber varios, reporte el nombre del primero y el último.
- Porcentaje de bateadores cuyo promedio fue mayor de 0.300, 2f.
- Porcentaje de sencillos bateados respecto al total de hits, 2f.
"""

""" Inicializar variables """
archivo = "Rendimiento.txt"
estadisticas = []
lista = []
nombre = ""
sencillos = dobles = triples = cuadrangulares = hits = embaso = 0
promedio = 0.0
nombre_mayor = [""]
promedio_mayor = 0
mayores = ultimo = 0
check = False
jugadores = superiores = 0
porcentaje_superiores = 0.0
total_hits = total_sencillos = 0
porcentaje_sencillos = 0.0


""" Proceso """
# Impresión para encabezado de tabla
print("Nombre    Ponches   Sencillos   Dobles   Triples   Home Run   Promedio   Se embaso")

# Procesamiento de archivo
estadisticas = open(archivo)
for row in estadisticas:
    lista = row.split(",")
    (nombre, ponches, sencillos, dobles, triples, cuadrangulares) = lista
    ponches = int(ponches)
    sencillos = int(sencillos)
    dobles = int(dobles)
    triples = int(triples)
    cuadrangulares = int(cuadrangulares)

    # Cálculo de promedio
    hits = sencillos + dobles + triples + cuadrangulares
    turnos = ponches + hits
    promedio = hits / turnos

    # Impresión de estadísticas
    print("{0:10}    {1:3d}         {2:3d}      {3:3d}       {4:3d}        {5:3d}      {6:4.3f}         {7:3d}".
    format(nombre, ponches, sencillos, dobles, triples, cuadrangulares, promedio, hits))

    # Conocer jugadores con mayor promedio
    if check == False:
        nombre_mayor[0] = nombre
        promedio_mayor = promedio
        mayores +=1
        check = True
    else:
        if promedio == promedio_mayor:
            nombre_mayor.append(nombre)
            mayores += 1
        elif promedio > promedio_mayor:
            nombre_mayor[0] = nombre
            promedio_mayor = promedio
            mayores = 1

    # Sumar numero de jugadores con promedio > 0.300
    jugadores += 1
    if promedio > 0.300:
        superiores +=1
    
    # Suma de hits y sencillos
    total_hits += hits
    total_sencillos += sencillos

# Obtener porcentaje de jugadores con promedio > 0.300
porcentaje_superiores = (superiores * 100) / jugadores

# Obtener porcentaje de sencillos respecto a hits
porcentaje_sencillos = (total_sencillos * 100) / total_hits

""" Salida final """
# Imprimir bateador o bateadores con mayor promedio
if mayores == 1:
    print("\nBateador con mayor promedio de bateo: ", nombre_mayor[0])
if mayores > 1:
    ultimo = len(nombre_mayor)
    print("\nPrimer y último bateador con mayores promedios: {0:8}, {1:8}".format(nombre_mayor[0], nombre_mayor[ultimo-1]))

# Imprimir porcentaje de bateadores con promedio > 0.300
print("Porcentaje de jugadores con promedio mayor a 0.300: {0:5.2f}".format(porcentaje_superiores))

#Imprimir porcentaje de sencillos
print("Porcentaje de sencillos respecto a hits: {0:5.2f}".format(porcentaje_sencillos))