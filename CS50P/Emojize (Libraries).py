"""
In a file called emojize.py, implement a program that prompts the user for a str in 
English and then outputs the “emojized” version of that str, converting any codes 
(or aliases) therein to their corresponding emoji.
"""

# Importing library
from emoji import emojize
""" Sex on the beach
"""

emoji = emojize(input("Input: "), language="alias")
print(f"Output: {emoji}")