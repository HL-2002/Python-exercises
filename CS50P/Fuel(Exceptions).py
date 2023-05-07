""" Fuel Gauge """

# Initialize variables
numbers = []
numerator = denominator = 0
fraction = 0.0
fuel = 0.0

# Asking user for input, handling errors should one arise
while True:
    numbers = input("Fraction: ").split("/")
    try:
        numerator = int(numbers[0])
        denominator = int(numbers[1])
        fraction = numerator / denominator
    except ValueError:
        print("Fraction must be made of integers, try again...\n")
    except ZeroDivisionError:
        print("Division by zero!, try again...\n")
    except IndexError:
        print("Number must be a fraction, try again...\n")
        if int(numbers[0]) == 1:
            print("To calculate \"1\", type \"1/1\"\n")
    else:
        break

# Calculating fuel percentage
fuel = fraction * 100

# Printing fuel percetange
if fuel <= 1:
    print("E")
elif fuel >= 99:
    print("F")
else:    
    print(f"{fuel:3.0f}%")
