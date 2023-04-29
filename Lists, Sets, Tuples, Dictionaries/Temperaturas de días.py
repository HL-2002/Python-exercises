""" 
Queremos guardar la temperatura mínima y máxima de 5 días. 
Realiza un programa que de la siguiente información:
    • La temperatura media de cada día.
    • Los días con menos temperatura media.
    • Se lee una temperatura por teclado y se muestran los días cuya 
    temperatura máxima coincide con ella. si no existe ningún día se muestra
    un mensaje de información.
"""

# Inicializar variables
dias = {}
dia = ""
temperaturas = []
menores = []
indicadas = []
minima = maxima = menor = 0.0
ini = False

# Insertar datos de días
for i in range(5):
    dia = input(f"Día {i+1}: ")
    minima = int(input("Temperatura mínima: "))
    maxima = int(input("Temperatura máxima: "))
    temperaturas = [minima, maxima]
    dias[dia] = temperaturas
    print()

# Insertar temperatura indicada
indicada = int(input("Inserte la temperatura indicada: "))
print()

# Calcular la temperatura media de cada día y cuál es la menor temperatura media
for dia, temperaturas in dias.items():
    media = (temperaturas[0] + temperaturas [1]) / 2
    print(f"Temperatura media del {dia}: {media}º")

    # Guardar temperatura media para posterior comparación con otros días
    temperaturas.append(media)

    # Guardar menor temperatura media
    if ini == False:
        # Guarda la 1ra temperatura media como la menor por los momentos
        menor = media
        ini = True
    else:
        # Guarda la temperatura de ser menor a la ya guardada
        if media < menor:
            menor = media
print()

# Días con menor temperatura media y temperatura indicada
for dia, temperaturas in dias.items():
    if temperaturas[2] == menor:
        menores.append(dia)
    if temperaturas[2] == indicada:
        indicadas.append(dia)

# Impresión de todos los días con menor temperatura media
print(f"Días con menor temperatura media ({menor}º): ", end="")
for i in range(len(menores)):
    if i < len(menores) - 1:
        print(menores[i], end=", ")
    else:
        print(menores[i])

# Impresión de todos los días con la tempertura media indicada
print(f"Días con temperatura indicada ({indicada}º): ", end="")
for i in range(len(indicadas)):
    if i < len(indicadas) - 1:
        print(indicadas[i], end=", ")
    else:
        print(indicadas[i])