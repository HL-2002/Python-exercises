import eel


# Initialize variables
# Universal set
U = {"Henry", "Gustavo", "Luis", "Mario", "Gabriel", "Jesús", "Natassja", "Víctor"}

# Subsets
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


# Interface functions
@eel.expose
def union(set) -> str:
    u = ""
    for i in range(1,10):
        if i!=int(set):
            R = eval(f"conj['{set}']|conj['{i}']")
        
            if len(R) > 0:
                u += f"<br>{set}∪{i}: {R}"
            else:
                u += f"<br>{set}∪{i}: " "{" "}"

    return u

@eel.expose
def intersection(set:int) -> str:
    inter = ""
    for i in range(1,10):
        if i!=int(set):
            R = eval(f"conj['{set}']&conj['{i}']")

            if len(R) > 0:
                inter += f"<br>{set}∩{i}: {R}"
            else:
                inter += f"<br>{set}∩{i}: " "{" "}"

    return inter

@eel.expose
def difference(set:int) -> str:
    diff = ""
    for i in range(1,10):
        if i!=int(set):
            R = eval(f"conj['{set}']-conj['{i}']")

            if len(R) > 0:
                diff += f"<br>{set}-{i}: {R}"
            else:
                diff += f"<br>{set}-{i}: " "{" "}"

    return diff

@eel.expose
def complement(set:int) -> str:
    compl = ""
    R = eval(f"{U}-conj['{set}']")

    if len(R) > 0:
        compl = f"<br>{set}': {R}"
    else:
        compl = f"<br>{set}': " "{" "}"

    return compl

eel.init("front")
eel.start("index.html")