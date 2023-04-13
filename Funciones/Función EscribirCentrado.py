""" 
Función Centrado de cualquier texto
"""
# Inicializar variables
texto = ""

# Definir función
def EscribirCentrado (texto:str) -> None:
    """ Busca Centrar un texto de cualquier tamaño, separándolo por palabra para formular un
    nuevo texto con las mismas según la longitud del texto centrado que se quiera.

    Args:
        texto (string): Texto a centrar.
    
    Vars:
        palabras (list): Almacena las palabras.
        filas (list): Almacena las filas del nuevo texto.
        n_texto (string): Concatena el nuevo texto para formular filas con longitud deseada.
        long (int): Lleva cuenta de la longitud del nuevo texto, luego la longitud de la fila creada.
        subrayado (bool): Determina si el usuario quiere subrayado del texto o no.

    Returns:
        None: La función imprime el texto centrado en vez de retornar algún valor.
    """

    palabras = []
    filas = []
    n_texto = ""
    long = 0
    subrayado = False

    if texto.endswith("="):
        texto = texto.strip("=")
        subrayado = True

    palabras = texto.split()

    for x in palabras:
        long += len(x) + 1
        n_texto += x + " "

        if long >= 60 and long <= 79:
            filas.append(n_texto)
            long = 0
            n_texto = ""

    for fila in filas:
        if subrayado:
            long = len(fila)
            print(((" ") * ((80 - long) // 2)), "\x1B[4m" + fila + "\x1B[0m", (" ") * ((80 - long) // 2)) 
            # Requiere este formato en vez del método str.center() para subrayar únicamente el texto de la fila.
        else:
            print(fila.center(80))

    return None

# Proceso
texto = input("Ingrese texto a centrar, coloque '=' al final si desea subrayarlo: \n")
EscribirCentrado(texto)