""" Función EsMultiplo
Crea una función que reciba dos números enteros y devuelva si el 1ro es múltiplo del 2do.
"""

# Inicializar variables
n1 = n2 = 0

# Definir función
def EsMultiplo(n1: int, n2: int) -> None:
    """Obtiene el residuo de la división de n2 / n1 para conocer si n1 es múltiplo de n2

    Args:
        n1 (int): Divisor
        n2 (int): Dividendo
    
    Vars:
        multiplo (str): String de resultado

    Returns:
        None: La función imprime el resultado, no retorna algún valor.
    """
    multiplo = ""
    if n2 % n1 == 0:
        multiplo = "{0} es múltiplo de {1}".format(n1, n2)
    else:
        multiplo = "{0} no es múltiplo de {1}".format(n1, n2)
    print(multiplo)
    return None

# Proceso
n1 = int(input("Introduzca el 1er número entero: "))
n2 = int(input("Introduzca el 2do número entero: "))
EsMultiplo(n1,n2)