from determinant import triangular_determinant


# Singular matrix
def test_singular_matrix():
    matrix = [
        [1, 2],
        [1, 2],
    ]
    assert triangular_determinant(matrix) == 0


# Null matrix
def test_null_matrix():
    matrix = [
        [0, 0],
        [0, 0],
    ]
    assert triangular_determinant(matrix) == 0


# Matrices with 0
def test_matrix_with_0():
    matrix1 = [
        [1, -1, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    assert triangular_determinant(matrix1) == 0

    matrix2 = [
        [1, -1, 1],
        [0, 1, 0],
        [0, 0, 2],
    ]
    assert triangular_determinant(matrix2) == 2


# Regular matrices
def test_regular_matrix():
    # 1D
    matrix1d = [
        [1]
    ]
    assert triangular_determinant(matrix1d) == 1
    # 2D
    matrix2d = [
        [1, 2],
        [3, 4],
    ]
    assert triangular_determinant(matrix2d) == -2
    # 3D
    matrix3d = [
        [1/3, 2/3, 0], 
        [3, 4, 9/2], 
        [-3, 7, 0],
    ]
    assert triangular_determinant(matrix3d) == -39 / 2
    # 4D
    matrix4d = [
        [1, 0, 1, 0], 
        [0, 1, 0, 0], 
        [1, 0, 0, 1], 
        [0, 0, 1, 1],
    ]
    assert triangular_determinant(matrix4d) == -2
