""" Función Escribir Centrado simple"""

# Inicializar variables
texto = ""
long = 0
 
# Proceso
texto = input("Ingrese texto a centrar, coloque '=' al final si desea subrayarlo: \n")
long = len(texto)

if texto.endswith("="):
    texto = texto.strip("=")
    print(((" ") * ((80 - long) // 2)), "\x1B[4m" + texto + "\x1B[0m", (" ") * ((80 - long) // 2))
else:
    print(texto.center(80))