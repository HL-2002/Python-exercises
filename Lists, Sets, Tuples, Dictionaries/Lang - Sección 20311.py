""" Parcial III - Programación II """
from random import randrange

# Identification
print("""Nombre y apellido: Henry Lang
Cédula: 30.020.022
Sección: 20311""",end="\n\n")

def main():
    # Variable initialization
    n = m = 5
    matrix = []
    rows_sum = []
    columns_sum = []

    # Matrix creation and filling
    matrix = create_matrix(n, m)
    matrix = fill_matrix(matrix)

    # Matrix's rows and columns sum
    rows_sum = sum_matrix_rows(matrix)
    columns_sum = sum_matrix_columns(matrix)

    # Print it all please
    print_matrix(matrix, rows_sum, columns_sum)

def create_matrix(rows:int, columns:int) -> list:
    """Creates a matrix based on the amount of rows and columns desired,
    filling it with temporary 0 values.

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
            matrix[i].append(0)
    
    return matrix

def fill_matrix(matrix:list) -> list:
    """Fills a given matrix with random numbers from 0 and 100.

    Args:
        matrix (list): The matrix to fill.

    Returns:
        list: The filled matrix.
    """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] = randrange(101)
    
    return matrix

def sum_matrix_rows(matrix:list) -> list:
    """Sums every row of the matrix and appends it to a list of rows sum.

    Args:
        matrix (list): The given matrix.

    Returns:
        list: List of rows sum.
    """
    rows_sum = []
    sum = 0

    for i in range(len(matrix)):
        for j in matrix[i]: 
            sum += j
        rows_sum.append(sum)
        sum = 0
    
    return rows_sum
            

def sum_matrix_columns(matrix:list) -> list:
    """Sums every colum of the matrix by summing each element of the matrix
    with the corresponding element of the columns sum list.

    Args:
        matrix (list): The given matrix.

    Returns:
        list: List of columns sum.
    """
    columns_sum = []

    # Appending sum elements according to amounts of columns
    for i in range(len(matrix[0])):
        columns_sum.append(0)

    # Summing columns to columns list
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            columns_sum[j] += matrix[i][j]

    return columns_sum

def print_matrix(matrix:list, rows_sum:list, columns_sum:list) -> None:
    """Prints the matrix together with the sum of each row and column.

    Args:
        matrix (list): The given matrix.
    """

    # Printing matrix with the sum of each row
    for i in range(len(matrix)):
        print("|", end=" ")
        for j in range(len(matrix[i])):
            print(f"{matrix[i][j]:^3}", end=" ")
        print(f"| → {rows_sum[i]}")
    
    # Printing the sum of the columns
    print(" " + "  ↓ "*len(matrix))
    print(" ", end="")
    for i in columns_sum:
        print(f" {i:^3}",end="")
    print()

    return None

# Execute main function
main()