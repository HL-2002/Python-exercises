"""
Determinación de códigos de seguridad

Desarrolle un programa en e Python 3.6 que procese la información del archivo 
“Empleados.txt”, determine y muestre por consola, para cada empleado:

- Nombre, Edad, cedula, Código del empleado, de forma tabula y formateada.

* Empleados.txt contiene el Nombre, Edad y la C.I. de cada empleado.

El código se construye con 6 dígitos, empezando con la edad del empleado y los
primeros 4 dígitos pares de su C.I., partiendo desde el último dígito al primero.
* De faltar dígitos, se añaden ceros hasta llegar a los 6 dígitos.
"""

# Inicializar variables
archivo = ""
registro = []
nombre = edad = codigo = ""
cedula = num = dig = 0

# Proceso
print("Nombre      Edad     Cédula     Código del empleado")
archivo = open("Empleados.txt")

for row in archivo:
    registro = row.split(",")
    (nombre, edad, cedula) = registro
    cedula = int(cedula)
    
    # Composición de código
    codigo += edad

    # Obtención de 4 dígitos pares de la cédula
    num = cedula
    while num != 0:
        dig = num % 10
        num //= 10

        if (len(codigo) < 6) and (dig % 2 == 0):
            codigo += str(dig)
    
    # Añadir ceros si faltan dígitos
    if len(codigo) < 6:
        while len(codigo) <  6:
            codigo += "0"
    
    # Salida
    print("{0:9}   {1:^4}    {2:8d}    {3:^19}".format(nombre, edad, cedula, codigo))

    # Resetear variables para próximo código
    codigo = ""