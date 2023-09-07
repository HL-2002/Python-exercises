""" 
In a file called working.py, implement a function called convert that expects 
a str in either of the 12-hour formats below and returns the corresponding str 
in 24-hour format (i.e., 9:00 to 17:00). Expect that AM and PM will be 
capitalized (with no periods therein) and that there will be a space before each.

- 9:00 AM to 5:00 PM
- 9 AM to 5 PM

Raise a ValueError instead if the input to convert is not in either of those 
formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do 
not assume that someone’s hours will start ante meridiem and end post meridiem; 
someone might work late and even long hours (e.g., 5:00 PM to 9:00 AM).
"""

import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    hour1 = minute1 = hour2 = minute2 = 0
    match = re.match(r"(?P<hour1>\d{1,2}):?(?P<minute1>\d{1,2})? (?P<stage1>AM|PM) to (?P<hour2>\d{1,2}):?(?P<minute2>\d{1,2})? (?P<stage2>AM|PM)", s)

    # Transforming and assigning 1st hour and minutes
    if match["stage1"] == "PM" and match["hour1"] != 12:
        hour1 += int(match["hour1"]) + 12
    elif match["stage1"] == "AM" and match["hour1"] == 12:
        hour1 = 0
    else:
        hour1 = int(match["hour1"])

    if match["minute1"] == None:
        minute1 = 0
    else:
        minute1 = int(match["minute1"])

    # Transforming and assigning 2nd hour and minutes
    if match["stage2"] == "PM" and match["hour2"] != 12:
        hour2 += int(match["hour2"]) + 12
    elif match["stage2"] == "AM" and match["hour2"] == 12:
        hour2 = 0
    else:
        hour2 = int(match["hour2"])

    if match["minute2"] == None:
        minute2 = 0
    else:
        minute2 = int(match["minute2"])

    # Raising ValueError (Based on 24h format)
    if minute1 > 59 or minute2 > 59:
        raise ValueError("Minutes greater than 59.")
    elif hour1 > 23 or hour2 > 23:
        raise ValueError("Hours greater than 12.")

    # Formatting and returning time
    return "{0:02d}:{1:02d} to {2:02d}:{3:02d}".format(hour1, minute1, hour2, minute2)

if __name__ == "__main__":
    main()