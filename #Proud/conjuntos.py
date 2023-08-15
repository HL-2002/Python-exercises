""" 
Programa que permita generar un conjunto universal junto n cantidad de conjuntos (mínimo 4),
con los que se puedan realizar Unión ∪, Intersección ∩, Diferencia - y Complemento de conjuntos '.
"""

import random, re

def main():
    # Var Ini
    operacion = ""
    # n de conjuntos
    n = get_int("Número de conjuntos a definir (4 a 27):", 
                "Error: Número de conjuntos imposible", 
                4, 27)

    # cantidad de elementos de U
    c = get_int("C de elementos en el conjunto universal: ", 
                "Error: Cantidad de elementos no posible.",
                0)

    # Inicializar conjunto Universal
    U = ini_univ(c)
    print(f"\nConjunto Universal: {U}")

    # Inicializar subconjuntos con su letra
    conj = ini_conj(n, c, U)
    for X in conj:
        if len(conj[X]) > 0:
            print(f"Conjunto {X}: {conj[X]}")
        else:
            print(f"Conjunto {X}: ""{""}")

    # Introducir operación o terminar programa
    while True:
        print("\nOperadores disponibles:"
              "\n∪ ~ Unión" +
              "\n∩ ~ Intersección" +
              "\n- ~ Diferencia" +
              "\n' ~ Complemento\n")
        operacion = input("Su operación:")

        # Validación de operación
        if x:= valid(operacion, n):
            operacion = txt_op(operacion, n, U)
            R = eval(operacion)
            print(f"Conjunto resultante: {R}")
        else:
            print("Error: Operación imposible")

        opcion = get_int("Terminar 1 - Continuar 0: ",
                            "Error: Número no posible de conjuntos.",
                            0,1)
        if opcion:
            break
        

# Obtención y validación de inputs
def get_int(texto: str, error_msg: str, min: int, max: int = None) -> int:
    while True:
        try:
            var = int(input(texto))
        except ValueError:
            print("Error: Introduzca un número.")
        else:
            # Ver si hay límite superior
            if max == None:
                if var >= min:
                    break
            else:
                if min <= var <= max:
                    break
            print(error_msg)

    return var


# Inicializar conjunto universal
def ini_univ(c: int) -> set:
    return {random.randrange(-100,100) for x in range(0, c)}


# Inicializar subconjunto de U
def ini_conj(n: int, c: int, U:set) -> dict:
    conj = {}
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for i in range(n):
        l = abc[i]
        conj[l] = {random.choice(list(U)) for x in range(random.randrange(0,c))}
    return conj


# Validar texto de operación
def valid(operacion: str, n: int) -> bool:
    # Remover espacios en blanco
    operacion = operacion.strip()
    # Definir letras definidas como conjuntos
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    L = abc[n-1]
    # Devolver la evaluación de la expresión regular
    format = rf"^(\(*(?<![A-{L}])[A-{L}](?![A-{L}])(?<!')'?(?!')(?:\)?'?)+[∪∩\-]?)+$"
    return re.match(format, operacion)


# Complemento de conjunto
def compl(X: set, U: set) -> set:
    return U - X

# Texto a operación de conjuntos
def txt_op(operacion: str, n: int, U: set) -> str:
    # Reemplazar operadores
    operacion = operacion.replace("∪", "|")
    operacion = operacion.replace("∩", "&")

    # Reemplazar complemento
    for _ in range(operacion.count("'")):
        i = operacion.find("'")
        # X'
        if operacion[i-1] != ")":
            X = operacion[i-1]
            operacion = operacion.replace(f"{X}'", f"compl({X}, {U})")

        # (X)'
        if operacion[i-1] == ")":
            # Buscar paréntesis más próximo a al ' encontrado
            k = i
            while True:
                # Reemplazar si hay "(" y no hay "compl" que lo anteceda
                if operacion[k] == "(" and operacion[k-1] != "l":
                    subs1 = operacion[0:k]
                    subs2 = operacion[k+1:]
                    operacion = subs1 + "compl(" + subs2
                    operacion = operacion.replace(f")'", f",{U})",1)
                    break
                k-=1

    # Reemplazar Letras de conjuntos por diccionario a evaluar
    abc = "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
    for i in range(n-1):
        operacion = operacion.replace(f"{abc[i]}", f"conj['{abc[i]}']")

    return operacion


if __name__ == "__main__":
    main()