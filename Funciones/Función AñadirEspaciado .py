""" Función AñadirEspaciado """

# Inicializar variables
texto = ""

# Definir Función
def AñadirEspaciado(texto:str) -> None:
    n_texto = ""
    for letra in texto:
        n_texto += letra + " "
    print(n_texto)

    return None

# Proceso
texto = input("Introduzca el texto a espaciar: ")
AñadirEspaciado(texto)