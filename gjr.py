def gaussJordan(A, n):
    for i in range(n):

        # Pivoting if diagonal element is zero
        if A[i][i] == 0:
            for k in range(i + 1, n):
                if A[k][i] != 0:
                    for j in range(n + 1):
                        A[i][j], A[k][j] = A[k][j], A[i][j]
                    break

        # Make pivot element 1
        pivot = A[i][i]
        for j in range(n + 1):
            A[i][j] = A[i][j] / pivot

        # Make other elements in column zero
        for k in range(n):
            if k != i:
                factor = A[k][i]
                for j in range(n + 1):
                    A[k][j] = A[k][j] - factor * A[i][j]


def displaySolution(A, n):
    for i in range(n):
        print("x", i + 1, "=", round(A[i][n], 2))


# Example matrix
A = [
    [1, 1, 1, 6],
    [0, 2, 5, -4],
    [2, 5, -1, 27]
]

n = 3

gaussJordan(A, n)
print("Solution:")
displaySolution(A, n)