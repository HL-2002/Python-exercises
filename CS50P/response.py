""" 
In a file called response.py, using either validator-collection or validators 
from PyPI, implement a program that prompts the user for an email address via 
input and then prints Valid or Invalid, respectively, if the input is a 
syntatically valid email address. You may not use re. And do not validate 
whether the email address’s domain name actually exists.
"""

from python_email_validation import AbstractEmailValidation

def main():
    email = input("What's your email address? ")
    if api_validation(email):
        print("Valid")
    else:
        print("Invalid")

def api_validation(email):
    api_key = "601148a9982d44288413deea69a9dc2b"
    AbstractEmailValidation.configure(api_key)
    return AbstractEmailValidation.verify(email).is_valid_format

if __name__ == "__main__":
    main()