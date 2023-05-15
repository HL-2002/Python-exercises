""" Fuel Gauge """

def main():
    # Initialize variables
    numbers = []
    numerator = denominator = 0
    fraction = 0.0

    # Asking user for input
    while True:
        numbers = input("Fraction: ").split("/")
        
        # Handling errors should one arise
        try:
            numerator = int(numbers[0])
            denominator = int(numbers[1])
            fraction = numerator / denominator
        except ValueError:
            print("Fraction must be made of integers, try again...\n")
        except IndexError:
            print("Number must be a fraction, try again...\n")
            if int(numbers[0]) == 1:
                print("To calculate \"1\", type \"1/1\"\n") 
        except ZeroDivisionError:
            print("Division by zero!, try again...\n")
        
        # Getting desired input (fraction values ranging from 0 to 1)
        if numerator < 0 or denominator < 0:
                print("Fraction numbers can't be negative, try again...\n")
        elif fraction > 1:
            print("Fraction can't be greater than 1, try again...\n")
        else:
            break

    # Printing fuel gauge
    print(fuel_calc(convert(fraction)))


def convert(fraction: float) -> int:
    return round(fraction * 100)


def fuel_calc(percentage: int) -> str:
    fuel_gauge = ""

    # Printing fuel percetange
    if percentage <= 1:
        fuel_gauge = "E"
    elif percentage >= 99:
        fuel_gauge = "F"
    else:
        fuel_gauge = f"{percentage}%"

    return fuel_gauge


if __name__ == "__main__":
    main()