" Gauss Jordan "
from fractions import Fraction
from random import randrange

def main():
    # Defining Linear System of Equations
    m = n = 3
    matrix = create_matrix(m,n)
    coefficients = create_coefficients(m)
    """ Manual definition
    matrix = [
        [a, b, c],
        [d, e, f],
        [g, h, i]
    ]

    coefficients = [x, y, z]
    """

    # Printing the matrix with coefficients
    matrix_print(matrix, coefficients)

    # Using Gauss Jordan to solve the linear system of equations
    gauss_jordan(matrix,coefficients)

def create_matrix(rows:int, columns:int) -> list:
    """Creates a matrix based on the amount of rows and columns desired.

    Args:
        rows (int)
        columns (int)

    Returns:
        list: Matrix created.
    """
    matrix = []
    
    for i in range(rows):
        matrix.append(list())
        for _ in range(columns):
            matrix[i].append(randrange(-10, 10))
    
    return matrix

def create_coefficients(length:int) -> list:
    """Creates a list of coefficients based on the amount of rows and columns desired.

    Args:
        length(int): List length.

    Returns:
        list: List of coefficients created.
    """
    matrix = []
    
    for i in range(length):
        matrix.append(randrange(-10,10))
    
    return matrix

def matrix_print(matrix:list, coefficients:list) -> None:
    """Prints the linear system of equations' extended matrix.

    Args:
        matrix (list).
        coefficients (list).
    """

    # Printing matrix with each coefficient
    for i in range(len(matrix)):
        print("|", end=" ")
        for j in range(len(matrix[i])):
            # This transforms any given expression to a fraction, then cast it into a str to apply the desired format
            print(f"{str(Fraction(matrix[i][j]).limit_denominator()):^5}".format(), end=" ")
        print(f" | {str(Fraction(coefficients[i]).limit_denominator()):^15} |")
    
    print()
    return None

def gauss_jordan(matrix:list, coefficients:list) -> None:
    # Declaring temporary variables in case of a substitution
    temp_row = []
    temp_coefficient = 0.0
    # Declaring scalar to pivot rows
    scalar = 0.0

    # Looping through each element of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Operating only with pivots
            if i == j:
                # Replacing row if its pivot is equal to 0
                if matrix[i][j] == 0:
                    # Store the whole row in temporary variables
                    temp_row = matrix[i]
                    temp_coefficient = coefficients[i]
                    # Looping through the matrix rows
                    for m in range(len(matrix)):
                        # If there's a pivot different to 0, replace rows.
                        if matrix[m][j] != 0:
                            matrix[i] = matrix[m]
                            coefficients[i] = coefficients[m]
                            matrix[m] = temp_row
                            coefficients[m] = temp_coefficient
                            break
                # Making pivot equal to 1 and dividing rest of the row by its scalar
                if matrix[i][j] != 1:
                    divisor = matrix[i][j]
                    for n in range(len(matrix)):
                        matrix[i][n] /= divisor
                    coefficients[i] /= divisor
            
                # Reduce rest of the column under and above current row
                for m in range(len(matrix)):
                    if m != i:
                        scalar = matrix[m][j]
                        for n in range(len(matrix[m])):
                            matrix[m][n] -= scalar * matrix[i][n]
                        coefficients[m] -= scalar * coefficients[i]
                    
    # Printing resulting extended matrix
    matrix_print(matrix,coefficients)

    return None

# Executing main function
main()