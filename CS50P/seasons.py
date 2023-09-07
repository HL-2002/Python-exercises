"""
In a file called seasons.py, implement a program that prompts the user for 
their date of birth in YYYY-MM-DD format and then sings prints how old they 
are in minutes, rounded to the nearest integer, using English words instead 
of numerals, just like the song from Rent, without any and between words.

Since a user might not know the time at which they were born, assume, for 
simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. 
And assume that the current time is also midnight. In other words, even if 
the user runs the program at noon, assume that it’s actually midnight, on the 
same date. Use datetime.date.today to get today’s date, per 
docs.python.org/3/library/datetime.html#datetime.date.today.
"""

from datetime import date
import inflect


def main():
    # Initialize variables
    bd = eng = ""
    year = month = day = diff = min = count = 0

    # Initialize inflect engine
    inf = inflect.engine()

    # Get user's birthday, clean it from whitespaces and split it into a list.
    bd = input("Insert date (YYYY-MM-DD):").strip().split("-")
    year = int(bd[0])
    month = int(bd[1])
    day = int(bd[2])

    # Store user's date
    birthday = date(year, month, day)

    # Get days since birthday
    diff = date.today() - birthday

    # Transform days into minutes
    min = diff.days * 24 * 60

    # Get minutes into English, and substitute "and" with ", "
    eng = inf.number_to_words(min)
    print(eng)


if __name__ == "__main__":
    main()