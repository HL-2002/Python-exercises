"Determinant of any given matrix"
from gauss_jordan import create_matrix
from fractions import Fraction


def main():
    # Create and print matrix
    m = 1
    n = 1
    matrix = [
        [1/3, 2/3, 0], 
        [3, 4, 9/2], 
        [-3, 7, 0],
    ]
    matrix_print(matrix)

    # Calculate determinant
    print("Determinant =", triangular_determinant(matrix))


def matrix_print(matrix: list) -> None:
    """Prints the linear system of equations' extended matrix.

    Args:
        matrix (list).
        coefficients (list).
    """
    element = coefficient = ""

    # Printing matrix with each coefficient
    for i in range(len(matrix)):
        print("|", end=" ")
        for j in range(len(matrix[i])):
            # This transforms any given expression to a fraction, then cast it into a str to apply the desired format
            element = str(Fraction(matrix[i][j]).limit_denominator())
            print(f"{element:^3}".format(), end=" ")
        print("|")
    print()

    return None


def triangular_determinant(matrix: list) -> float:
    alpha = 1  # Scalar to divide determinant with
    det = 1 # Determinant value
    temp_row = []  # Temporary variable in case of a row substitution
    scalar1 = scalar2 = 0.0 # To scale rows in order to reduce them

    # Check wether it's possible to calculate determinant
    if len(matrix) != len(matrix[0]) :
        raise IndexError("Non-Square matrices have no determinant.")

    # Gaussian reduction
    # Looping through each element of the matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            # Operating only with pivots
            if i == j:
                # Replacing row if its pivot is equal to 0
                if matrix[i][j] == 0:
                    # Store the whole row in temporary variables
                    temp_row = matrix[i]
                    # Looping through the matrix rows
                    for m in range(len(matrix)):
                        # If there's a pivot different to 0, replace rows.
                        if matrix[m][j] != 0:
                            matrix[i] = matrix[m]
                            matrix[m] = temp_row
                            break

                # Reduce rest of the column under current row
                for m in range(len(matrix)):
                    if m != i and matrix[m][j] != 0:
                        # Getting scalars for reduction and compounding alpha
                        scalar1 = matrix[i][j]
                        scalar2 = matrix[m][j]
                        alpha *= scalar1
                        # Reduction
                        for n in range(len(matrix[m])):
                            matrix[m][n] = (
                                scalar1 * matrix[m][n] - scalar2 * matrix[i][n]
                            )

    # Calculate determinant of triangular matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j:
                det *= matrix[i][j]

    # Application of determinant's scaling theorem
    det /= alpha

    return Fraction(det).limit_denominator(10000)


if __name__ == "__main__":
    main()
