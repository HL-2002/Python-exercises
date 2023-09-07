""" 
Implement a function that validates an IPv4 address, considering that each
numberic value ranges from 0 to 255.
"""

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    ip = ip.strip()
    # The pattern includes the range 0-255, addresing it from 0-199 | 200-249 | 250-255
    num_pattern = r"(?:1?\d?\d|2[0-4]\d|25[0-5])"
    ip_pattern = rf"{num_pattern}\.{num_pattern}\.{num_pattern}\.{num_pattern}"
    return bool(re.fullmatch(ip_pattern, ip))


if __name__ == "__main__":
    main()
