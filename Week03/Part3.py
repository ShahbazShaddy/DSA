def printMatrix(A, starting_index, rows, columns):
    for i in range(rows):
        for j in range(columns):
            print(A[i + starting_index[0]][j + starting_index[1]], end=" ")
        print()


def matAdd(A, B):
    result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]
    return result


def matAddPartial(A, B, start, size):
    result = [[0 for _ in range(size)] for _ in range(size)]
    for i in range(size):
        for j in range(size):
            result[i][j] = A[i + start[0]][j + start[1]] + B[i + start[0]][j + start[1]]
    return result


def matMul(A, B):
    rows_A = len(A)
    cols_A = len(A[0])
    cols_B = len(B[0])

    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


def matMulRecursive(A, B):
    if len(A) == 1 and len(A[0]) == 1:
        return [[A[0][0] * B[0][0]]]

    row_mid = len(A) // 2
    col_mid = len(A[0]) // 2

    A11 = [row[:col_mid] for row in A[:row_mid]]
    A12 = [row[col_mid:] for row in A[:row_mid]]
    A21 = [row[:col_mid] for row in A[row_mid:]]
    A22 = [row[col_mid:] for row in A[row_mid:]]

    B11 = [row[:col_mid] for row in B[:row_mid]]
    B12 = [row[col_mid:] for row in B[:row_mid]]
    B21 = [row[:col_mid] for row in B[row_mid:]]
    B22 = [row[col_mid:] for row in B[row_mid:]]

    C11 = matMulRecursive(A11, B11), matMulRecursive(A12, B21)
    C12 = matMulRecursive(A11, B12), matMulRecursive(A12, B22)
    C21 = matMulRecursive(A21, B11), matMulRecursive(A22, B21)
    C22 = matMulRecursive(A21, B12), matMulRecursive(A22, B22)

    return C11 + C12 + C21 + C22


def matMulStrassen(A, B):
    if len(A) != len(B[0]) or len(A[0]) != len(B):
        raise ValueError("matrix dimensions are not compatible for multiplication.")

    n = len(A)
    size = 1
    while size < n:
        size *= 2

    A_padded = [[0 for _ in range(size)] for _ in range(size)]
    B_padded = [[0 for _ in range(size)] for _ in range(size)]

    for i in range(n):
        for j in range(len(A[0])):
            A_padded[i][j] = A[i][j]
            B_padded[i][j] = B[i][j]

    result_padded = matMulRecursive(A_padded, B_padded)
    result = [[result_padded[i][j] for j in range(n)] for i in range(n)]

    return result


# Example usage
A = [[3, 4, 5], [2, 5, 7]]
B = [[1, 2, 3], [4, 3, 2]]

printMatrix(A, (0, 0), 2, 3)
print()
printMatrix(B, (0, 0), 2, 3)
print()

C = matAdd(A, B)
printMatrix(C, (0, 0), 2, 3)
print()

C_partial = matAddPartial(A, B, (0, 0), 2)
printMatrix(C_partial, (0, 0), 2, 2)
print()

C_mul = matMul(A, B)
printMatrix(C_mul, (0, 0), 2, 3)
print()

C_mul_recursive = matMulRecursive(A, B)
printMatrix(C_mul_recursive, (0, 0), 2, 3)
print()

C_mul_strassen = matMulStrassen(A, B)
printMatrix(C_mul_strassen, (0, 0), 2, 3)
