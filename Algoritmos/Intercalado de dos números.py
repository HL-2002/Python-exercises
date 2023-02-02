"""
Intercalar dígitos de dos números, del más significativo al menos significativo.
1. Se empieza con el número con más dígitos, por defecto A en caso de números con
igual cantidad de dígitos.
2. De agotarse los dígitos del número menor, se completa con los dígitos faltantes
del número mayor.
"""

# Inicializar variables
a = b = dig1 = div1 = dig2 = div2 = a_len = b_len = cont = 0
k = ""

# Proceso
a = input("Inserte número entero A: ")
b = input("Inserte número entero B: ")

# Cálculo de longitud, divisores y casting de A y B
a_len = len(a)
b_len = len(b)
div1 = 10 ** (a_len - 1)
div2 = 10 ** (b_len - 1)
a = int(a)
b = int(b)

while (a != 0) or (b != 0):
    # Obtención de dígitos
    if a != 0:
        dig1 = a // div1
        a %= div1
        div1 //= 10

    if b != 0:
        dig2 = b // div2
        b %= div2
        div2 //= 10

    # Composición de intercalado
    if b_len > a_len:
        if a_len > cont:
            k += str(dig2) + str(dig1)
            cont += 1
        else:
            k += str(dig2)
    if (a_len > b_len) or (a_len == b_len):
        if b_len > cont:
            k += str(dig1) + str(dig2)
            cont += 1
        else:
            k += str(dig1)

print(k)