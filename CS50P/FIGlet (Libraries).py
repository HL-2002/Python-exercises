""" 
In a file called figlet.py, implement a program that:

* Expects zero or two command-line arguments:
    - Zero if the user would like to output text in a random font.
    - Two if the user would like to output text in a specific font, in which case the 
    first of the two should be -f or --font, and the second of the two should be the name of the font.
* Prompts the user for a str of text.
* Outputs that text in the desired font.
"""

import sys
import random
from pyfiglet import Figlet, FigletFont

# Variable initialization
f = text = ""

# CLA handling
if len(sys.argv) == 1:
    # Random font
    # Figlet function is the font formatter, getFonts returns a list of fonts.
    f = Figlet(font=random.choice(FigletFont.getFonts()))
    print
elif len(sys.argv) == 3:
    # Specified font
    if sys.argv[1] == "-f" or sys.argv[1] == "--font":
        f = Figlet(font=sys.argv[2])
    else:
        sys.exit
elif len(sys.argv) == 2:
    print("Font specification left.")
    sys.exit
else:
    print("Too many arguments.")
    sys.exit

# Input and Output
text = input("Text: ")
print(Figlet.renderText(f, text))
