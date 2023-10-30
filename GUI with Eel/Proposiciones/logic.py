import eel
import re

# Initialize eel object
eel.init("front")

# Variables
# Dict to store sets
props = dict()
# Initiated dict
auto_props = {
    1: "El cielo es azul",
    2: "La Tierra es redonda",
    3: "El agua es líquida",
    4: "El fuego es caliente",
    5: "El viento es fuerte",
    6: "El sol es brillante",
    7: "La luna es llena",
    8: "Las estrellas son brillantes",
    9: "Los planetas son redondos",
    10: "Los animales son vivos",
    11: "Las plantas son verdes",
    12: "Los humanos son inteligentes",
    13: "Los niños son felices",
    14: "Los adultos son responsables",
    15: "Los ancianos son sabios",
    16: "La vida es hermosa",
    17: "El número 7 es primo",
    18: "El cuadrado de 9 es 81",
    19: "El seno de 90 grados es 1",
    20: "El coseno de 90 grados es 0",
}


# Functions to expose
@eel.expose
def add_prop(input) -> int:
    """
    Receives input from front and stores it in props dict out of scope,
    to then return the number of the proposition within the dict
    """
    # Adds proposition to props out of scope
    global props
    # Counting from 1
    n = len(props) + 1
    props[n] = input.strip()

    # Returns index + 1 to count number of sets on js
    return n


@eel.expose
def auto_ini() -> dict:
    """ 
    Equals the props dict to the initialized one and returns it
    """
    global props, auto_props
    props = auto_props
    return props

@eel.expose
def reset() -> None:
    """
    Resets the props
    """
    global props
    props = dict()

@eel.expose
def valid(operacion) -> bool:
    """ 
    After getting the proposition numbers out of an operation, checks the validity 
    of a given operation, considering the proper use of logical operators syntax 
    and balanced parentheses.
    """
    # Var ini
    last = len(props)
    # Get prop_indexes involved in operation
    propositions = get_propositions(operacion)

    # Determine definition of given proposition index
    for x in propositions:
        if int(x) > last:
            return False

    # Set REGEX
    # ^(((?<!~)~?(?!~)\(*)*\d(?:\))*([v^→](?=[~\(]|\d(?![v^→])))?)+$
    regex = rf"""
                ^(                             # Must begin with pattern
                (                              # Group for repetiton of ~(
                (?<!~)~?(?!~)                  # Unique optional negation
                \(*                            # Optional (
                )*                             # End of optional group
                \d                             # Proposition number
                (?:\))*                        # Optional )
                ([v^→](?=[~\(]|\d(?![v^→])))?  # Optional operators only if followed by ~,( or a digit that's not followed by operators
                )+$                            # Must appear more than once and end with pattern
                """

    return re.match(regex, operacion, re.X) and parentheses_pair(operacion)


@eel.expose
def operacion_manual(operacion) -> str:
    return op_txt(operacion)


@eel.expose
def exists(prop_index) -> bool:
    return 0 <= int(prop_index) <= len(props)


@eel.expose
def conjunction(prop_index) -> str:
    u = ""
    for i in range(1,len(props)+1):
        if i != int(prop_index):
            u += op_txt(f"{prop_index}^{i}") + "<br>"

    return u


@eel.expose
def disjunction(prop_index) -> str:
    u = ""
    for i in range(1,len(props)+1):
        if i != int(prop_index):
            u += op_txt(f"{prop_index}v{i}") + "<br>"

    return u

@eel.expose
def conditional(prop_index) -> str:
    u = ""
    for i in range(1,len(props)+1):
        if i != prop_index:
            u += op_txt(f"{prop_index}→{i}") + "<br>"

    return u

@eel.expose
def negation(prop_index) -> str:
    return op_txt(f"~{prop_index}")


# Implementation functions
def get_propositions(operacion) -> list:
    """
    Gets every proposition index involved in the given operation
    """
    # Var init
    propositions = []
    prop_index = ""
    i = count = 0

    while(i < len(operacion)):
        # Get letter and begin operation if it's a number
        l = operacion[i]
        if re.match("[1-9]", l):
            # Append whole number
            try:
                while re.match("\d", operacion[i+count]):
                    prop_index += operacion[i+count]
                    count += 1
            except IndexError:
                pass
            if prop_index not in propositions:
                propositions.append(prop_index)
            # Jumping to index after last digit
            i += count
            # Reset variables
            count = 0
            prop_index = ""
        else:
            i+=1
    return propositions
    

def parentheses_pair(input) -> bool:
    """
    Counts the amount of opened and closed parentheses, returning the boolean evaluation
    of its equality
    """
    # Count open and closed parentheses
    open = input.count("(")
    closed = input.count(")")
    return open == closed


def op_txt(operacion) -> str:
    """
    Gets a valid logical operation and translates it to natural language, by
    iterating over operation str and adding natural language to result
    """
    # Var init
    token = []
    resultado = ""
    prop_index = ""
    i = count = 0

    # Tokenize operation
    while i < len(operacion):
        x = operacion[i]
        # Add operator to token
        if re.match("[~^v→\(\)]", x):
            token.append(x)
            i += 1
        # Add prop_index to token
        elif re.match("\d",x):
            # Append whole number
            try:
                while re.match("\d", operacion[i+count]):
                    prop_index += operacion[i+count]
                    count += 1
            except IndexError:
                pass
            token.append(prop_index)
            # Jumping to index after last digit
            i += count
            # Reset variables
            count = 0
            prop_index = ""

    # Replace every operator with natural language
    for i in range(len(token)):
        match token[i]:
            # Replace negation
            case "~":
                resultado += "no es cierto que "
            # Replace conjunction
            case "^":
                resultado += " y "
            # Replace disyunction
            case "v":
                resultado += " ó "
            # Replace closed parentheses
            case ")":
                if token[i-1] != ")" and i != len(token) - 1:
                    resultado += ";"
            # Do nothing with opened parenteses
            case "(":
                pass
            # Replace conditional
            case "→":
                if token[i-1] != ")":
                    resultado += ", por lo que "
                else:
                    resultado += " por lo que "
            # Replace prop_index with actual proposition
            case _:
                resultado += props[int(token[i])]

    # Return formatted result with operation and capitalization
    return f"{operacion} ⩳ " + resultado.capitalize()

# Run app
if __name__ == "__main__":
    eel.start("index.html")