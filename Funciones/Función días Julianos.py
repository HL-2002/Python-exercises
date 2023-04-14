""" Función de días Julianos """

# Identificación
print("""Nombre y apellido: Henry Lang
Cédula: 30.020.022
Sección: 20311
""",end="\n\n")

# Inicializar variables
fecha = 0

# Definir funciones
def LeerFecha() -> list:
    """Lee, verifica y almacena una fecha en una lista con sus datos como enteros

    Vars:
        fecha (string/list): Almacena la fecha en string y luego en lista.
        posible (bool): Determina si la fecha es posible o no, para repetir la lectura de ser imposible.
    
    Returns:
        list: Lista con datos de la fecha
    """
    fecha = ""
    posible = False

    while posible == False:
        # Lectura  y almacenamiento en lista de fecha
        fecha = input("Introduzca la fecha (dd/mm/aaaa): ")
        fecha = fecha.split("/")
        for i in range(3):
            fecha[i] = int(fecha[i])

        # Separación de datos y verificación
        dia = fecha[0]
        mes = fecha [1]
        if dia > 31 or mes > 12:
            print(posible)
            print("Usted ha introducido una fecha imposible.")
        else:
            posible = True
    

    return fecha

def EsBisiesto(año: int) -> bool:
    """Recibe un año y determina si es un año bisiesto, partiendo del primer
    año bisiesto (el año 0), hasta el año 10.000

    Args:
        año (int): Año de la fecha introducida
        
    Vars:
        frecuencia (int): Cada cuantos años hay un biciesto
        bisiesto (bool): Almacena si el año es bisiesto o no

    Returns:
        bool: Devuelve si es bisiesto o no
    """
    frecuencia = 4
    bisiesto = False
    
    for n in range(1, 2501):
        if año == n * frecuencia:
            bisiesto = True
    return bisiesto

def DiasDelMes(mes: int, bisiesto: bool) -> int:
    """Recibe un mes y si el año es bisiesto, para determinar la cantidad de días
    de dicho mes.

    Args:
        mes (int): Mes de la fecha
        bisiesto (bool): Si año es bisiesto o no

    Returns:
        int: Días del año
    """
    dias = 0
    
    if mes == 2:
        if bisiesto == False:
            dias = 28
        else:
            dias = 29
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        dias = 31
    else:
        dias = 30
    return dias

def Calcular_Dia_Juliano(fecha:list) -> None:
    """Recibe una fecha para sumar la cantidad de días que hay hasta llegar al mes
    especificado, para luego sumar el día de la fecha. Al final imprime el día juliano.

    Args:
        fecha (list): Recibe 

    Vars:
        dia, mes, año (int): Almacenan los datos de la fecha recibida por separado
        bisiesto (bool) : Almacena si el año es bisiesto o no para la función DiasDelMes
        juliano (int) : Almacena la cantidad de día para decir el día juliano

    Returns:
        None: La función imprime el día juliano en vez de devolver algún valor
    """
    (dia, mes, año) = fecha
    bisiesto = EsBisiesto(año)
    juliano = 0

    for i in range (1, mes):
        juliano += DiasDelMes(i, bisiesto)
    
    juliano += dia

    print("Día Juliano: ", juliano)

# Proceso
Calcular_Dia_Juliano(LeerFecha())