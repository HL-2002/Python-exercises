"""
In a file called watch.py, implement a function called parse that expects a 
str of HTML as input, extracts any YouTube URL that’s the value of a src 
attribute of an iframe element therein, and returns its shorter, shareable 
youtu.be equivalent as a str.
"""

import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    link = re.search(r"src=\".+?/embed/(.+?)\"", s)
    return f"https://youtu.be/{link[1]}"


if __name__ == "__main__":
    main()