
A = [
    [2, 3, -1, 5],
    [4, 1, 2, 6],
    [3, -2, 1, 4]
]

n = 3

# Forward Elimination
for i in range(n):
    for j in range(i + 1, n):
        ratio = A[j][i] / A[i][i]
        for k in range(n + 1):
            A[j][k] = A[j][k] - ratio * A[i][k]

# Back Substitution
x = [0] * n

x[n - 1] = A[n - 1][n] / A[n - 1][n - 1]

for i in range(n - 2, -1, -1):
    sum_value = 0
    for j in range(i + 1, n):
        sum_value += A[i][j] * x[j]
    x[i] = (A[i][n] - sum_value) / A[i][i]

# Printing Solution
print("Solution:")
print("x =", x[0])
print("y =", x[1])
print("z =", x[2])