"""
Realizar una función usando una función con Callback, usando tipado estático.
"""

# Definición de variables
a: int = 0
b = c = opcion = a

# Definición de funciones
def suma(a: int, b: int) -> int:
    """ Función que suma dos enteros, retornando el resultado """
    return a + b

def producto(a:int, b:int) -> int:
    """ Función que multiplica enteros a través de la suma """
    c = 0
    for times in range(b//2):
        c += suma(a,a)
    # Como suma de dos en dos, se suma una última vez A a C para completar el producto.
    if b%2 != 0:
        c = suma(c,a)
    return c

# Proceso
print("Bienvenido a la calculadora de sumas, indique qué operación desea realizar...")
opcion = int(input("Suma - 0 | Producto - 1 : "))
a = int(input("\nValor A: "))
b = int(input("Valor B: "))

if opcion == 0:
    c = suma(a,b)
elif opcion == 1:
    c = producto(a,b)

print("Resultado: ", c)
