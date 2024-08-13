matrix0 = [
    [1, 2, 3],
    [4, 5, 6]
]


def create_matrix(rows, cols):
    """Create a matrix with given dimensions filled with user input."""
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            value = int(input(f"Enter value for matrix[{i}][{j}]: "))
            row.append(value)
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """Prints the matrix in a readable format."""
    for row in matrix:
        print(" ".join(map(str, row)))


rows = 3
cols = 3


#matrix1 = create_matrix(rows, cols)


def new_matrix(r, c):
    matrix = []
    for i in range(0, r):
        row = []
        for j in range(0, c):
            value = int(input(f"add the values for matrix of [{i}][{j}]: "))
            row.append(value)
        matrix.append(row)

    print(matrix)


#new_matrix(3, 3)


def get_diagonals(matrix):
    """Calculate and return the main and anti-diagonals of the matrix."""
    main_diagonal = []
    anti_diagonal = []
    rows = len(matrix)
    cols = len(matrix[0])

    for i in range(min(rows, cols)):
        main_diagonal.append(matrix[i][i])
        print(main_diagonal)
        anti_diagonal.append(matrix[i][cols - 1 - i])

    return main_diagonal, anti_diagonal


matrix3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

main_diagonal, anti_diagonal = get_diagonals(matrix3)

print("Main Diagonal:", main_diagonal)
print("Anti Diagonal:", anti_diagonal)
