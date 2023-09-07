""" Program that expects exactly one CLA, the path of a .py file, that outputs
the lines of code it has. Comments and lines with whitespaces don't count. """

# How to debug code that uses CLA? (pending)

import sys
# Variable initialization
lines = ini = end = 0

print(sys.argv)
# Validate arg
try:
    path = sys.argv[1]
except IndexError:
    sys.exit("Not enough CLA, insert file's path.")

# Validate .py file
if path.count(".py") != 1:
    sys.exit("Defined path is not a valid .py file.")
else:
    # Validate existence of .py file
    try:
        file = open(path)
    except FileNotFoundError:
        sys.exit("Defined path isn't an existent .py file")
    # Read lines of code
    for line in file:
        # Condition for blank lines and # comments
        if line != "\n" and not line.startswith("#"):
            lines += 1
            # Condition for lines of """ comments counting the """ lines and those in between
            if line.startswith("\"\"\"") and (ini == 0 or end == 0):
                if ini == 0:
                    ini = lines
                elif end == 0:
                    end = lines + 1
                    lines -= end - ini
                    ini = end = 0
            
    print(f"This file has {lines} lines of code.")
