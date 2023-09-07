""" 
Software que permita ingresar el conjunto universal conformado por los estudiantes de 
lógica simbólica y los subconjuntos de la actividad anterior, con los que se puedan realizar 
Unión ∪, Intersección ∩, Diferencia - y Complemento de conjuntos '.
"""


def main():
    # Var Ini
    operacion = ""

    # Inicializar conjunto Universal
    U = {"Henry", "Gustavo", "Luis", "Mario", "Gabriel", "Jesús", "Natassja", "Víctor"}
    print(f"\nConjunto Universal: {U}")

    # Inicializar subconjuntos
    conj = {# Caballero mayor de 17 de cabello castaño
            "1": {"Henry", "Luis", "Víctor", "Gustavo"},
            # Dama menor de 21
            "2": set(),
            # Dama con cabello castaño y ojos claros
            "3": set(),
            # Menor de 18
            "4": set(),
            # Les gusta el chocolate
            "5": {"Henry", "Mario", "Luis", "Víctor", "Gabriel", "Natassja", "Gustavo"},
            # Viven fuera de Carabobo
            "6": {"Gabriel"},
            # Juegan videojuegos
            "7": {"Henry", "Mario", "Luis", "Jesús", "Víctor", "Gabriel", "Gustavo"},
            # No les dio COVID
            "8": {"Henry", "Mario", "Luis", "Jesús", "Gabriel"},
            # Intersección de 1 y 2
            "9": set()
    }

    # Imprimir subconjuntos
    for X in conj:
        if len(conj[X]) > 0:
            print(f"Conjunto {X}: {conj[X]}")
        else:
            print(f"Conjunto {X}: " "{" "}")

    # Operaciones automáticas
    # Unión de cada conjunto
    n = 1
    print("\nUnión:")
    for i in range(1, 10):
        for j in range(n,10):
            operacion = txt_op(f"{i}∪{j}",U)
            R = eval(operacion)
            
            if len(R) > 0:
                print(f"{i}∪{j}: {R}")
            else:
                print(f"{i}∪{j}: " "{" "}")
        print()
        n += 1

    # Intersección de cada conjunto
    n = 1
    print("\nIntersección:")
    for i in range(1, 10):
        for j in range(n,10):
            operacion = txt_op(f"{i}∩{j}",U)
            R = eval(operacion)
            
            if len(R) > 0:
                print(f"{i}∩{j}: {R}")
            else:
                print(f"{i}∩{j}: " "{" "}")
        print()
        n += 1

    # Diferencia de cada conjunto
    n = 1
    print("\nDiferencia:")
    for i in range(1, 10):
        for j in range(n,10):
            operacion = txt_op(f"{i}-{j}",U)
            R = eval(operacion)
            
            if len(R) > 0:
                print(f"{i}-{j}: {R}")
            else:
                print(f"{i}-{j}: " "{" "}")
        print()
        n += 1

    # Complemento de cada conjunto
    print("\nComplemento:")
    for i in range(1, 10):
        operacion = txt_op(f"{i}'", U)
        R = eval(operacion)

        if len(R) > 0:
            print(f"{i}: {R}")
        else:
            print(f"{i}: " "{" "}")


# Complemento de subconjunto en su conjunto universal dado
def compl(X: set, U: set) -> set:
    return U - X


# Texto a operación de conjuntos
def txt_op(operacion: str, U: set) -> str:
    # Reemplazar operadores
    operacion = operacion.replace("∪", "|")
    operacion = operacion.replace("∩", "&")

    # Reemplazar complemento
    for _ in range(operacion.count("'")):
        i = operacion.find("'")
        # X'
        if operacion[i - 1] != ")":
            X = operacion[i - 1]
            operacion = operacion.replace(f"{X}'", f"compl({X}, U)")

        # (X)'
        if operacion[i - 1] == ")":
            # Buscar paréntesis más próximo a al ' encontrado
            k = i
            while True:
                # Reemplazar si hay "(" y no hay "compl" que lo anteceda
                if operacion[k] == "(" and operacion[k - 1] != "l":
                    subs1 = operacion[0:k]
                    subs2 = operacion[k + 1 :]
                    operacion = subs1 + "compl(" + subs2
                    operacion = operacion.replace(f")'", f",{U})", 1)
                    break
                k -= 1

    # Reemplazar Letras de subconjuntos por diccionario a evaluar
    abc = "123456789"
    for i in range(9):
        operacion = operacion.replace(f"{abc[i]}", f"conj['{abc[i]}']")

    # Reemplazar instancias de U con conjunto universal
    operacion = operacion.replace("U", f"{U}")

    return operacion


if __name__ == "__main__":
    main()