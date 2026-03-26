# Newton's Divided Difference Interpolation

# Given data
x = [-2, -1, 0, 1, 3, 4]
y = [9, 16, 17, 18, 44, 81]

n = len(x)

# Create divided difference table
table = [[0 for _ in range(n)] for _ in range(n)]

# First column = y values
for i in range(n):
    table[i][0] = y[i]

# Fill the table
for j in range(1, n):
    for i in range(n - j):
        table[i][j] = (table[i+1][j-1] - table[i][j-1]) / (x[i+j] - x[i])

# Print the table properly
print("Divided Difference Table:\n")
for i in range(n):
    for j in range(n - i):
        print(f"{table[i][j]:10.2f}", end=" ")
    print()

# Interpolation
value = 3.1
result = table[0][0]

product = 1
for i in range(1, n):
    product *= (value - x[i-1])
    result += product * table[0][i]

print("\nInterpolated value at x =", value)
print("f(3.1) =", round(result, 2))