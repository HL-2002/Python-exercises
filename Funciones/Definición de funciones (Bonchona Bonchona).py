# Definición de funciones
ciudad = nombre = cancion = ""

def bonchona_bonchona():
    print("Bonchona Bonchona")
    nombre = input("¿Quién llama?: ")
    ciudad = input("¿De dónde nos llama {0}?: ".format(nombre))
    cancion = input("¿Qué canción le ponemos {0}?: ".format(nombre))
    print("*Reproduciendo '{0}'*".format(cancion))
bonchona_bonchona()
